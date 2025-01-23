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
   git clone [<repository-url>](https://github.com/Abdou-bnm/MCQ-App)
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

## Screenshots

### 1. Login Page
Console:
![image](https://github.com/user-attachments/assets/dc95a876-97cb-4f15-9cb8-c3f4ec5d9fec)
Gui:
![image](https://github.com/user-attachments/assets/70285d02-989a-4732-b5d4-7507926079a4)

### 2. Main Menu
Console:
![image](https://github.com/user-attachments/assets/0d348f5e-63bd-4cbe-bec0-6a207ac9b34e)
Gui:
![image](https://github.com/user-attachments/assets/417d1d62-8b79-4ba2-a4e3-a032765e30ba)

### 3. Quiz Interface
Console :
![Quiz Interface](path/to/quiz_screenshot.png)
![image](https://github.com/user-attachments/assets/3420c662-e1ff-4650-b92a-f1e9abde3e4b)
![image](https://github.com/user-attachments/assets/ab9611cc-ac14-4be7-9f4e-a23755f870b1)
![image](https://github.com/user-attachments/assets/9c62ad25-c0c1-4eca-9036-76ab2a809b30)
![image](https://github.com/user-attachments/assets/95582028-5cd8-4230-bcb6-ca3cd31d1a84)
Gui :
![image](https://github.com/user-attachments/assets/4d890747-f7fc-4a1d-b664-19994c69dcb6)
![image](https://github.com/user-attachments/assets/1632727f-47b6-4590-93df-832a360ceaad)
![image](https://github.com/user-attachments/assets/5ae8d28d-b0fd-461e-8f4b-9b3b6dab45c9)
![image](https://github.com/user-attachments/assets/1889e31f-c58d-4bf2-98ac-1299d311eb80)
![image](https://github.com/user-attachments/assets/7af55b42-0106-4601-9b1f-d08347ad60cb)


### 4. Admin Panel
![Admin Panel](path/to/admin_screenshot.png)
Gui:
![image](https://github.com/user-attachments/assets/4464feca-474f-4850-83c0-efe0e8e26225)

### 5. History Tracker
Console:
![image](https://github.com/user-attachments/assets/87e624d2-8458-423d-97f1-0a69bf6637bb)
![image](https://github.com/user-attachments/assets/706d1329-5ad4-4ae3-ad5d-2ade99531e43)

Gui:
![image](https://github.com/user-attachments/assets/a6027268-a5cf-4e2f-9501-d59fab159177)
![image](https://github.com/user-attachments/assets/e52bef5a-6812-49d6-83bf-1a6910331c8f)



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


   



