# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#the application main part (logical processing and handover between classes) will be handled here

from habit import Habit
import datetime





#Tests
drink_water = Habit("Water","dont forget to drink","daily")
drink_water.complete_habits()
current_streak = drink_water.get_habit_streak()
print (drink_water.name)




