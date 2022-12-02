# 77476491
import sys


class FullDequeError(Exception):
    pass


class EmptyDequeError(Exception):
    pass


class MyDeque():
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__queue = [None] * self.__max_size
        self.__size = 0
        self.__head = None
        self.__tail = None

    def pop_back(self):
        if self.__size == 0:
            raise EmptyDequeError

        num = self.__queue[self.__tail]
        self.__queue[self.__tail] = None

        if self.__tail == 0:
            self.__tail = self.__max_size - 1
        else:
            self.__tail -= 1

        self.__size -= 1
        return num

    def pop_front(self):
        if self.__size == 0:
            raise EmptyDequeError

        num = self.__queue[self.__head]

        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1

        return num

    def push_back(self, num):
        if self.__size == self.__max_size:
            raise FullDequeError

        if self.__tail is None:
            self.__tail = 0
        else:
            self.__tail = (self.__tail + 1) % self.__max_size

        if self.__head is None:
            self.__head = self.__tail

        self.__queue[self.__tail] = num
        self.__size += 1

    def push_front(self, num):
        if self.__size == self.__max_size:
            raise FullDequeError

        if self.__head is None:
            self.__head = 0
        elif self.__head == 0:
            self.__head = self.__max_size - 1
        else:
            self.__head -= 1

        self.__queue[self.__head] = num

        if self.__tail is None:
            self.__tail = self.__head
        self.__size += 1


def call_method(the_deque, command):
    try:
        if ' ' in command:
            command, arg = command.split()
            command = getattr(the_deque, command)
            command(arg)
            return
        command = getattr(the_deque, command)
        print(command())
    except Exception:
        print('error')


if __name__ == '__main__':
    com_num = int(input())
    max_size = int(input())

    the_deque = MyDeque(max_size)
    for _ in range(com_num):
        command = sys.stdin.readline().rstrip()
        call_method(the_deque, command)
