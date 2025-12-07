# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774
from enum import nonmember



"""
Tracker Controller Module
This module acts as the 'Controller' in the application architecture.
It coordinates the flow of data between the User Interface (CLI), the
Logic Layer (Habit objects), and the Persistence Layer (Storage).
"""

from habit import Habit
from storage import storage_tracker

class Tracker:
    """
    The main controller class.
    Manages the list of active habits and handles high-level operations
    like adding new habits, marking them as complete, and syncing with the database.
    """

    def __init__(self, db_name):
        """
        Initializes the Tracker controller.
        :param db_name: The name of the database file to connect to.
        """

        self.storage = storage_tracker(db_name)
        self.habits = []
        self.load_habits_from_db()
        self.check_for_predef_habits()

    def check_for_predef_habits(self):
        """
        Checks if the database is empty (first-time run).
        If no habits exist, it creates 5 default habits to help the user get started.
        """

        if not self.habits:
            print("First run detected. Adding predefined habits...")

            predefined_habits = [
                ("Drink Water", "Drink at least 2L of water", "daily"),
                ("Read a Book", "Read 10 pages of a book", "daily"),
                ("Workout", "Complete a 30-minute workout session", "daily"),
                ("Weekly Review", "Review the past week and plan the next", "weekly"),
                ("Clean the Apartment", "Do a full clean of the apartment", "weekly")
            ]

            for habit_data in predefined_habits:
                name, description, recurrence = habit_data
                self.save_habits_to_db(name, description, recurrence)
            self.load_habits_from_db()


    def load_habits_from_db(self):
        """
        Refreshes the memory list of habits by reloading them from the storage.
        """
        self.habits = self.storage.load_habit()

    def save_habits_to_db(self, name, description, recurrence):
        """
        Creates a new Habit object and saves it to the database.
        :param name: Name of the new habit.
        :param description: Description of the habit.
        :param recurrence: 'daily' or 'weekly'.
        """

        new_habits = Habit(name, description, recurrence)
        self.habits.append(new_habits)
        self.storage.save_habit(new_habits)

    def complete_habits(self, habit_name):
        """
        Finds a specific habit by name and marks it as complete.
        Updates the storage to persist the completion event.
        :param habit_name: The name of the habit to complete.
        """

        habits_complete = None

        for n in self.habits:
            if n.name == habit_name:
                habits_complete = n
                break

        if habits_complete:
            habits_complete.complete_habits()
            self.storage.save_habit(habits_complete)