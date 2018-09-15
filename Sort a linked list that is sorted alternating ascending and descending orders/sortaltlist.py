class LinkedList:
	def __init__(self):
		self.head = None

	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None

	def newNode(self, key):
		return self.Node(key)

	def printlist(self):
		printval = self.head
		while printval != None:
			print (printval.data , end=' ')
			printval = printval.next
		print('')

	def lenglist(self):
		count = 0
		cur_val = self.head
		while cur_val is not None:
			count += 1
			cur_val = cur_val.next
		return count

	def reverseList(self, head):
		curr = head
		prev = None
		while curr != None:
			self.next = curr.next
			curr.next = prev
			prev = curr
			curr = self.next
		head = prev
		return head

	def mergeList(self, head1, head2):
		if head1 == None: return head2
		if head2 == None: return head1
		print(head1.data, head2.data)
		temp = None
		if head1.data < head2.data:
			temp = head1
			head1.next = self.mergeList(head1.next, head2)
		else:
			temp = head2
			head2.next = self.mergeList(head1, head2.next)
		return temp

	def mergeListIter(self, head1, head2):
		if head1 == None: return head2
		if head2 == None: return head1

		s = dummy = self.Node(0)

		while head1 != None and head2 != None:
			if head1.data < head2.data:
				curr = head1
				head1 = head1.next
			else:
				curr = head2
				head2 = head2.next
			dummy.next = curr
			dummy = dummy.next

		dummy.next = head1 or head2
		return s.next

	def splitList(self, Ahead, Dhead):
		asc = Ahead
		dsc = Dhead
		curr = self.head

		while curr != None:
			asc.next = curr
			asc = asc.next
			curr = curr.next
			if curr != None:
				dsc.next = curr
				dsc = dsc.next
				curr = curr.next
		asc.next = None
		dsc.next = None

	def sort(self):
		Ahead = self.Node(0)
		Dhead = self.Node(0)
		self.splitList(Ahead, Dhead)
		Ahead = Ahead.next
		Dhead = Dhead.next
		Dhead = self.reverseList(Dhead)
		self.head = self.mergeListIter(Ahead, Dhead)


#####################
# First linked list #
#####################

list1 = LinkedList()
list1.head = list1.newNode(2)
list1.head.next = list1.newNode(16)
list1.head.next.next = list1.newNode(8)
list1.head.next.next.next = list1.newNode(9)
list1.head.next.next.next.next = list1.newNode(15)
list1.head.next.next.next.next.next = list1.newNode(4)
list1.head.next.next.next.next.next.next = list1.newNode(24)


list1.printlist()

list1.sort()
list1.printlist()
