## Capstone Project: Machine Learning System for Emotion Recognition and Adaptive Tracking

### 📌 **Project Overview**  
This project focuses on developing a machine learning-based system capable of detecting and displaying a user’s emotions through a camera that **automatically adjusts to their height** and centers on their face in real time. The system is designed to enhance personalized interactions by providing accurate emotional feedback in various settings, such as **mental health assessments**, **customer service**, and **virtual meetings**.  

Our solution addresses critical challenges such as:  
✅ Variable lighting conditions  
✅ Accurate face alignment and tracking  
✅ Multi-emotion detection for enhanced precision  
✅ Privacy and data security  

The motivation behind this project is to improve assistive technology by fostering more empathetic and responsive communication.  

---

### 🎯 **Goals and Scope**  
The project is divided into two main components:  

1. **Software Component:**  
   - Machine learning model for emotion recognition using real-time facial expression analysis.  
   - Secondary emotion display to enhance accuracy in ambiguous cases.  
   - Integration of facial tracking to maintain camera alignment with the user’s face.  

2. **Hardware Component:**  
   - A dynamic camera mount constructed via 3D printing.  
   - The mount is attached to a belt-driven system that automatically adjusts to the user’s height in real time based on the software’s feedback.  

---

### 🚀 **Key Features**  
✅ Real-time facial expression detection  
✅ Dynamic camera adjustment to follow face movements  
✅ Multi-emotion classification  
✅ Efficient and cost-effective hardware design  
✅ Privacy-first approach to data handling  

---

### 💡 **Interface**  
The project involves three key interfaces:  

1. **Camera Interface**  
   - Python is used with the OpenCV library to capture real-time images from the camera.  
   - The image is processed and fed into the deep learning model to detect facial emotions.  
   - The image can be stored locally for future reference or debugging.  

2. **User Interface**  
   - A simple display on the computer screen shows:  
     - Predicted emotion as text.  
     - Captured image shown in the bottom right corner of the screen.  
     - If detected, a secondary emotion will appear in smaller text under the primary emotion.  

3. **Motor Interface**  
   - The camera mount is adjusted using a **Hitec HS-785HB sail winch servomotor**.  
   - This motor can rotate up to **7.85 revolutions**, allowing a vertical height adjustment of approximately **92 cm** (~1 meter).  
   - A **Pololu Micro Maestro USB Servo Controller** manages the motor's positioning through commands sent via Python using the **Pyserial** library.  
   - The servomotor ensures precise vertical alignment to keep the face centered.  

---

## 📊 **Model Performance and Results**  
Our model achieved impressive results during testing and validation. Below are key performance metrics and visualizations:  

### ✅ **F1 Score Curve**  
The F1 Score Curve shows the model's performance in terms of precision and recall across different epochs, indicating balanced learning.  
![F1 Curve](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/F1_curve.png)  

---

### ✅ **Precision-Recall Curve**  
The Precision-Recall Curve illustrates the trade-off between precision and recall, helping to understand the model’s sensitivity and specificity.  
![PR Curve](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/PR_curve.png)  

---

### ✅ **P Curve (Precision)**  
This graph shows how well the model maintains precision over time during training and validation.  
![P Curve](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/P_curve.png)  

---

### ✅ **R Curve (Recall)**  
The R Curve measures how effectively the model detects positive samples.  
![R Curve](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/R_curve.png)  

---

### ✅ **Confusion Matrix**  
The confusion matrix shows the number of correct and incorrect predictions for each class.  
![Confusion Matrix](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/confusion_matrix.png)  

---

### ✅ **Normalized Confusion Matrix**  
The normalized confusion matrix provides a clearer understanding of the model's classification accuracy by showing percentage-based values.  
![Normalized Confusion Matrix](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/confusion_matrix_normalized.png)  

---

### 🎯 **Training and Validation Results**  
Here are sample outputs from the training and validation process, showing the model's predictions versus the ground truth:

#### **Validation Results**  
- **Validation Batch 0 (Labels vs Predictions):**  

**Labels:**  
![Validation Batch 0 Labels](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/val_batch0_labels.jpg)  

**Predictions:**  
![Validation Batch 0 Predictions](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/val_batch0_pred.jpg)  

---

- **Validation Batch 1 (Labels vs Predictions):**  

**Labels:**  
![Validation Batch 1 Labels](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/val_batch1_labels.jpg)  

**Predictions:**  
![Validation Batch 1 Predictions](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/val_batch1_pred.jpg)  

---

- **Validation Batch 2 (Labels):**  
![Validation Batch 2 Labels](https://raw.githubusercontent.com/Harminder13/Capstone-Project/main/Model%233_YoloV11s_Dataset%232/val_batch2_labels.jpg)  

---

### 🌍 **Challenges and Considerations**  
- Ensuring accurate emotion detection in varying lighting conditions.  
- Addressing potential bias by considering cultural diversity in emotional expressions.  
- Maintaining user privacy and preventing the perception of surveillance.  
- Balancing cost-effectiveness with high-performance components.  

---

### 💡 **Impact and Applications**  
This project has the potential to improve human-computer interaction in areas such as:  
- **Mental Health:** Providing real-time emotional feedback to improve therapy outcomes.  
- **Customer Service:** Enhancing customer interactions by identifying and responding to emotional cues.  
- **Virtual Meetings:** Creating more engaging and empathetic communication environments.  

---

### 📹 **Project Demo**  
Check out the full project demo here:  

[![Watch the demo](https://img.youtube.com/vi/nWPFgpKB1sE/0.jpg)](https://www.youtube.com/watch?v=nWPFgpKB1sE)  


---

### 👥 **Contributors**  
- Justin Hoddenbagh
- Jide Obatolu
- Liam O’Regan
- Harminder Saini 

---
### 📄 **License**  
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.  

---


