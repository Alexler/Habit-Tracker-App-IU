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
        self.load_habits_from_db

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


