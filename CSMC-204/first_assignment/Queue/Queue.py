

class Queue:

    def __init__(self):
        self.queue = []
        self.head = None

    def enqueue(self, item):
        self.head = item
        self.queue.append(item)

    def dequeue(self, number_to_remove = 1):
        if len(self.queue) == 0:
            print('no item in queue')
            return None
        for _ in range(number_to_remove):
            self.queue.pop(0)
        self.head = self.queue[0]
    # return name and schedule
    def search(self, item):
        return item in self.queue

    def peek(self):
        return self.head
    
    def display_queue(self):

        if len(self.queue) > 0:
            final_print_item = ""
            for index in range(len(self.queue)):
                if index == len(self.queue)-1:
                    final_print_item += f"{self.queue[index]}"
                else:
                    final_print_item += f"{self.queue[index]} -> "
            print(final_print_item)
        else:
            print('no item in queue')

    def simple_queue(self):
        
        return self.queue
