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
        #a habit will be setup/start here
        self.create_time = datetime.datetime.now()
        print("Habit " + self.name + " started")
#        print("Time = " + str(self.create_time))

    def complete_habits(self):
        #a habit will be marked as completed here
        self.complete_time.append(datetime.datetime.now())
        print("Habit "+self.name+" marked as complete")
#        print("Time = " + str(self.complete_time[-1]))

    def get_habit_streak_(self):
        #calculates the streak based on the habit's recurrence
        today = datetime.datetime.now().date()
        habit_date = self.complete_time[0].date()
        if habit_date == today:
            print("streak")
        else:
            print("no streak")
            print("habit date="+str(habit_date))
            print("today="+str(today))



#Tests
drink_water = Habit("Water","dont forget to drink","Wiederholung")
drink_water.start_habits()
time.sleep(2)
drink_water.complete_habits()
drink_water.get_habit_streak_()
