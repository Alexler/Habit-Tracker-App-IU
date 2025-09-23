# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#the application main part (logical processing and handover between classes) will be handled here

from habit import Habit
from storage import storage_tracker
from tracker import Tracker
import time

####   Tests

### Create different habits ###
#eat_salat = Habit("eat Salat","dont forget to eat healthy","weekly")
#running = Habit("go running","training for marathon","weekly")
#drink_water = Habit("drink water","drink 3L every day","daily")

Tracker_db = Tracker("Tracker DB")
Tracker_db.storage.setup_db()
Tracker_db.save_habits_to_db("eat Salat","dont forget to eat healthy","weekly")
Tracker_db.complete_habits("eat Salat")
