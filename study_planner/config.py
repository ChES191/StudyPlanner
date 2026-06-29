from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent 
TASKS_FILE = BASE_DIR / "tasks.json"

#study_planner/config.py -> C:Users/Maxim/StudyPlanner/study_planner/config.py 
# -> .parent -> C:Users/Maxim/StudyPlanner/study_planner/ -> .parent -> C:Users/Maxim/StudyPlanner/

#C:Users/Maxim/StudyPlanner/tasks.json


PRIORITIES = ("Низкий", "Средний", "Высокий")
FILTERS = ("Все", "Невыполненные", "Выполненные")

