class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

	def index_correct(self, value):
		position = 0
		while value != None:
			value.position = position
			position += 1
			value = value.next

class SLinkedList:
	def __init__(self):
		self.headval = None

	def listprint(self):
		printval = self.headval
		while printval is not None:
			print (printval.dataval)
			printval = printval.nextval

	def iterate_from(list_item):
		while list_item is not None:
			yield list_item
			list_item = list_item.nextval

#####################
# First linked list #
#####################

list1 = SLinkedList()
list1.headval = Node(3)
a2 = Node(6)
a3 = Node(9)
a4 = Node(15)
a5 = Node(30)

# Link first Node to second node
list1.headval.nextval = a2

# Link second Node to third node
a2.nextval = a3
a3.nextval = a4
a4.nextval = a5

#list1.listprint()

######################
# Second linked list #
######################

list2 = SLinkedList()
list2.headval = Node(10)
b2 = a4
b3 = a5

# Link first Node to second node
list2.headval.nextval = b2

# Link second Node to third node
b2.nextval = b3

#list2.listprint()

######################################
# Look where the two lists intersect #
######################################

def test_func():
	for list1_item in [list1.headval, a2, a3, a4, a5]:
		for list2_item in [list2.headval, b2, b3]:
			if list1_item == list2_item:
				print(list1_item.dataval)
				return

test_func()
