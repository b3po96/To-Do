'''
Python To-Do
A simple to-do list program using text files to hold tasks
Authored by: Bryce Buchanan
'''

#TODO 1. Convert to class
#TODO 2. Detemine and implement best data structure
#TODO 3. File I/O
#TODO 4. GUI

class ToDoItem:
    
    def __init__(self, task):
        self.task = task
        self.next = None
        
    def get(self):
        return self.task
    
class ToDoModule:
    
    def __init__(self, toDo, completedTasks, head = None):
        self.toDo = toDo
        self.completedTasks = completedTasks
        self.head = head
    
    def append(self):
        newTask = input('Type your task here: ')
        toDoList.append(newTask)
        
    def completeTask(self):
        while (1):
            try:
                completed = int(input('Which task number would you like to complete? (Enter index): '))
                break
            except ValueError:
                print('Not a valid task number')
        completedTasks.append(toDoList[completed - 1])
        del toDoList[completed - 1]
        
    def printTasks(self):
        for task in toDoList:
            index = "{}".format(toDoList.index(task) + 1)
            print(index + '. ' + task.get(), end = '\n')
        print('\n')
        
    def printCompleted(self):
        for task in completedTasks:
            index = "{}".format(completedTasks.index(task) + 1)
            print(index + '. ' + task.get(), end = '\n')
        print('\n')

toDoList = ['Add a task!']
completedTasks = ['First task completed!']

"""
def listMenu():
    response = input('''Would you like to ...
          Start a (N)ew to-do list?
          (O)pen an existing to-do list?
          (D)elete a to-do list?
    # Create new to-do list
    if (response == 'N' or response == 'n'):
        toDoList.name = input('Please name your file:')
        with open(newList, 'x', encoding = 'utf-8') as f: {}
"""
 
def taskMenu(list, completed):
    response = ''
    response = input('''Would you like to...
          (A)dd a task?
          (E)dit a task?
          (C)omplete a task?
          (L)ist current tasks?
          (R)eview completed tasks?
          (Q)uit? ''' + '\n')
    
    # Adds a task to the to-do list
    if (response == 'A' or response == 'a'):
        list.add()
       
    # Removes a task from the to-do list and adds it to the completed list
    elif (response == 'C' or response == 'c'):
        list.completeTask()
                
    # Lists all tasks in to-do list
    elif (response == 'L' or response == 'l'):
        list.printTasks()  
        
    # Lists all tasks in completed list
    elif (response == 'R' or response == 'r'):
        completed.printCompleted()        

    # Confirms exiting of the program
    elif (response == 'Q' or response == 'q'):
        exit = input('Are you sure you would like to exit? (Y/N)' + '\n')
        if (exit == 'Y' or exit == 'y'):
            raise SystemExit
        elif (exit == 'N' or exit == 'n'): {}

def main():
    print("Welcome to Python To-Do!")
   # listMenu()
    while(1):
        taskMenu(toDoList, completedTasks)       
    
if __name__ == '__main__': main()