# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#the coordination / organisation of habits between the main and habit class will be handled here


class Tracker:
    def __init__(self, db_name):
        self.db_name = db_name

        self.habits = []
        def habits_from_db(self):
            self.habits