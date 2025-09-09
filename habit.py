# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#This is the Habit class that will be trackable by the user

import datetime, time

class Habit:
    def __init__(self, name: str, description: str, recurrence: str):
        # initialization of a new habit
        self.name = name
        self.description = description
        self.recurrence = recurrence
        self.create_time = datetime.datetime.now()
        self.complete_time = []

    def start_habits(self):
        #a habit will be setup here
        self.create_time = datetime.datetime.now()
        print("Habit " + self.name + " started")
        print("Time = " + str(self.create_time))

    def complete_habits(self):
        #a habit will be marked as complete here
        self.complete_time.append(datetime.datetime.now())
        print("Habit "+self.name+" marked as complete")
        print("Time = " + str(self.complete_time[-1]))

#Tests
#drink_water = Habit("Water","dont forget to drink","Wiederholung")
#drink_water.start_habits()
#time.sleep(2)
#drink_water.complete_habits()

