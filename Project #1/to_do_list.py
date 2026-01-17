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

options = [["add","1"], ["remove","2"], ["show","3"], ["search","4"], ["quit","5"]] # the user is only allowed to input one of these.
status = ["done", "undone"]
priority = ["high", "medium", "low"] 
tasks = {}
exit_all = False # get out of while loop twice

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
    if tasks == {}: # always be concerned with empty-case.
        print("There is no current task.")
    else: 
        print("Your current tasks:")
        for index,value in enumerate(tasks.keys()):
            print(f"{index+1} : {value}")

while True:
    valid = False
    show_menu()
    try: 
        choice = input("Select among five options/numbers: ").strip().lower()
    except ValueError:
        print("You're only allowed to type strings.")

    for option in options: # searching item in list
        if choice in option:
            valid = True
            break

    if valid == False:
        print("Please type one of the five options/numbers.")
    
    if choice == "quit" or choice == "5":
        print("Quit the program.")
        break

    elif choice == "add" or choice == "1":
        task_name = input("What is the name of the task? ")
        task_status = input("Is it done/undone? ")
        task_priority = input("How important is that? High/Medium/Low: ")

        add_task(task_name,task_status,task_priority)

    elif choice == "remove" or choice == "2":
        task_name = input("Which task would you like to remove? ").strip()
        removed_task = tasks.pop(task_name, None) # without default -> key error, with default -> returns default
        if removed_task is None:
            print("It is not an existing task.")
        else:
            print(f"Removed : {task_name}")
            
    elif choice == "show" or choice == "3":
        show_tasks()
        answer = input("Would you like to go back Home? yes/no: ")
        while True:
            if answer =="yes":
                break
            elif answer =="no":
                print("Quit the program.")
                exit_all = True
                break
            else:
                print("You must type valid answer yes/no.")
                answer = input("Would you like to go back Home? yes/no: ")
        if exit_all == True:
            break

    elif choice == "search" or choice == "4":
        task_name = input("Which task would you like to check existance? ")
        if task_name in tasks.keys():
            print("The task exists.")
        else:
            print("The task does not exist.")
            additional_task = input("Would you like to add the task? yes/no: ")
            while True:
                if additional_task == "yes":
                    task_status = input("Is it done/undone? ")
                    task_priority = input("How important is that? High/Medium/Low: ")
                    add_task(task_name,task_status,task_priority)
                    break 
                elif additional_task == "no":
                    break
                else:
                    print("You must type valid answer yes/no. ")
                    additional_task = input("Would you like to add the task? yes/no: ")


