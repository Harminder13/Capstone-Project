import cv2

def getPic():
    # Open the first camera (0 usually refers to the first USB camera)
    cap = cv2.VideoCapture(0) #If there are two cameras, swap out 0 with 1 to get the image from a different camera.

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    i = True

    while i:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame was not captured correctly, break the loop
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imwrite('DATASET/captured_frame.png', frame) #This saves the image from the camera

        i = False

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    getPic()
