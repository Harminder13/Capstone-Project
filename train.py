from ultralytics import YOLO


def train_model(model_file):
    try:
        print(f"\n[TRAINING MODE]\nLoading model: {model_file}...")
        model = YOLO(model_file)
        print("Model loaded successfully.")

        training_params = {
            "data": "data.yaml",
            "epochs": 300,
            "save": True,
            "augment": True,
            "mosaic": 0,
            "lr0": 0.01,
            "batch": 32
        }

        model.train(**training_params)
        print("\nTraining complete!")

        print("\nStarting validation...")
        model.val(data = "data.yaml", save=True, plots=True)
        print("\nValidation complete!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    choice = input("Select YOLO model:\n1. YOLO v11\n2. YOLO v8\nEnter choice (1 or 2): ").strip()
    model_file = "yolo11m.pt" if choice == "1" else "yolov8n.pt" if choice == "2" else None

    if model_file:
        train_model(model_file)
    else:
        print("Invalid choice. Exiting.")
