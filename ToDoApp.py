import json

# file name
file = "tasks.json"


# load tasks
def load_tasks():

    try:
        f = open(file, "r")
        tasks = json.load(f)
        f.close()

    except:
        tasks = []

    return tasks


# save tasks
def save_tasks(tasks):

    f = open(file, "w")
    json.dump(tasks, f)
    f.close()


# add task
def add_task(tasks):

    task_name = input("Enter task name: ")

    task = {
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task Added Successfully")


# view tasks
def view_tasks(tasks):

    if len(tasks) == 0:
        print("No Tasks Available")

    else:

        print("\nTask List\n")

        i = 1

        for task in tasks:

            print(i, ".", task["name"], "-", task["status"])

            i = i + 1


# delete task
def delete_task(tasks):

    view_tasks(tasks)

    num = int(input("Enter task number to delete: "))

    if num >= 1 and num <= len(tasks):

        tasks.pop(num - 1)

        save_tasks(tasks)

        print("Task Deleted")

    else:
        print("Invalid Number")


# mark task done
def mark_done(tasks):

    view_tasks(tasks)

    num = int(input("Enter task number: "))

    if num >= 1 and num <= len(tasks):

        tasks[num - 1]["status"] = "Done"

        save_tasks(tasks)

        print("Task Marked Done")

    else:
        print("Invalid Number")


# main program
tasks = load_tasks()

while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task(tasks)

    elif choice == "2":

        view_tasks(tasks)

    elif choice == "3":

        delete_task(tasks)

    elif choice == "4":

        mark_done(tasks)

    elif choice == "5":

        print("Program Ended")
        break

    else:

        print("Wrong Choice")