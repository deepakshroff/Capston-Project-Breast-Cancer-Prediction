# 🩺 Breast Cancer Risk Prediction

**Breast Cancer Risk Prediction** is a web-based ML application that predicts whether a patient has a **low or high risk of breast cancer** based on diagnostic measurements. Built using a trained machine learning model and rendered with a beautiful, responsive Flask-based frontend.

## 🔍 Screenshots

<table>
  <tr>
    <td><img src="Screenshot 2025-07-27 231531.png" width="100%"/></td>
    <td><img src="Screenshot%202025-07-27%20150009.png" width="100%"/></td>
  </tr>
</table>


---

## 🚀 Features

- ✅ Predicts whether cancer is **Benign (Low Risk)** or **Malignant (High Risk)**  
- 📊 Displays **Model Accuracy** on the interface  
- ✍️ Accepts 4 key clinical inputs: Radius Mean, Area Worst, Smoothness Worst, and Symmetry Worst  
- 🧠 Integrated with a trained `.pkl` machine learning model  
- 🎨 Clean and mobile-friendly interface with live prediction result  
- ⚙️ Flask + HTML/CSS-based responsive UI

---

## 🧪 Tech Stack

### 🖥️ Frontend
- HTML5 + CSS3 (custom styling)
- JavaScript (for AJAX form submission)
- Jinja2 (Flask templating)

### 🧠 Backend
- Python 3.x
- Flask Framework
- Scikit-learn (ML model training and prediction)
- Pickle (`.pkl`) file for model persistence

### 🛠 Development Tools
- VS Code
- Chrome/Edge
- GitHub for version control

---

## 💡 How to Use

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Breast-Cancer-Prediction.git
   cd Breast-Cancer-Prediction

---

## 🧠 How It Works
- User fills in medical parameters (e.g., Radius Mean, Area Worst)
- Data is sent to Flask backend via JavaScript (AJAX POST)
- Trained ML model (Breast_Cancer_Model.pkl) makes a prediction
- Prediction result is returned as Benign ✅ or Malignant ⚠️

## 🔮 Future Improvements
- 📥 Add CSV upload for batch predictions
- 📊 Store and visualize prediction history
- 🧬 Include more clinical features for better accuracy
- ☁️ Deploy to Render or Railway for public use

---

## 🙌 Acknowledgements
- 🧠 Scikit-learn for ML
- 🧪 UCI Breast Cancer Dataset
- 🔥 Mr. Lokesh Sir for mentorship
- 💻 Flask + HTML for UI integration

---