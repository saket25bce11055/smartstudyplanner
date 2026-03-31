#SMART STUDY PLANNER 
#PREREQUISITE:
#PROLOG INSTALLED
#LATEST PYTHON
#LIBRARIS : DATETIME



from datetime import datetime, timedelta
from pyswip import Prolog
prolog = Prolog() #if facing error for importing pyswip reinstall using pip install prolog in powershell
prolog.consult("rules.pl") #make sure to have prolog installed 
"---------------------------------------------------------------------------------------------------------------------------"
"Defining different classes which will be consulted bhy our prolog file"
class Task:
    def __init__(self, name, subject, deadline, difficulty, duration):
        self.name = name
        self.subject = subject
        self.deadline = deadline
        self.difficulty = difficulty
        self.duration = duration
        self.priority = 0
    def calculate_priority(self):
        days_left = (self.deadline - datetime.now()).days

        if list(prolog.query(f"high_priority({days_left}, {self.difficulty})")):
            self.priority = 3
        elif list(prolog.query(f"medium_priority({days_left}, {self.difficulty})")):
            self.priority = 2
        else:
            self.priority = 1
"---------------------------------------------------------------------------------------------------------------------------"
#user inputs (starting time is default 16:00 no  user input for that)
def input_tasks():
    tasks = []
    n = int(input("Enter number of tasks: "))

    for i in range(n):
        print("\nTask" ,{i+1})
        name = input("Task name: ")
        subject = input("Subject: ")
        deadline = datetime.strptime(
            input("Deadline (DD-MM-YYYY): "), "%d-%m-%Y"
        )
        difficulty = int(input("Difficulty (1-5): "))
        duration = float(input("Duration (hours): "))
        print("-----------------------------------------------------------------")

        task = Task(name, subject, deadline, difficulty, duration)
        task.calculate_priority()
        tasks.append(task)

    return tasks
"---------------------------------------------------------------------------------------------------------------------------"
#scheduling taskss
def schedule_tasks(tasks, hours1):
    tasks.sort(key=lambda x: x.priority, reverse=True)
    schedule = []
    current_hours = 0
    for task in tasks:
        if current_hours + task.duration <= hours1:
            schedule.append(task)
            current_hours += task.duration
        else:
            # Split task if needed
            remaining = hours1 - current_hours
            if remaining > 0:
                part = Task(task.name + " (Part)", task.subject, task.deadline, task.difficulty, remaining)
                part.calculate_priority()
                schedule.append(part)
                break
    return schedule
"--------------------------------------------------------------------------------------------------------------------------"
#had errors displaying schedule , took insights from online tutorial and codes mentioned in project report
def display_schedule(schedule):
    print("\n --------------------------Today's Study Plan:------------------------------------\n")

    start_time = datetime.now().replace(hour=16, minute=0, second=0, microsecond=0)

    for task in schedule:
        end_time = start_time + timedelta(hours=task.duration)

        print(f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')} → {task.subject} ({task.name})")

        start_time = end_time

"---------------------------------------------------------------------------------------------------------------------------"
def main():
    print("SMART STUDY PLANNER \n")
    print("---------------------------------------------------------------------------------------------------------------------")

    tasks = input_tasks()
    hours_per_day = float(input("\nEnter available study hours today: "))

    schedule = schedule_tasks(tasks, hours_per_day)
    display_schedule(schedule)
if __name__ == "__main__":
    main()
    