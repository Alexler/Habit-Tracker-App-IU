# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774
from enum import nonmember


#Scope of this part:
#the coordination / organisation of habits between the main and habit class will be handled here

from habit import Habit
from storage import storage_tracker

class Tracker:
    def __init__(self, db_name):
        self.storage = storage_tracker(db_name)
        self.habits = []
        self.load_habits_from_db()
        self.check_for_predef_habits()

    def check_for_predef_habits(self):
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
        self.habits = self.storage.load_habit()

    def save_habits_to_db(self, name, description, recurrence):
        new_habits = Habit(name, description, recurrence)
        self.habits.append(new_habits)
        self.storage.save_habit(new_habits)

    def complete_habits(self, habit_name):

        habits_complete = None

        for n in self.habits:
            if n.name == habit_name:
                habits_complete = n
                break

        if habits_complete:
            habits_complete.complete_habits()
            self.storage.save_habit(habits_complete)