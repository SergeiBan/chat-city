# 77201164
import sys


class MyDeque():
	def __init__(self, max_size):
		self.queue = [None] * max_size
		self.max_size = max_size
		self.size = 0
		self.head = None
		self.tail = None

	def pop_back(self):
		if self.size == 0:
			return 'error'
		
		num = self.queue[self.tail]
		self.queue[self.tail] = None

		if self.tail == 0:
			self.tail = self.max_size - 1
		else:
			self.tail -= 1

		self.size -= 1
		return num

	def pop_front(self):
		if self.size == 0:
			return 'error'
			
		num = self.queue[self.head]

		self.queue[self.head] = None
		self.head = (self.head + 1) % self.max_size
		self.size -= 1

		return num

	def push_back(self, num):
		if self.size == self.max_size:
			print('error')
			return

		if self.tail is None:
			self.tail = 0
		else:
			self.tail = (self.tail + 1) % self.max_size
		
		if self.head is None:
			self.head = self.tail

		self.queue[self.tail] = num
		self.size += 1

	def push_front(self, num):
		if self.size == self.max_size:
			print('error')
			return

		if self.head is None:
			self.head = 0
		elif self.head == 0:
			self.head = self.max_size - 1
		else:
			self.head -= 1

		self.queue[self.head] = num
		
		if self.tail is None:
			self.tail = self.head
		self.size += 1


if __name__ == '__main__':
	com_num = int(input())
	max_size = int(input())
	
	the_deque = MyDeque(max_size)
	for com_idx in range(com_num):
		command = sys.stdin.readline().rstrip()
		if command == 'pop_back':
			print(the_deque.pop_back())
		elif command == 'pop_front':
			print(the_deque.pop_front())
		else:
			comm, arg = command.split()
			method = getattr(the_deque, comm)
			method(arg)
