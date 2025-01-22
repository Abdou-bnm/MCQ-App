# MCQ-App

## Overview

MCQ-App is an interactive application designed to offer Multiple Choice Question (MCQ) quizzes with comprehensive user management and progress tracking. It includes both GUI and console modes to enhance user accessibility and flexibility. The app also features an admin panel for managing quizzes, categories, and users.

## Features

- 🔐 **User Management:** Login, signup, and role-based access control\
    `src/login.py`, `src/Console/user_management.py`
- 📝 **MCQ Quizzes:** Various categories with real-time feedback and performance tracking based on difficulty level\
    `src/qcm_app.py`, `src/Console/Quiz.py`
- 🛠️ **Admin Panel:** Manage users, questions, and categories efficiently\
    `src/Admin_Panel.py`
- ⏳ **Difficulty-Based Timers:** Adjustable quiz timers based on selected difficulty\
    `src/Logic/difficulty_based_timer.py`
- 📊 **History Tracking:** Track quiz progress and results by difficulty level\
    `src/view_history.py`, `src/Console/history_tracker.py`
- 🖥️ **Multi-Mode Support:** GUI (`main` and `GUI` branches) and console (`console` branch) interfaces

## Requirements

- **Python:** Version 3.x or higher
- **Libraries:**
  - customtkinter (for GUI)
  - rich (for console enhancements)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/MCQ-App.git
   cd MCQ-App
   ```

2. **Install Dependencies:**

   ```bash
   pip install customtkinter rich
   ```

3. **Run the Application:**

   - **GUI Mode (Main/GUI Branch):**
     ```bash
     python src/main.py
     ```
   - **Console Mode (Console Branch):**
     ```bash
     python src/Console/main.py
     ```

## Usage Instructions

- 🔑 **Login/Sign Up:** Create an account or log in with existing credentials.
- 🏆 **Start a Quiz:** Select a category and difficulty, then begin the quiz.
- 📂 **View History:** Access past results, tracked by difficulty level.
- ⚙️ **Admin Features:** Log in as an admin to manage questions, users, and categories.

## Screenshots/Demos

Enhance your understanding of the MCQ-App with these visuals:

- 🔑 **Login Page**&#x20;

- 🏠 **Home/Dashboard**&#x20;

- ❓ **Quiz Interface**&#x20;

- 📈 **History Page**&#x20;

- 🛠️ **Admin Panel**&#x20;

## Execution Examples

- **Running GUI Mode (Main/GUI Branch):**
  ```bash
  python src/main.py
  ```
- **Running Console Mode (Console Branch):**
  ```bash
  python src/Console/main.py
  ```

## Admin Panel

1. **🔑 Login as Admin:** Use admin credentials to access the panel.
2. **📝 Manage Content:** Add, edit, or delete users, questions, and categories.
3. **📊 Track Performance:** View user progress and quiz statistics by level.

## Technologies Used

- 🐍 **Python**&#x20;
- 🖼️ **CustomTkinter** (GUI)&#x20;
- ⚡ **Rich Library** (Console UI)&#x20;
- 📄 **JSON** (Data storage)
- 📄 **CSV** (Data storage) 

## Known Issues

- ⚠️ Ensure all dependencies are installed to avoid runtime errors.
- 💻 Compatibility may vary across different operating systems.

## Contributing

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`feature/YourFeature`).
3. 💾 Commit your changes (`git commit -m 'Add new feature'`).
4. 📤 Push to the branch (`git push origin feature/YourFeature`).
5. 🔀 Open a Pull Request.



