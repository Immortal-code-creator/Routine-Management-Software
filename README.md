# ⏰ Routine Management Software (Python)

A command-line based **Routine Management Software** written in Python that helps individuals manage their daily routines by setting scheduled alarms. Each routine triggers an alarm sound at the specified time and continues to ring until the user manually stops it.

---

## 📖 Description

The Routine Management Software is a Python program designed to help users follow a structured daily schedule.  
The user can assign **7 predefined routines**, each with a specific time entered in **12-hour AM/PM format**.

The software uses the system clock to trigger alarms daily. Once an alarm starts, it will continue playing until the user presses **Enter**, ensuring the routine is not missed.

The program runs continuously and checks pending tasks every second.

---

## ✨ Features

- Supports **7 daily routines**
- Allows **7 alarms**, one for each routine
- Accepts user-friendly **12-hour time format (AM/PM)**
- Automatically converts time to **24-hour format internally**
- Alarm rings continuously until stopped by user
- Uses system time for accurate scheduling
- Simple and interactive command-line interface

---

## 🗂 Supported Routines

1. Wake-Up / Good Morning  
2. Do Exercises  
3. Time For Breakfast  
4. Drink Water  
5. Time For Lunch  
6. Time For Dinner  
7. Sleep / Good Night  

---

## 🧠 Concepts Used

- `datetime` module for time parsing and formatting  
- `time` module for delays  
- `schedule` module for task scheduling  
- `pygame` module for playing alarm sounds  
- Functions and loops  
- Conditional statements  
- User input handling  

---

## 🛠 Dependencies

- **Python 3.10 or later**
- Any operating system that supports Python:
  - Windows
  - Linux
  - macOS

### External Modules Required
- `schedule`
- `pygame`

### Install dependencies using:
bash
pip install schedule pygame

## Audio Files Required

Ensure the following audio files are available in the same directory as the Python script:

.brahma-rooster-89888.mp3

.exercise_time.wav

.Breakfast.mp3

.it's-time-to-drink-water-made-with-Voicemod.mp3

.time-for-lunch-64-kbps.mp3

.dinner.mp3

.its-time-to-go-to-bed_wUZtynX.mp3

## ⚙️ How the Software Works

.The user enters their name.

.The user selects a routine number (1–7).

.The user enters the time in Hour:Minute AM/PM format.

.The routine is saved and scheduled.

.After all 7 routines are set, the program starts running.

.At the scheduled time:

.The alarm sound plays continuously.

.The user presses Enter to stop the alarm.

## 📥 Installation

Clone the repository:

### git clone https://github.com/Immortal-code-creator/routine-management-software.git


Navigate to the project directory.

Ensure Python is installed on your system.

## ▶️ Executing the Program

.Open a terminal or command prompt.

.Navigate to the project folder.

.Run the program:

-python routine_management.py

## ❓ Help

If the program does not run:

.Make sure Python 3.10 or later is installed.

.Verify Python installation:

.python --version


.Ensure all required audio files are present.

Make sure you are running the program from the correct directory.

## 👨‍💻 Author

Aeshan Chowdhury

### GitHub: https://github.com/Immortal-code-creator
```bash
pip install schedule pygame
