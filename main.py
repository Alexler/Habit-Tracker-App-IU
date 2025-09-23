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

Tracker_db = Tracker("Tracker DB")
Tracker_db.storage.setup_db()
Tracker_db.save_habits_to_db("eat Salat","dont forget to eat healthy","weekly")
Tracker_db.complete_habits("eat_salat")
Tracker_db.save_habits_to_db("running","train for marathon","daily")
Tracker_db.complete_habits("running")
time.sleep(1)
Tracker_db.complete_habits("running")

habits = Tracker_db.load_habits_from_db()
for n in Tracker_db.habits:
    print(n.name,n.description, n.recurrence, n.create_time, n.completed)