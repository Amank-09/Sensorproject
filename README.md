# **Sensor Fault Detection**

A complete end-to-end Machine Learning pipeline built using **Python**, **Flask**, and **MongoDB** to detect faults in semiconductor wafers based on high-dimensional sensor data (~590 features).
The system supports **data ingestion**, **data transformation**, **model training**, and **batch prediction**, all exposed through simple browser routes.

---

## ✨ **Features**

* 📥 **Automated Data Ingestion** from MongoDB → CSV feature store
* 🔧 **Data Transformation Pipeline** (imputation + robust scaling)
* 🧠 **Model Training Pipeline** with performance evaluation
* 📤 **Prediction Pipeline** with automatic `predictions.csv` download
* 🌐 **Flask Web Interface** (Upload test.csv, trigger training)
* 🗂 **Modular ML architecture** (clean, production-ready)
* 🎨 **Modern UI** for upload & project overview

---

## 🧱 **Tech Stack**

* **Python 3.x**
* **Flask**
* **MongoDB**
* **Pandas**, **NumPy**
* **Scikit-Learn**
* **Custom ML Pipelines (OOP architecture)**
* **HTML/CSS (custom UI enhanced)**

---

## 📌 **Project Architecture**

The project follows a modular, clean architecture with dedicated pipelines:

---

# 📂 **How to Run the Project Locally**

### **1. Clone Repo**
```
git clone <your-repo-url>
cd sensor-fault-detection
```

### **2. Create Environment**

```
python -m venv venv
venv/Scripts/activate   # Windows
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

### **4. Run Flask App**

```
python app.py
```

### **5. Open in Browser**

```
http://localhost:5000
```

---

# 🖼 **UI Screenshot**

![Prediction Page](<img width="1450" height="900" alt="Screenshot 2025-11-25 153149" src="https://github.com/user-attachments/assets/30fbac34-101c-43c4-a8aa-d31486b9591f" />)
![Upload Page](docs/upload_ui.png)
```

---

# ♻️ **Future Improvements**

* Deploy on AWS/GCP
* Add monitoring + model drift detection
* Add retraining automation
* Add authentication layer
* Add CI/CD pipeline

---

# 👤 **Author**

**Aman Kushwaha**
B.Tech (EEE) | Machine Learning & Data Analytics

---

