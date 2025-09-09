# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#This is the Habit class that will be trackable by the user

class Habit:
    def __init__(self, name: str, description: str, recurrence: str):
        # initialization of a new habit object

        self.name = name
        self.description = description
        self.recurrence = recurrence
        self.create_date = datetime.datetime.now()
        self.complete.time = []

    def complete_habits(self):
        self.complete.time.append(datetime.datetime.now())
        print("Habit "+self.name+" complete")
        print(self.complete.time)

Habit.complete_habits()