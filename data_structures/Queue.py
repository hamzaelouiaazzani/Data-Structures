# The item represents each element of the queue (equivelent to the node in LinkedLists)

class item():
    def __init__(self , data = None , next_item = None):
        self.data = data
        self.next_item = next_item



class queue_linkedlist(): 

    def __init__(self , data = None):
        '''
        this constructor initializes the Queue
        '''
        self.front = item(data) if data is not None else None
        self.rear = self.front
        
        self.size = 0 if data is None else 1

    def enqueue(self , data):
        '''
        The operation of adding an element to the rear of the queue
        '''
        
        # create an item to the current NULL
        new_item = item(data , None)

        if not(self.isEmpty()):
            # let the current rear if exists points to the the new item
            self.rear.next_item = new_item
        else: 
            self.front = new_item
            
        # let the new item be the new rear of the queue
        self.rear = new_item

        # increase the size of the queue
        self.size = self.size + 1
        

    def dequeue(self):
        '''
        The operation of removing and returning an element from the front of the queue
        '''
        if not(self.isEmpty()):
            
            # data to be returned by the method and removed from the queue
            removed_data = self.front.data
            
            # get the second item in the queue list
            second_item = self.front.next_item

            # delete the current front
            del(self.front)

            # let the second item be the new front
            self.front = second_item

            # decrease the size of the Queue
            self.size = self.size - 1
            
            return removed_data


    def peek(self):
        if not self.isEmpty():
            return self.front.data

        
    def isEmpty(self):
        return not(self.size)

        
    def __len__(self):
        return self.size  


    def to_python_list(self):
        item_data_python_list = []
        current_item = self.front
        if self.size:
            item_data_python_list.append(current_item.data)
            while current_item.next_item is not None:
                current_item = current_item.next_item
                if current_item.data is not None:
                    item_data_python_list.append(current_item.data)
        return item_data_python_list



class queue_array():
    def __init__(self):
        self.queue = []

    def enqueue(self , data):
        '''
        The operation of adding an element to the rear of the queue
        '''
        self.queue.append(data)

    def dequeue(self):
        '''
        The operation of removing and returning an element from the front of the queue
        '''
        if not(self.isEmpty()):
            return self.queue.pop(0)

    def peek(self):
        if not(self.isEmpty()):
            return self.queue[0]

    def isEmpty(self):
        return not(len(self.queue))

        
    def __len__(self):
        return len(self.queue)  