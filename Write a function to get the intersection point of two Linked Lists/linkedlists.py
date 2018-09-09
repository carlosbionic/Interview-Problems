class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def index_correct(self, value):
		position = 0
		while value != None:
			value.position = position
			position += 1
			value = value.next

class SLinkedList:
	def __init__(self):
		self.head = None

	def listprint(self):
		printval = self.head
		while printval is not None:
			print (printval.data)
			printval = printval.next

	def iterate_from(list_item):
		while list_item is not None:
			yield list_item
			list_item = list_item.next

	def leng(self):
		count = 0
		cur_val = self.head
		while cur_val is not None:
			count += 1
			cur_val = cur_val.next
		return count

#####################
# First linked list #
#####################

list1 = SLinkedList()
list1.head = Node(5)
a2 = Node(8)
a3 = Node(11)
a4 = Node(5)
a5 = Node(7)

# Link first Node to second node
list1.head.next = a2

# Link second Node to third node
a2.next = a3
a3.next = a4
a4.next = a5

#list1.listprint()

######################
# Second linked list #
######################

list2 = SLinkedList()
list2.head = Node(2)
b2 = a4
b3 = a5

# Link first Node to second node
list2.head.next = b2

# Link second Node to third node
b2.next = b3

#list2.listprint()

######################################
# Look where the two lists intersect #
######################################
#print(list1.leng(), list2.leng())

def method1():

	cur1 = list1.head
	for i in range(list1.leng()):

		cur2 = list2.head
		for j in range(list2.leng()):

			if cur1 == cur2:
				print("Element: ", cur1.data, "\nFirst index: ", i, "\nSecond index: ", j)
				return

			cur2 = cur2.next
		cur1 = cur1.next



def method3():

	len1,len2 = list1.leng(),list2.leng()
	d = abs( len1 - len2 )

	cur1, cur2 = list1.head, list2.head

	if len1 > len2:
		for i in range(d):
			cur1 = cur1.next

	elif len2 > len1:
		for i in range(d):
			cur2 = cur2.next

	i = d
	while cur1 != cur2:
		cur1 = cur1.next
		cur2 = cur2.next
		i += 1

	print("Element: ", cur1.data, "\nFirst index: ", i, "\nSecond index: ", i-d)

method1()
