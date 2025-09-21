# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#This is the Habit class that will save and load habits

import sqlite3
from habit import Habit

class storage_tracker:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def setup_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS habits(title TEXT, test TEXT, score TEXT)")
        self.conn.commit()
        print("Database table set up.")

    def save_habit(self, habit):
        self.cursor.execute("INSERT OR REPLACE INTO habits() VALUES (?,?,?)")

        print("habit saved.")

#    def load_habit(self):
