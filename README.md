# 🧠 Study Tracker Web App

A clean and minimal **study tracking web application** built with **Flask**.
This app allows users to record study sessions, track progress, and visualise completed study time.


## 🚀 Features

* Add study records (subject + hours)
* Automatically store the date of each session
* Mark tasks as completed or undo completion
* Edit existing study records
* Delete records
* Track progress through:

  * Total records
  * Completed tasks
  * Pending tasks
  * Total completed study hours
* Clean, modern, and user-friendly UI


## 🛠 Tech Stack

* Python 3
* Flask
* SQLite
* HTML / CSS


## 📦 Project Structure

```
study-tracker/
│── app.py
│── study.db
│── templates/
│   └── index.html
│── README.md
```


## ▶️ How to Run

1. Install Flask:

```
pip install flask
```

2. Run the application:

```
python app.py
```

3. Open in browser: http://127.0.0.1:5000

## 📊 How It Works

* Each study record is stored in a SQLite database.

* Every record includes:

  * Subject
  * Study hours
  * Completion status
  * Date

* Only completed study sessions contribute to total study hours,
  providing a more accurate measure of productivity.


## 💡 Example Workflow

1. Add a study session
   → e.g. "Mathematics - 2 hours"

2. Mark it as completed
   → included in total study hours

3. Edit or delete if needed


## 🎨 UI Design

* Soft pastel colour palette (blue / grey tones)
* Rounded and modern components
* Clear visual distinction between:

  * ✔ Completed
  * ○ Not Completed
* Responsive layout for different screen sizes


## 📈 Future Improvements

* Filter by date (today / week)
* Study analytics (charts)
* User authentication
* Subject-based tracking


## ⭐ Notes

This project was developed to practice:

* Backend development with Flask
* Database integration (SQLite)
* CRUD operations
* UI/UX design for web applications
