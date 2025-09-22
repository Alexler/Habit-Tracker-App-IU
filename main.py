# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#the application main part (logical processing and handover between classes) will be handled here

from habit import Habit
from storage import storage_tracker
import time

####   Tests

### Create different habits ###
eat_salat = Habit("eat Salat","dont forget to eat healthy","weekly")
running = Habit("go running","training for marathon","weekly")
drink_water = Habit("drink water","drink 3L every day","daily")

### Performing the habits ###
drink_water.complete_habits()
time.sleep(1)
drink_water.complete_habits()
time.sleep(2)
running.complete_habits()
time.sleep(1)
eat_salat.complete_habits()

### Create Database ###
database = storage_tracker("Tracker DB")
database.setup_db()

### Save and load habit ###
database.save_habit(drink_water)
database.save_habit(running)
database.save_habit(eat_salat)
database_output = database.load_habit()

### OUTPUT
current_streak_water = drink_water.get_habit_streak()
current_streak_running = running.get_habit_streak()
current_streak_eat_salat = eat_salat.get_habit_streak()

print("\n\nYou have completed the habit: "+drink_water.name+". This habit was created "+str(drink_water.create_time)+". This habit was done: "+ str(len(drink_water.completed)) +" times")
print("\n\nYou have completed the habit: "+running.name+". This habit was created "+str(running.create_time)+". This habit was done: "+ str(len(running.completed)) +" times")
print("\n\nYou have completed the habit: "+eat_salat.name+". This habit was created "+str(eat_salat.create_time)+". This habit was done: "+ str(len(eat_salat.completed)) +" times")


print ("\n\n\n\nDB Return = "+str(database_output))