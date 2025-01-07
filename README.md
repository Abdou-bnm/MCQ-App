# QCM (Multiple Choice Questions) Application

A Python-based command-line application for managing and taking multiple-choice quizzes across various subjects and difficulty levels.

## 🌟 Features

- User Management System
- Multiple Quiz Categories
- Different Difficulty Levels (Easy, Medium, Hard)
- Score Tracking and History
- Detailed Performance Analytics
- Export Results to CSV
- Rich Console Interface

## 📁 Project Structure

```
qcm-application/
├── data/
│   ├── users.json         # User data and history
│   ├── questions_1.json   # Quiz questions database
│   └── results/          # Quiz results in CSV format
├── src/
│   ├── main.py               # Application entry point
│   ├── Quiz.py              # Quiz logic implementation
│   ├── question_manager.py   # Questions handling
│   ├── user_management.py    # User management system
│   ├── evaluation_system.py  # Score evaluation system
│   └── history_tracker.py    # User history tracking
```

## 🔧 Requirements

- Python 3.8+
- Rich library (`pip install rich`)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/qcm-application.git
cd qcm-application
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src\main.py
```

## 💻 Usage

### Starting the Application

When you run the application, you'll be prompted to enter your username. If you're a new user, a profile will be created automatically.

```bash
Enter your username: Abdou
```

### Main Menu

The application presents three main options:
1. Start MCQ Test
2. View History
3. Exit Application

### Taking a Quiz

1. Select "Start MCQ Test"
2. Choose a category (Python, Science, Math, etc.)
3. Select difficulty level (Easy, Medium, Hard)
4. Answer the questions by entering the number corresponding to your choice

Example interaction:
```
Available Categories:
1. Python
2. Science
3. Math
4. Geography
5. Object-Oriented Programming (OOP)
6. File and Folder Structures
7. Databases

Select a category (number): 1

Available Levels:
1. easy
2. medium
3. hard

Select a level (number): 1

Starting quiz in Python - easy level...

Question 1: Which keyword is used to define a function in Python?
1. def
2. func
3. lambda

Your answer (number): 1
✔ Correct!
```

### Viewing History

Select "View History" to see:
- Previous quiz attempts
- Scores and dates
- Detailed feedback for each attempt

## 📊 Score Tracking

The application tracks:
- Raw score (number of correct answers)
- Percentage score
- Date and time of attempt
- Category and difficulty level
- Individual question responses

## 📝 Results Export

After each quiz:
- Results are automatically saved to CSV files in the `data/results/` directory
- Files are named with format: `results_username_timestamp.csv`
- Contains detailed feedback for each question


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
