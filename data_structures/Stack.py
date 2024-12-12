# The item represents each element of the stack (equivelent to the node in LinkedLists)

class item():
    def __init__(self , data = None , next_item = None):
        self.data = data
        self.next_item = next_item

class stack_linkedlist(): 

    def __init__(self , base_data = None):
        '''
        this constructor initializes the stack with the base item (the bottom of the stack) which is also the top item at the begining
        '''
        self.top = item(base_data)
        self.size = 0 if self.top.data is None else 1
    
    # push data to the top of the stack
    def push(self , data):
        # create new item that points to the current top of the stack
        new_item = item(data , self.top)
        # update the top itme with the new item
        self.top = new_item
        self.size = self.size + 1
    
    # remove the current top item and return the data of the removed item
    def pop(self):
        if not self.isEmpty():
            # extract the item that comes after the current top
            new_top = self.top.next_item
            data_to_return = self.top.data
            # delete the current top
            del(self.top)
            # define new_top as the new top item of the stack
            self.top = new_top

            self.size = self.size - 1
            return data_to_return

    
    # View the element at the top of the stack without removing it
    def peek(self):
        return self.top.data

    
    # return True if the stack is empty, False otherwise
    def isEmpty(self):
        return not(self.size)
    #     return self.top.next_item is None and self.top.data is None

    
    def __len__(self):
        return self.size
            
    def to_python_list(self):
        item_data_python_list = []
        current_item = self.top
        if current_item.data is not None:
            item_data_python_list.append(current_item.data)
            
        while current_item.next_item is not None:
            current_item = current_item.next_item
            if current_item.data is not None:
                item_data_python_list.append(current_item.data)
        return item_data_python_list




class stack_array(): 

    def __init__(self):
        '''
        this constructor initializes the stack with a python list
        '''
        self.stack = []
    
    # push data to the top of the stack
    def push(self , data):
        self.stack.append(data)
    
    # remove the current top item and return the data of the removed item
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    
    # View the element at the top of the stack without removing it
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    
    # return True if the stack is empty, False otherwise
    def isEmpty(self):
        return not(len(self))
    #     return self.top.next_item is None and self.top.data is None

    
    def __len__(self):
        return len(self.stack)