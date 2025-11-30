# Habit Tracker App
### A command-line tool for tracking daily and weekly habits
###### Author: Alexander Lerch (IU14130774)

## 1. Installation
#### (Preconditions: Python 3.8 or higher)

    1.1 Download the project files to your local folder.
    1.2 Install Dependencies: Open your terminal in the project folder and run: >>pip install click pytest<<

## 2. How to Run
#### These are the commands to demonstrate the full functionality of the app. You can copy and paste these directly into your terminal.

    * Step 1: Initialization // Run the app for the firest time. It will automatically create the database and 5 predefined habits. 
             >>python main.py list<<

    * Step 2: Create a Habit //  Add a custom daily habit.
             >>python main.py add "Learn Python" --descripton "Study for 30 mins" --recurrence daily<<

    * Step 3: Complete a Habit //  Mark the habit as done for today
             >>python main.py complete "Learn Python"<<

    * Step 4: Analytics //  View your streaks and statistics.
             >>python main.py list<<                          -> View all habits and their current streaks<<
             >>python main.py analyze all<<                   -> Find the longest streak among ALL habits<<
             >>python main.py analyze habit "Learn Python"<<  -> View longest streak for a SPECIFIC habit<<
             >>python main.py analyze period weekly<<         -> List only WEEKLY habits<<

## 3. Running Tests
#### To verify the logic (especially streak calculations and broken streaks), run the test suite.
            >>pytest<<

## 4. Key Features
    * Flexible Recurrence:
        Support both "daily" and "weekly" habits.

    * Streak Tracking:
        Algorithms correctly identify broken chains (gaps > 1 day for daily, > 7 days for weekly). 

    * Predefined Fixtures:
         Comes with 5 built-in habits (e.g., "Drink Water", "Workout") to get you started immediately.