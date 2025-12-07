# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

"""
Storage Module
This module manages the SQLite database connection, table creation, and
all Read/Write operations for Habit objects and their logs.
"""

import datetime
import sqlite3
from habit import Habit

class storage_tracker:
    """
    Database Manager class.
    Handles low-level SQL queries to save habit data and completion history.
    """

    def __init__(self, db_name):
        """
        Initializes the database connection.
        :param db_name: The filename of the SQLite database.
        """

        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        """
        Creates the necessary database tables ('habits' and 'complete_habits')
        if they do not already exist.
        """

        self.cursor.execute("CREATE TABLE IF NOT EXISTS habits(name TEXT, description TEXT, recurrence TEXT, create_time TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS complete_habits (name TEXT, habit_complete_time TEXT)")
        self.conn.commit()

    def save_habit(self, habit):
        """
        Saves a single Habit object and its entire completion history to the database.
        Note: This performs an 'upsert' operation (Insert or Replace) to update
        existing records.
        :param habit: The Habit object to be saved.
        """

        self.cursor.execute("DELETE FROM complete_habits WHERE name = ?", (habit.name,))
        self.cursor.execute("INSERT OR REPLACE INTO habits          (name, description, recurrence, create_time)    VALUES (?,?,?,?)", (habit.name, habit.description, habit.recurrence, str(habit.create_time)))

        for n in habit.completed:
            self.cursor.execute("INSERT OR REPLACE INTO complete_habits (name, habit_complete_time)                     VALUES (?, ?)",(habit.name, str(n)))

        self.conn.commit()

    def get_completed_habits(self, habit_name):
        """
        Retrieves the list of completion timestamps for a specific habit.
        :param habit_name: The name of the habit to look up.
        :return: A list of datetime objects.
        """

        self.cursor.execute("SELECT habit_complete_time FROM complete_habits WHERE name = ?", (habit_name,))

        db_data = self.cursor.fetchall()

        db_data_time = []
        for n in db_data:
            time_object = datetime.datetime.fromisoformat(n[0])
            db_data_time.append(time_object)

        return db_data_time

    def load_habit(self):
        """
        Loads ALL habits from the database and reconstructs them into Habit objects.
        :return: A list of fully populated Habit objects.
        """

        all_habits = []

        self.cursor.execute("SELECT * FROM habits")
        habit_input = self.cursor.fetchall()

        for n in habit_input:
            name, description, recurrence, create_time = n

            habit = Habit(name, description, recurrence)
            habit.create_time = datetime.datetime.fromisoformat(create_time)

            habit.completed = self.get_completed_habits(name)

            all_habits.append(habit)


        return all_habits