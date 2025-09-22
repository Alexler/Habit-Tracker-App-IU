# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#This is the Habit class that will save and load habits

import datetime
import sqlite3
from habit import Habit

class storage_tracker:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def setup_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS habits(name TEXT, description TEXT, recurrence TEXT, create_time TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS complete_habits (name TEXT, habit_complete_time TEXT)")

        self.conn.commit()

    def save_habit(self, habit):
        habit_to_storage = (habit.name, habit.description, habit.recurrence, habit.create_time)
        habit_complete_time_to_storage = (habit.name, str(habit.completed))
        self.cursor.execute("INSERT OR REPLACE INTO habits          (name, description, recurrence, create_time)    VALUES (?,?,?,?)", habit_to_storage)
        self.cursor.execute("INSERT OR REPLACE INTO complete_habits (name, habit_complete_time)                     VALUES (?, ?)", habit_complete_time_to_storage)
        self.conn.commit()

    def load_habit(self):
        self.cursor.execute("SELECT * FROM habits")
        habit_input = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM complete_habits")
        complete_habit_input = self.cursor.fetchall()

        return habit_input, complete_habit_input
