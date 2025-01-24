# Multiple-Choice Questionnaire (MCQ) Application

## Overview

MCQ-App is an interactive application designed to offer Multiple Choice Question (MCQ) quizzes with comprehensive user management and progress tracking. It includes both GUI and console modes to enhance user accessibility and flexibility. The app also features an admin panel for managing quizzes, categories, and users.

## Features

### Core Features
- **User Management**: 
  - Role-based system: Admins and Students.
  - Users can register, log in, and view their quiz history.
- **Quizzes**:
  - Multiple-choice quizzes with categories and difficulty levels (easy, medium, hard).
  - Automatic feedback on answers with final scores.
- **Admin Panel**:
  - Admins can manage users, questions, and categories.
  - Add, edit, or delete questions within categories .
- **History Tracking**:
  - Students can view detailed history of their quizzes, including correct answers and performance summaries.
  - Results are exported to CSV files.

### Advanced Features
- **Difficulty-Based Timers**:
  - Timer durations adapt based on the quiz difficulty level.
- **Export Results**:
  - Admins can export quiz results and question statistics for analysis.
- **Error Handling**:
  - Graceful handling of invalid inputs and missing data in both GUI and console modes.

## Requirements and Installation

### Prerequisites
- Python 3.9 or higher.
- Required Python packages:
  - `CustomTkinter`
  - `rich`

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Abdou-bnm/MCQ-App)
   ```
2. Navigate to the project directory:
   ```bash
   cd MCQ-App
   ```
3. Install the required dependencies:
   ```bash
   pip install requirements.txt
   ```

### Running the Application
- **GUI Mode**:
  ```bash
  python src/GUI/main.py
  ```

- **Console Mode**:
  ```bash
  python src/Console/main.py
  ```

Ensure you have installed all dependencies before running the application:
```bash
pip install requirements.txt
```

## Project Structure

The project is organized as follows:

```
├── data/
│   ├── questions_1.json  # Stores all questions, categories, and levels
│   ├── users.json        # Stores user profiles and history
│   └── results/          # Folder for exported results (CSV files)
├── src/
│   ├── Console           # Console mode implementation
│   │   ├── main.py       # Entry point for console mode
│   │   ├── Quiz.py       # Handles quiz logic in console mode
│   │   ├── user_management.py
│   │   └── ...
│   ├── GUI/              # GUI mode implementation
│   │   ├── main.py       # Entry point for GUI mode
│   │   ├── Admin_Panel.py
│   │   └── ...
│   └── tests/        
│       ├── test_questions.py
│       └── test_users.py
│       └── ...
├── README.md             # Documentation for the project
├── requirements.txt      # Dependencies for the project
└── .gitignore            # Files to ignore in version control
```

## Usage Instructions

### Students
1. **Log In or Register**:
   - Log in using an existing username or register as a new user.
2. **Take a Quiz**:
   - Choose a category and difficulty level.
   - Answer the multiple-choice questions within the time limit.
3. **View History**:
   - Access detailed history of past quizzes, including scores and correct answers.

### Admins
1. **Log In as Admin**:
   - Use an admin account to access the Admin Panel.
2. **Manage Questions ,Categories and Users**:
   - Add, edit, or delete categories and questions.
3. **Export Results**:
   - Export student quiz results and question statistics to CSV files.
  
## Known Issues
- Ensure all dependencies are installed correctly to avoid module import errors.
- Compatibility may vary with Python versions below 3.9.
- JSON files must maintain valid syntax to prevent application crashes.
  
## Technologies Used

- 🐍 **Python**&#x20;
- 🖼️ **CustomTkinter** (GUI)&#x20;
- ⚡ **Rich Library** (Console UI)&#x20;
- 📄 **JSON** (Data storage)
- 📄 **CSV** (Data storage) 


## Known Issues

- ⚠️ Ensure all dependencies are installed to avoid runtime errors.

## Contributing

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`feature/YourFeature`).
3. 💾 Commit your changes (`git commit -m 'Add new feature'`).
4. 📤 Push to the branch (`git push origin feature/YourFeature`).
5. 🔀 Open a Pull Request.


   



