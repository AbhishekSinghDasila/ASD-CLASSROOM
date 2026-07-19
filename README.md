# 🎓 ASD Classroom
### AI-Powered Smart Attendance System using Face Recognition & Voice Recognition

SnapClass is an intelligent classroom attendance management platform that leverages Artificial Intelligence, Computer Vision, and Voice Recognition to automate attendance tracking. Instead of traditional manual attendance, teachers can simply capture a classroom image or record students' voices, and the system automatically identifies students and marks attendance.

The application is built using **Streamlit** for the frontend, **Supabase (PostgreSQL)** for cloud database management, **dlib** for facial recognition, **Resemblyzer** for speaker recognition, and **Scikit-learn** for machine learning-based student identification.

---

## 🚀 Features

### 👨‍🏫 Teacher Features

- Secure Teacher Registration & Login
- Create and Manage Subjects
- Generate QR Code / Join Code
- Share Subject Enrollment Links
- Face Recognition Attendance
- Voice Recognition Attendance
- Review AI Predictions before Saving
- Attendance History
- Student Enrollment Statistics

### 👨‍🎓 Student Features

- Face-ID Login
- Student Registration
- Face Enrollment
- Optional Voice Enrollment
- Join Subjects via QR Code
- View Enrolled Subjects
- Attendance Dashboard
- Unenroll from Subjects

---

# 🤖 AI Capabilities

## Face Recognition

- Automatic face detection
- Face embedding generation
- Student identification using Machine Learning
- Multiple face detection
- Face-ID based authentication

Technologies

- dlib
- Face Recognition Models
- Scikit-Learn
- Support Vector Machine (SVM)

---

## Voice Recognition

- Voice embedding generation
- Speaker identification
- Silence detection
- Multi-speaker attendance
- Optional voice enrollment

Technologies

- Resemblyzer
- Librosa
- PyTorch

---

# 🏗️ System Architecture

```
             Streamlit Frontend
                     │
        ┌────────────┴────────────┐
        │                         │
 Teacher Dashboard        Student Dashboard
        │                         │
        ├────────────┬────────────┤
        │            │
 Face Pipeline   Voice Pipeline
        │            │
        └──────┬─────┘
               │
        Supabase PostgreSQL
```

---

# 🛠 Tech Stack

### Frontend

- Streamlit
- HTML
- CSS

### Backend

- Python

### Database

- Supabase
- PostgreSQL

### Machine Learning

- Scikit-Learn
- dlib
- Resemblyzer
- Librosa
- NumPy
- Pandas

### Authentication

- Face-ID
- bcrypt Password Hashing

### Other Libraries

- OpenCV
- Segno (QR Code)
- Matplotlib

---

# 📂 Project Structure

```
SnapClass/
│
├── app.py
├── requirements.txt
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── assets/
├── .streamlit/
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/SnapClass.git

cd SnapClass
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Supabase

Create

```
.streamlit/secrets.toml
```

Add

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_KEY"
```

## Run

```bash
streamlit run app.py
```

---

# 📊 Database

The application uses **Supabase PostgreSQL** with the following tables:

- Teachers
- Students
- Subjects
- Subject Students
- Attendance Logs

---

# 🔐 Security

- Passwords hashed using bcrypt
- Secure cloud database
- Face-ID authentication
- Optional voice verification
- Supabase cloud storage

---

# 📈 Future Improvements

- Liveness Detection
- Face Anti-Spoofing
- Attendance Analytics Dashboard
- CSV/PDF Report Export
- Mobile Application
- Email Notifications
- Docker Deployment
- Multi-factor Authentication
- Role-Based Access Control
- Real-Time Attendance Dashboard

---

# 🎯 Use Cases

- Schools
- Universities
- Coaching Institutes
- Training Centers
- Corporate Training Programs

---

# 👨‍💻 Author

**Abhishek Singh Dasila**

M.Tech – Information Technology  
Indian Institute of Information Technology, Allahabad

GitHub:
https://github.com/AbhishekSinghDasila

---

# ⭐ If you like this project

Give this repository a ⭐ and consider following for more AI and Full Stack projects.
