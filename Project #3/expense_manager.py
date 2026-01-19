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

expenses = [
    {
    "id" : "1", 
    "date" : "2026-01-01",
    "name" : "tuition fee",
    "category" : "education",
    "cost" : "300000"
    }
]

import json

def load_expenses(filename):
    try:
        with open(filename,"r") as f:
            return json.load(f) # returns a list
    except FileNotFoundError:
        return []
    
def save_expenses(filename, expenses):
    with open(filename,"w") as f:
        json.dump(expenses,f)


def show_menu():
    # show a menu of the program : add, remove, summary, quit
    print("""
    1) Add
    2) Remove
    3) Summary
    4) Quit
    """)

