'''
Python To-Do
A simple to-do list program using text files to hold tasks
Authored by: Bryce Buchanan
'''

# TO DO 1. Convert to class
# TO DO 2. Allow editing of tasks
# TO DO 3. Detemine and implement best data structure
# TO DO 4. File I/O
# TO DO 5. GUI


#class ToDoItem:
#	def __init__(self, task):
#		self.task = task
#		self.next = None

#	def get(self):
#		return self.task


class ToDoModule:
	def __init__(self, toDoList, completedTasks, head = None):
		self.toDoList = toDoList
		self.completedTasks = completedTasks
		self.head = head

	def add(self):
		self.toDoList.append(input('Type your task here: '))

	def completeTask(self):
		while (1):
			try:
				completed = int(input('Which task number would you like to complete? (Enter index): '))
				break
			except ValueError:
				print('Not a valid task number')
		self.completedTasks.append(self.toDoList[completed - 1])
		del self.toDoList[completed - 1]

	def printTasks(self):
		for task in self.toDoList:
			index = "{}".format(self.toDoList.index(task) + 1)
			print(index + '. ' + task + '\n')
		print('\n')

	def printCompleted(self):
		for task in self.completedTasks:
			index = "{}".format(self.completedTasks.index(task) + 1)
			print(index + '. ' + task, end = '\n')
		print('\n')