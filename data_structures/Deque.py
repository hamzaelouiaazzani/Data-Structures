# The item represents each element of the deque (equivelent to the node in LinkedLists)

class item():
    def __init__(self , data = None , next_item = None , previous_item = None):
        self.data = data
        self.next_item = next_item                # each item points to the next element in the direction Front ---------> Rear 
        self.previous_item = previous_item        # each item points to the next element in the direction Rear  ---------> Front 


class deque_linkedlist(): 

    
    def __init__(self , data = None):
        '''
        this constructor initializes the Deque
        '''
        self.front = item(data) if data is not None else None
        self.rear = self.front
        
        self.size = 0 if data is None else 1

    
    def enqueue_front(self , data):
        '''
        The operation of adding an element to the front of the Deque
        '''
        # create a new item that points next to the current front, and prev to the NULL node
        new_item = item(data , self.front , None)

        if not(self.isEmpty()):
            # let the current front points prev to the new item if the deque is not empty
            self.front.previous_item = new_item
        else:
            # if the deque is empty, define the new item as the the new rear
            self.rear = new_item

        # whether the deque is empty or not let the new item be the new front of the deque
        self.front = new_item

        self.size = self.size + 1

    
    def enqueue_rear(self , data):
        '''
        The operation of adding an element to the rear of the Deque
        '''
        # create an new item that points next to NULL and prev to the current rear
        new_item = item(data , None , self.rear)
        
        if not(self.isEmpty()):
            # let the current rear if points next to the new item if the deque is not empty
            self.rear.next_item = new_item
        else:
            # if the deque is empty, define the new item as the the new front
            self.front = new_item
            
        # whether the deque is empty or not let the new item be the new rear of the deque
        self.rear = new_item

        self.size = self.size + 1

    
    def dequeue_front(self):
        '''
        The operation of removing and returning the data from the front of the deque
        '''
        if not(self.isEmpty()):
            # data to be returned by the method and removed from the deque
            removed_data = self.front.data
            
            # get the second item in the deque list
            second_item = self.front.next_item

            # delete the current front
            del(self.front)
            
            # let the second item be the new front
            self.front = second_item
            
            # if only one item existing in the deque, let the rear be NULL
            if self.size == 1:
                self.rear = None
                
            # decrease the size of the deque
            self.size = self.size - 1
            
            return removed_data            


    def dequeue_rear(self):
        '''
        The operation of removing and returning the data from the rear of the deque
        '''
        if not(self.isEmpty()):
            # data to be returned by the method and removed from the deque
            removed_data = self.rear.data
            
            # get the penultimate item (the one previous to the rear) in the deque list
            penultimate_item = self.rear.previous_item

            # delete the current rear
            del(self.rear)
            
            # let the penultimate item be the new rear
            self.rear = penultimate_item
            
            # if only one item existing in the deque, let the front be NULL
            if self.size == 1:
                self.front = None
                
            # decrease the size of the deque
            self.size = self.size - 1
            
            return removed_data            
            
    
    def peek_front(self):
        '''
        The operation of viewing the data from the front of the deque
        '''
        if not self.isEmpty():
            return self.front.data


    def peek_rear(self):
        '''
        The operation of viewing the data from the rear of the deque
        '''
        if not self.isEmpty():
            return self.rear.data

    
    def __len__(self):
        '''
        The operation returning the size of the deque
        '''        
        return self.size  

    
    def isEmpty(self):
        '''
        The operation of verifying if the deque is empty or NOT
        '''        
        return not(self.size)

    
    def to_python_list(self):
        '''
        The operation of returning the data and adresses and pointers of the deque in a python list (for easy viewing and debuging)
        '''
        item_data_python_list = []
        current_item = self.front
        if self.size:
            item_data_python_list.append(current_item.data)
            while current_item.next_item is not None:
                current_item = current_item.next_item
                if current_item.data is not None:
                    item_data_python_list.append(current_item.data)
        return item_data_python_list




class array_deque(): 

    
    def __init__(self , data = None):
        '''
        this constructor initializes the deque
        '''
        self.deque = []

    
    def enqueue_front(self , data):
        '''
        The operation of adding an element to the front of the deque
        '''
        self.deque.insert(0, data)
        
    
    def enqueue_rear(self , data):
        '''
        The operation of adding an element to the rear of the Deque
        '''
        self.deque.append(data)

    
    def dequeue_front(self):
        '''
        The operation of removing and returning the data from the front of the deque
        '''
        if not(self.isEmpty()):
            return self.deque.pop(0)            


    def dequeue_rear(self):
        '''
        The operation of removing and returning the data from the rear of the deque
        '''
        if not(self.isEmpty()):
            return self.deque.pop()            
            
    
    def peek_front(self):
        '''
        The operation of viewing the data from the front of the deque
        '''
        if not(self.isEmpty()):
            return self.deque[0]


    def peek_rear(self):
        '''
        The operation of viewing the data from the rear of the deque
        '''
        if not(self.isEmpty()):
            return self.deque[-1]

    
    def isEmpty(self):
        '''
        The operation of verifying if the deque is empty or NOT
        '''        
        return not(len(self.deque))        