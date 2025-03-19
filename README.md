## Real-Time Emotion Recognition and Adaptive Tracking

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

### 📹 **Demo**  
Check out the full project demo here: [Upload your video link here]  

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
