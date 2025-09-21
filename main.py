# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#the application main part (logical processing and handover between classes) will be handled here

from habit import Habit
from storage import storage_tracker
import time

####   Tests

### Create Database save and load habit###
database = storage_tracker("Tracker DB")
database.setup_db()
database.save_habit(Habit("TEST", "asdf", "daily"))
database.load_habit()




### Create two different habbits -> complete them and print status###

#drink_water = Habit("Water","dont forget to drink","daily")
#running = Habit("running","sport activity","weekly")
#drink_water.complete_habits()
#time.sleep(1)
#drink_water.complete_habits()
#time.sleep(2)
#running.complete_habits()
#time.sleep(1)
#running.complete_habits()
#current_streak_water = drink_water.get_habit_streak()
#current_streak_running = running.get_habit_streak()
#print (drink_water.name+" completed = "+str(drink_water.completed))
#print (drink_water.name+" streak = "+str(current_streak_water))
#print (running.name+" completed = "+str(running.completed))
#print (drink_water.name+" streak = "+str(current_streak_running))


