from To_Do import *

def taskMenu(toDo):
		response = ''
		response = input('''Would you like to...
		    (A)dd a task?
		    (C)omplete a task?
		    (L)ist current tasks?
		    (R)eview completed tasks?
		    (Q)uit? ''' + '\n')

		# Adds a task to the to-do list
		if (response == 'A' or response == 'a'):
			toDo.add()

		# Removes a task from the to-do list and adds it to the completed list
		elif (response == 'C' or response == 'c'):
			toDo.completeTask()

		# Lists all tasks in to-do list
		elif (response == 'L' or response == 'l'):
			toDo.printTasks()  

		# Lists all tasks in completed list
		elif (response == 'R' or response == 'r'):
			toDo.printCompleted()        

		# Confirms exiting of the program
		elif (response == 'Q' or response == 'q'):
			exit = input('Are you sure you would like to exit? (Y/N)' + '\n')
			if (exit == 'Y' or exit == 'y'):
				raise SystemExit
		elif (exit == 'N' or exit == 'n'): {}

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

def main():
    toDoList = ['Add a task!']
    completedTasks = ['First task completed!']
    firstList = ToDoModule(toDoList, completedTasks)
    
    print("Welcome to Python To-Do!")
	# listMenu()
    while(1):
        taskMenu(firstList)       
if __name__ == '__main__': main()
