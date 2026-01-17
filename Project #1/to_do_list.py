# Simple To-do List:
# 1) Add tasks
# 2) Remove tasks
# 3) Show status
# 4) Search particular task
# 5) Quit program

# Initial Plan
# Use while loop -> ask the user what he wants to do until he quits.
# Use a dictionary to keep track of a couple of information for the task: name, status, priority.
# Use try/except that I learnt yesterday.

options = ["add", "remove", "show", "search", "quit"] # the user is only allowed to input one of these.
tasks = {}

def show_menu():
    print(""" You have five options:
        1. add
        2. remove
        3. show
        4. search
        5. quit
        """)

def add_task(name, status, priority):
    tasks[name] = {"status" : status, "Priority" : priority}

def remove_task(name):
    del tasks[name]

def show_tasks():
    for index,value in enumerate(tasks.keys()):
        print(f"Your current tasks: {index+1} : {value}")

status = ["done", "undone"]
priority = ["high", "medium", "low"]

while True:
    show_menu()
    try: 
        choice = input("What do you want to do? ")
    except ValueError:
        print("You're only allowed to type strings.")

    if choice not in options:
        print("Please type one of the five options.")
    
    if choice == "quit":
        break

    elif choice == "add":
        task_name = input("What is the name of the task? ")
        task_status = input("Is it done/undone? ")
        if task_status not in status:
            print("Please type: done/undone ")
            task_status = input("Is it done/undone? ")
            
        task_priority = input("How important is that? High/Medium/Low: ")
        if task_priority not in priority:
            print("Please type: high/medium/low ")
            task_priority = input("How important is that? High/Medium/Low: ")

        add_task(task_name,task_status,task_priority)

    elif choice == "remove":
        task_name = input("Which task would you like to remove? ").strip()
        removed_task = tasks.pop(task_name, None) # without default -> key error, with default -> returns default
        if removed_task is None:
            print("It is not an existing task.")
        else:
            print(f"Removed : {task_name}")
            
    elif choice == "show":
        show_tasks()
    elif choice == "search":
        task_name = input("Which task would you like to check existance? ")
        if task_name in tasks.keys():
            print("The task exists.")
        else:
            print("The task does not exist.")
            additional_task = input("Would you like to add the task? yes/no : ")
            if additional_task == "yes":
                task_status = input("Is it done/undone? ")
                task_priority = input("How important is that? High/Medium/Low: ")
                add_task(task_name,task_status,task_priority)   
            else:
                continue

