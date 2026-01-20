# Project #3 - Create a simple expense manager
# Learning Outcomes :
# 1) Understand what is a JSON file
# 2) How to read/write a JSON file
# 3) Create a program using a JSON file

# Initial plan :
# 1) Add a new expense, remove current expense, summarize the total list of espenses and total costs.
# 2) Save everything to a JSON file and load the file when the program starts.
# 3) Design :
# - store expenses as a list of dictionaries: id,date,name,category,cost

import json
import re
from datetime import datetime
PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$") # exactly YYYY-MM-DD

def read_date(prompt="Enter date (YYYY-MM-DD): ") -> str:
    while True:
        date = input(prompt).strip()

        # 1) format check
        if not PATTERN.match(date):
            print("Invalid format. Use exactly YYYY-MM-DD (e.g., 2026-10-20). ")
            continue

        # 2) real date check (e.g. 2026-13-40)
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("That date doesn't exsist. Try again. ")

def load_expenses(filename):
    # fileName -> list
    try:
        with open(filename,"r") as f:
            return json.load(f) # returns a list
    except FileNotFoundError:
        return [] # create a inital file if the file does not exist.
    
def save_expenses(filename, expenses):
    with open(filename,"w") as f:
        json.dump(expenses,f,indent=2)

def add_expense(expenses):
    expenses.append(item)
    save_expenses("test.json", expenses)

def show_menu():
    # show a menu of the program : add, remove, summary, quit
    print("""
    1) Add
    2) Remove
    3) Summary
    4) Quit
    """)

def show_summary(food,clothes,hobby,general,total):
    # int -> None
    print(f"""
    Food Expense : ${food}
    Clothes Expense : ${clothes}
    Hobby Expense : ${hobby}
    General Expense : ${general}
    Total Expense : ${total}
""")

menu_options = [1,2,3,4] # Add - 1, Remove - 2, Summary - 3, Quit - 4

category_options = ["food", "clothes", "hobby", "general"]

test_expenses = load_expenses("test.json")

while True:
    item = {}
    show_menu()
    try:
        choice = int(input("Choose an option: ").strip())
    except ValueError:
        print("Only integers are allowed. ")
        continue

    # range 1~4
    if choice not in menu_options:
        print("Please type 1~4. ")
        continue


    if choice == 1:
        # ask date,name,category,cost and add them to JSON
        date = read_date()
        name = input("What is the name of purchase? ").strip().lower()
        while True:
            category = input("What kind of category is it? ").strip().lower()
            if category not in category_options:
                print("That is not in the category options.")
            else:
                break

        while True:
            try:
                cost = int(input("How much does it cost? "))
            except ValueError:
                print("Only integers allowed.")
                continue
            
            if type(cost) == int:
                break

        # idea1) id = last id - 1? / first id = 1
        # idea2) keep two json files : 1) whole data 2) not deleted data
        # idea3) change status to False in terms of deleted data, and show only data status = True 
        item.update({"id":len(test_expenses)+1, "date":date, "name":name, "category":category, "cost":cost, "status":True})
        add_expense(test_expenses)
        

    elif choice == 2:
        # ask name and remove the corresponding item
        # what if the item doesnt exist?
        remove_item = input("Which item do you want to remove? ").strip().lower()
        item_found = False
        for item in test_expenses:
            if remove_item == item["name"]:
                item_found = True
                test_expenses.remove(item)
                print("Item Deleted.")
                break # terminate the program once you found the item. try to learn any() and next() next time!
        if item_found == False:
            print("The item does not exist. ")

        save_expenses("test.json",test_expenses)
        
        
    elif choice == 3:
        # summary - show whole items / load?
        food_expense = 0
        clothes_expense = 0
        hobby_expense = 0
        general_expense = 0
        total_expense = 0
        for item in test_expenses:
            total_expense += item["cost"]
            if item["category"] == "food":
                food_expense += item["cost"]
            elif item["category"] == "clothes":
                clothes_expense += item["cost"]
            elif item["category"] == "hobby":
                hobby_expense += item["cost"]
            elif item["category"] == "general":
                general_expense += item["cost"]

        show_summary(food_expense,clothes_expense,hobby_expense,general_expense,total_expense)    


    elif choice == 4:
        print("Quit Expense Manager Prgrogram.")
        break
    

