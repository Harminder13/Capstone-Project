import os
import tkinter as tk
from tkinter import ttk, filedialog
import cv2
import keyboard
import servo
import UI_test
import time

RATE_MAX = 30000

NUM_NO_EMOTION = 4
NUM_CAM_LOC_STEPS = 5

CROP_AMOUNT = 2
CROP = True

class Application(tk.Frame):
    def __init__(self, master=None):
        self.CAMERA_NUM = 1
        self.PIC_FREQUENCY = 1000  # How often a picture is taken from the camera. (ms)
        tk.Frame.__init__(self, master)
        self.continuous = False
        self.master = master
        self.grid(sticky='nsew')
        self.time_since_last_image = int(time.time() * 1000)
        self.interrupt_time = 50

        # Definitions for the model
        self.MODEL_PATH = "best.pt"  ### **CHANGE** (CHANGE THE PATH TO WHERE THE MODEL IS) ###
        self.CONFIDENCE_THRESHOLD = 0.25
        self.model = UI_test.load_model(self.MODEL_PATH, self.CONFIDENCE_THRESHOLD)
        self.noEmotionNum = 0

        # Definitions for the Servo
        self.s = servo.Servo('COM5', 0)
        self.s.setAccel(5)
        self.s.setSpeed(4)
        self.s.setLimits(1000, 1600)
        self.s.setPos(1200)
        self.moveDirectionUp = False
        self.minSet = False
        self.maxSet = False
        self.createWidgets()
        self.image = 0
        self.last_image = 0
        self.cap = cv2.VideoCapture(self.CAMERA_NUM)  # If there are two cameras, swap out 0 with 1 to get the image from a different camera.

    def __del__(self):
        self.cap.release()

    def toggleContinuous(self):
        if (self.minSet and self.maxSet):
            self.continuous = not self.continuous
        else:
            self.status.configure(text="Warning: Cannot take continuous images until maximum and minimum heights are set.")

    def setSource(self):
        self.continuous = False
        src = self.cameraSource.get()
        if src.isnumeric() and not self.CAMERA_NUM == int(src):
            self.CAMERA_NUM = int(src)
            self.cap = cv2.VideoCapture(self.CAMERA_NUM)

    def setRate(self):
        rateValid = True
        rate = self.pictureRate.get()
        if not rate.isnumeric():
            rate = self.PIC_FREQUENCY
            rateValid = False
        else:
            rate = int(rate)
            if rate < 1:
                rate = 1
                rateValid = False
            elif rate > RATE_MAX:
                rate = RATE_MAX
                rateValid = False

        self.PIC_FREQUENCY = rate
        if not rateValid:
            self.status.configure(text="Warning: Picture rate has been capped between 1 and " + str(RATE_MAX))

    def takeUpload(self):
        self.image = tk.filedialog.askopenfilename()

    def takeSingle(self):
        self.continuous = False
        self.getPic(False)

    def getPic(self, moveBit):
        # Open the first camera (0 usually refers to the first USB camera)
        try:
            self.last_image = tk.PhotoImage(file="DATASET/captured_frame.png")
        except:
            print("couldn't find an image")
            self.status.configure(text="Error: Could not retrieve the image for the captured frame")
        print("Trying to get a pic")

        # self.setSource()
        if not self.cap.isOpened():
            print("Cannot open camera")
            self.status.configure(text="Error: Could not open the camera at that index - maybe try another one?")
            return

        i = True

        self.status.configure(text="Status: Trying to get a picture")
        while i:
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # If the frame was not captured correctly, break the loop
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                self.status.configure(text="Error: Could not retrieve the next frame from the camera")
                break

            if CROP:
                width = int(len(frame[0])/CROP_AMOUNT)
                height = int(len(frame[1])/CROP_AMOUNT)
                topleftcorner = [int((len(frame[0])/2)-(width/2)), int((len(frame[1])/2)-(height/2))]
                print(f"True Width: {len(frame[0])}")
                print(f"True Height: {len(frame[0])}")
                print(f"Halved Width: {width}")
                print(f"Halved Height: {height}")
                print(f"Top left corner: {topleftcorner}")

                frame = frame[topleftcorner[0]:width+topleftcorner[0], topleftcorner[1]:height+topleftcorner[1]]

            # Break the loop on 'q' key press
            if cv2.waitKey(1) == ord('q'):
                break
            cv2.imwrite('DATASET/captured_frame.png', frame)  # This saves the image from the camera
            i = False

        # When everything done, release the capture
        self.image = tk.PhotoImage(file="DATASET/captured_frame.png")
        self.cameraOutput.config(image=self.image)
        self.status.configure(text="Status: Captured a frame from the camera, processing the image")
        input_image_path = 'DATASET/captured_frame.png'  ### **CHANGE** (CHANGE THE NAME OF THE "input_image" VARIABLE) ###
        cropped_face_path = 'cropped_face.jpg'

        # Check if the input image exists
        if not os.path.exists(input_image_path):
            return

        # Crop the face from the input image
        UI_test.crop_face(input_image_path, cropped_face_path)
        processed_image = cv2.imread(cropped_face_path)
        if processed_image is None:
            return

        # Perform detection on the cropped face
        results = self.model(processed_image, verbose=False)

        # Print detection results and display images
        emotions = UI_test.print_detection_results(results)
        if (len(emotions) == 1):
            self.noEmotionNum = 0
            self.emotion1.config(text=emotions[0])
            self.emotion2.config(text="-")
        elif(len(emotions) == 2):
            self.noEmotionNum = 0
            self.emotion1.config(text=emotions[0])
            self.emotion2.config(text=emotions[1])
        else:
            self.noEmotionNum = self.noEmotionNum+1
            if (moveBit and self.noEmotionNum > NUM_NO_EMOTION):
                self.noEmotionNum = 0
                move = int((self.s.upper_limit-self.s.lower_limit)/NUM_CAM_LOC_STEPS)
                print(f"move: {move}")
                print(f"Moving up {self.moveDirectionUp}")
                if self.moveDirectionUp:
                    newPos = self.s.getAttemptedPos()-move
                    self.s.setPos(newPos)
                    if newPos <= self.s.lower_limit:
                        self.moveDirectionUp = False
                else:
                    newPos = self.s.getAttemptedPos() + move
                    self.s.setPos(newPos)
                    if newPos >= self.s.upper_limit:
                        self.moveDirectionUp = True
            self.emotion1.config(text="-")
            self.emotion2.config(text="-")
            self.status.configure(text="Status: Done!")

    def setMinPos(self):
        self.s.setLimits(self.s.lower_limit, self.s.getAttemptedPos())
        self.minSet = True
        self.status.configure(text="Status: Set minimum height.")

    def setMaxPos(self):
        self.s.setLimits(self.s.getAttemptedPos(), self.s.upper_limit)
        self.maxSet = True
        self.status.configure(text="Status: Set maximum height.")

    def resetHeight(self):
        self.continuous = False
        self.s.setLimits(1000, 2000)
        self.maxSet = False
        self.minSet = False
        self.status.configure(text="Status: Reset minimum and maximum heights.")

    def createWidgets(self):
        # Main Frame
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.grid(sticky='nsew')

        # Configure mainFrame to expand and resize
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

        # Frame for camera selection and display
        self.cameraFrame = ttk.Frame(self.mainFrame)

        # Frame for emotion display
        self.emotionFrame = ttk.Frame(self.mainFrame)

        # Frame for application controls
        self.controlFrame = ttk.Frame(self.mainFrame)

        # Camera widgets
        self.cameraSourceCaption = ttk.Label(self.cameraFrame, text="Camera #:")
        self.cameraSource = ttk.Spinbox(self.cameraFrame, increment=1, from_=0, to=1, command=self.setSource)
        self.cameraSource.set(self.CAMERA_NUM)
        self.cameraOutputCaption = ttk.Label(self.cameraFrame, text="Camera Output", anchor="center")
        self.image = tk.PhotoImage(file="PicOfTheGroup.png")
        self.cameraOutput = ttk.Label(self.cameraFrame, image=self.image, anchor="center")

        # Emotion widgets
        large_font = ('Helvetica', 30)
        self.emotion1Caption = ttk.Label(self.emotionFrame, text="You are most likely feeling:", anchor="center")
        self.emotion2Caption = ttk.Label(self.emotionFrame, text="Or, you might be:", anchor="center")
        self.emotion1 = ttk.Label(self.emotionFrame, text="-", anchor="center", font=large_font)
        self.emotion2 = ttk.Label(self.emotionFrame, text="-", anchor="center", font=large_font)

        # Control widgets
        self.pictureUpload = ttk.Button(self.controlFrame, text="Upload")
        self.pictureSingle = ttk.Button(self.controlFrame, text="Take Single", command=self.takeSingle)
        self.pictureContinuous = ttk.Button(self.controlFrame, text="Take Continuous", command=self.toggleContinuous)
        self.pictureRate = ttk.Spinbox(self.controlFrame, increment=1, from_=100, to=RATE_MAX, command=self.setRate)
        self.pictureRate.set(self.PIC_FREQUENCY)
        self.heightMin = ttk.Button(self.controlFrame, text="Set Min Height", command=self.setMinPos)
        self.heightMax = ttk.Button(self.controlFrame, text="Set Max Height", command=self.setMaxPos)
        self.heightReset = ttk.Button(self.controlFrame, text="Reset Max/Min Height", command=self.resetHeight)
        self.pictureRateCaption = ttk.Label(self.controlFrame, text="Rate (ms):")

        # Status label
        self.status = ttk.Label(self.mainFrame, text="Status: Waiting for camera input", anchor="center")

        # Layout for camera widgets
        self.cameraSourceCaption.grid(column=0, row=0, sticky="nsw")
        self.cameraSource.grid(column=0, row=0, sticky="nse")
        self.cameraOutputCaption.grid(column=0, row=1, sticky="nsew")
        self.cameraOutput.grid(column=0, row=2, sticky="nsew")
        self.cameraFrame.columnconfigure(0, weight=1)
        self.cameraFrame.rowconfigure(2, weight=1)

        # Layout for emotion widgets
        self.emotion1Caption.grid(column=0, row=0, sticky="nsew")
        self.emotion2Caption.grid(column=1, row=0, sticky="nsew")
        self.emotion1.grid(column=0, row=1, sticky="nsew")
        self.emotion2.grid(column=1, row=1, sticky="nsew")
        self.emotionFrame.columnconfigure(0, weight=1)
        self.emotionFrame.columnconfigure(1, weight=1)
        self.emotionFrame.rowconfigure(1, weight=1)

        # Layout for control widgets
        self.pictureUpload.grid(column=0, row=0, columnspan=3, sticky="nsew")
        self.pictureSingle.grid(column=0, row=1, columnspan=3, sticky="nsew")
        self.pictureContinuous.grid(column=0, row=2, columnspan=3, sticky="nsew")
        self.pictureRateCaption.grid(column=0, row=4, sticky="nsw")
        self.pictureRate.grid(column=2, row=4, sticky="nse")
        self.heightMin.grid(column=0, row=3, sticky="nsew")
        self.heightMax.grid(column=1, row=3, sticky="nsew")
        self.heightReset.grid(column=2, row=3, sticky="nsew")
        self.controlFrame.columnconfigure(0, weight=1)
        self.controlFrame.columnconfigure(1, weight=1)
        self.controlFrame.columnconfigure(2, weight=1)
        self.controlFrame.rowconfigure(0, weight=1)

        # Layout for whole window
        self.cameraFrame.grid(row=0, sticky="nsew")
        self.emotionFrame.grid(row=1, sticky="nsew")
        self.controlFrame.grid(row=2, sticky="nsew")
        self.status.grid(row=3, sticky="nsew")

        # Configure root window for resizing
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # Make sure frames resize as well
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.run_task()

    def run_task(self):
        current_time_ms = int(time.time() * 1000)
        if (current_time_ms - self.time_since_last_image >= self.PIC_FREQUENCY):
            if self.continuous:
                self.time_since_last_image = int(time.time() * 1000)
                self.getPic(True)
            if self.pictureRate.focus:
                self.setRate()

        if keyboard.is_pressed('down'):
            self.s.setPos(self.s.getAttemptedPos()+5)
            print(self.s.getAttemptedPos())
        if keyboard.is_pressed('up'):
            self.s.setPos(self.s.getAttemptedPos()-5)
            print(self.s.getAttemptedPos())

        self.after(self.interrupt_time, self.run_task)


app = Application(master=tk.Tk())
app.master.title("Emotion Detector")
app.mainloop()

