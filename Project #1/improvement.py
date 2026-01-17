# Nice to imrove next time

# 1) Use a dict for menu validation
# get is a method you can use on dictionaries to safely read a value by key.
# It does not return a ValueError.
command_map = {
    "1":"add", "add" : "add",
    "2":"remove", "remove":"remove",
    "3":"show", "show":"show",
    "4":"search", "search":"search",
    "5":"quit", "quit":"quit"
}
cmd = command_map.get(choice) 
if cmd is None: 
    print("Invalid choice")
    continue



# 2) Make a resuable "yes/no input" function
# (prompt : str) means the parameter prompt should be a string
# -> bool means the function returns a boolean (True or False)
def ask_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("yes","y"):
            return True
        if ans in ("no", "n"):
            return False
        print("Type yes/no.")

while True:
    if ask_yes_no("Go back home? yes/no: "):
        continue
    else:
        break


# 3) Small style habits
# Always strip().lower() inputs that are commands.
# Prefer if not task: over if tasks == {}:
# Prefer if task_name in tasks: over if task_name in tasks.keys():
# Write a description for each function.