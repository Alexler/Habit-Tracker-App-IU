# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#this application part is for development purpose, for testing of single function and the whole app

from habit import Habit
from storage import storage_tracker
from tracker import Tracker
from analytics import get_all_habits, get_habits_by_periodicity, get_longest_streak_all, get_longest_streak_for_habit
import time

####   Tests

### Create different habits ###

Tracker_db = Tracker("Tracker DB")
Tracker_db.storage.setup_db()
Tracker_db.save_habits_to_db("habit 1","first habit","daily")
Tracker_db.complete_habits("habit 1")
Tracker_db.save_habits_to_db("habit 2","2nd habit","weekly")

Tracker_db.complete_habits("habit 1")
time.sleep(1)
Tracker_db.complete_habits("habit 2")

habits = Tracker_db.load_habits_from_db()

print(habits)

all_habits = get_all_habits(Tracker_db.habits)
daily_habits = get_habits_by_periodicity(Tracker_db.habits, "daily")
print(all_habits)
print(daily_habits)

longest_streak = get_longest_streak_all(Tracker_db.habits)
print(longest_streak)

longest_streak_specific_habit = get_longest_streak_for_habit(Tracker_db.habits,"habit 1")
print(longest_streak_specific_habit)