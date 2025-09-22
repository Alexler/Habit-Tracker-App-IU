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
        self.cursor.execute("INSERT OR REPLACE INTO habits          (name, description, recurrence, create_time)    VALUES (?,?,?,?)", (habit.name, habit.description, habit.recurrence, habit.create_time))
        #self.cursor.execute("INSERT OR REPLACE INTO complete_habits (name, habit_complete_time)                     VALUES (?, ?)", (habit.name, str(habit.completed))

        for n in habit.completed:
            self.cursor.execute("INSERT OR REPLACE INTO complete_habits (name, habit_complete_time)                     VALUES (?, ?)",(habit.name, n))

        self.conn.commit()

    def get_completed_habits(self, habit_name):
        self.cursor.execute("SELECT habit_complete_time FROM complete_habits WHERE name = ?", (habit_name,))

        db_data = self.cursor.fetchall()

        db_data_time = []
        for n in db_data:
            time_object = datetime.datetime.fromisoformat(n[0])
            db_data_time.append(time_object)

        return db_data_time

    def load_habit(self):

        all_habits = []

        self.cursor.execute("SELECT * FROM habits")
        habit_input = self.cursor.fetchall()

        for n in habit_input:
            name, description, recurrence, create_time = n

            habit = Habit(name, description, recurrence)
            habit.create_time = datetime.datetime.fromisoformat(create_time)

            all_habits.append(habit)


        return all_habits
