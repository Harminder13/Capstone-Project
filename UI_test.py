import cv2
from ultralytics import YOLO
from rich.console import Console
from rich.table import Table
import os
import matplotlib.pyplot as plt

# Constants
MODEL_PATH = "best.pt" ### **CHANGE** (CHANGE THE PATH TO WHERE THE MODEL IS) ###
CONFIDENCE_THRESHOLD = 0.25

# Function to increase the brightness of an image
def increase_brightness(image, factor):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

# Function to crop the face from an image
def crop_face(image_path, output_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    if image is None:
        return False

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # No faces are detected to crop
    if len(faces) == 0:
        brightened_image = increase_brightness(image, 1.35)
        gray_image = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(output_path, gray_image)
        print("Cropped: 0")
        return False

    # Crop and process the first detected face
    (x, y, w, h) = faces[0]
    cropped_face = image[y:y + h, x:x + w]
    brightened_face = increase_brightness(cropped_face, 1.35)
    gray_face = cv2.cvtColor(brightened_face, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, gray_face)
    print("Cropped: 1")
    return True

# Function to load the YOLO model
def load_model(model_path, confidence_threshold):
    model = YOLO(model_path)
    model.conf = confidence_threshold
    return model

# Function to print detection results
def print_detection_results(results):
    console = Console()
    table = Table(title="Detection Results", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan", justify="left")
    table.add_column("Value", style="green", justify="left")

    for result in results:
        num_detections = len(result.boxes)
        table.add_row("Detected objects", str(num_detections))

        sorted_indices = result.boxes.conf.argsort(descending=True)
        sorted_boxes = result.boxes[sorted_indices]

        emotions = []
        # Display primary and secondary emotions with confidence
        for i, box in enumerate(sorted_boxes[:2]):
            class_id = int(box.cls)
            class_name = result.names[class_id]
            confidence = float(box.conf)
            emotion_type = "Primary Emotion" if i == 0 else "Secondary Emotion"
            table.add_row(f"  - {emotion_type}", f"{class_name} (ID: {class_id})")
            table.add_row("    Confidence", f"{confidence:.2f}")
            emotions.append(class_name)

        # Display processing times
        for key, value in result.speed.items():
            table.add_row(f"{key.capitalize()} time", f"{value:.1f}ms")

    #console.print(table)
    return emotions

# Function to display before and after images with detection results
def display_images(before_image, after_image, results):
    before_image_rgb = cv2.cvtColor(before_image, cv2.COLOR_BGR2RGB)
    annotated_image_rgb = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(before_image_rgb)
    plt.title("Before Process")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(annotated_image_rgb)
    plt.title("After Process")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

# Main function
def main():
    input_image_path = 'DATASET/captured_frame.png' ### **CHANGE** (CHANGE THE NAME OF THE "input_image" VARIABLE) ###
    cropped_face_path = 'cropped_face.jpg'

    # Check if the input image exists
    if not os.path.exists(input_image_path):
        return

    # Crop the face from the input image
    crop_face(input_image_path, cropped_face_path)
    processed_image = cv2.imread(cropped_face_path)
    if processed_image is None:
        return

    # Load the trained YOLO model
    model = load_model(MODEL_PATH, CONFIDENCE_THRESHOLD)

    # Perform detection on the cropped face
    results = model(processed_image, verbose=False)

    # Print detection results and display images
    print_detection_results(results)
    display_images(cv2.imread(input_image_path), processed_image, results)

if __name__ == "__main__":
    main()