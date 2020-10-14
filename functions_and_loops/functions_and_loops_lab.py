# Print a list of uncompleted tasks

# Print a list of completed tasks

# Print a list of all task descriptions

# Print a list of tasks where time_taken is at least a given time

# Print any task with a given description

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# Print a list of uncompleted tasks & also used for completed tasks depending on arguement passed

def task_status(list, true_or_false): #Add false as variable name is_false
    task_list = []
    for task in list:
        if task["completed"] == true_or_false: #change False to is_false
            task_list.append(task["description"])
    return task_list

print("Uncomplete task list: " , task_status(tasks, False))
print("Comleted task list: " , task_status(tasks, True))

# Print a list of all task descriptions

def task_descriptions(list):
    task_descriptions_list = []
    for task in list:
        task_descriptions_list.append(task["description"])
    return task_descriptions_list

print("Full task list: " , task_descriptions(tasks))

# Print a list of tasks where time_taken is at least a given time

def time_of_task(list, given_time):
    list_times = []
    for task in list:
        if task["time_taken"] >= given_time:
            list_times.append(task["description"])

    return list_times

print(time_of_task(tasks, 20))

# Print any task with a given description

def check_description(list, given_task):
    for task in list:
        if given_task == task["description"]:
            return task["description"]
             

print(check_description(tasks, "Make Dinner"))


# tasks = [
#     { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
#     { "description": "Clean Windows", "completed": False, "time_taken": 15 },
#     { "description": "Make Dinner", "completed": True, "time_taken": 30 },
#     { "description": "Feed Cat", "completed": False, "time_taken": 5 },
#     { "description": "Walk Dog", "completed": True, "time_taken": 60 },
# ]

#Given a description update that task to mark it as complete.

#Add a task to the list

# function with 2 para task

def mark_as_completed(list, item_description):
    for task in list:
        if task["description"] == item_description:
            task["completed"] = True

mark_as_completed(tasks, "Wash Dishes")
print(tasks)

def add_task(list, description, completed, time_taken):
    list.append([{"description": description , "completed": completed , "time_taken": time_taken}])

add_task(tasks, "Hoover", True, 10)
print(tasks)
