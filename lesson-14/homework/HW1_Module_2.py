import os
import csv

class ToDoApp():
    def __init__(self, filename = "Task.csv"):
        self.filename = filename
        self.database = self.load_tasks()
    
    def load_tasks(self):
        if not os.path.exists(self.filename):
            return {}
        database = {}
        with open(self.filename, "r", newline="") as load_file:
            reader = csv.reader(load_file)
            for line in reader:
                id, task, status = line
                database[int(id)] = {task : status}

        return database
    
    def save_tasks(self):
        with open(self.filename, "w", newline="") as write_file:
            writer = csv.writer(write_file)
            for id in self.database.keys():
                for task, status in self.database[id].items():
                    writer.writerow([id, task, status])
    
    def show_tasks(self, filter_status = None):
        for id, task_status in self.database.items():
            for task, status in task_status.items():
                if not filter_status or status == filter_status:
                    print(f"{id}. {task} ({status})")
    
    def udpate_status(self):
        self.show_tasks()
        try:
            task_id = int(input("Which task do you want to update: "))
            new_status = input("Set the status (Upcoming/Success/Ongoing): ")

            for task, status in self.database[task_id].items():
                self.database[task_id][task] = new_status
            self.save_tasks()
        except (KeyError, ValueError):
            print("\nWrong input, please try again!")
    
    def create_task(self):
        input_task = input("Enter the name of the task: ")
        input_status = input("Please, set the status: ")
        self.database[max(self.database.keys()) + 1] = {input_task : input_status}
        self.save_tasks()
    
    def delete_task(self):
        self.show_tasks()
        try:
            task_id = int(input("Please, enter the task ID you want to delete: "))
            self.database.pop(task_id)
            self.save_tasks()
        except:
            print("\nWrong input, please try again!")

    def show_menu(self):
        menu = {
            "1" : "Show all tasks",
            "2" : "Show upcoming tasks",
            "3" : "Show ongoing tasks",
            "4" : "Show successfull tasks",
            "5" : "Update task status",
            "6" : "Create task",
            "7" : "Delete task",
            "8" : "Exit"
        }

        while True:
            print("\n************* MENU *************\n")
            for id, command in menu.items():
                print(f"{id}. {command}")
            command_input = input("Choose command: ")

            match(command_input):
                case "1":
                    self.show_tasks()
                case "2":
                    self.show_tasks("Upcoming")
                case "3":
                    self.show_tasks("Ongoing")
                case "4": 
                    self.show_tasks("Success")
                case "5":
                    self.udpate_status()
                case "6":
                    self.create_task()
                case "7":
                    self.delete_task()
                case "8":
                    print("\nGood bye :)\n")
                    return
                case _:
                    print("\nWrong input, please try again!")

app = ToDoApp("Task.csv")
app.show_menu()

