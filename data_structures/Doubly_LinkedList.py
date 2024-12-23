# The core Element of LinkedLists
class Node():
    def __init__(self , data = None , pointer_to_next_node = None , pointer_to_previous_node = None):
        self.data = data
        self.pointer_to_next_node = pointer_to_next_node
        self.pointer_to_previous_node = pointer_to_previous_node

class DoublyLinkedList():


    def __init__(self , first_node_data=None , is_circular=False):
        '''
        Initialize the DoublyLinkedList with the first Node.
        '''
        self.is_circular = is_circular
        if self.is_circular:
            # Circular LinkedLists Must at least have one Node!
            if first_node_data is not None:
                self.head = Node(first_node_data)
                self.head.pointer_to_next_node = self.head
                self.head.pointer_to_previous_node = self.head
                self.tail = self.head
                self.size = 1
            else:
                print("CircularDoublyLinkedList Must at least contain one node. Please Initialize your CircularDoublyLinkedList with a data!. You will get the following Error if first_node_data is None!")
                print("AttributeError: 'DoublyLinkedList' object has no attribute 'size'")

        
        else:
            self.head = Node(first_node_data) if first_node_data is not None else None
            self.tail = self.head
            self.size = 0 if first_node_data is None else 1
        

    def insert_at_beginning(self , data):

        if self.size:
            # create a new node that points next to the current head, and points prev to the node to which the current head points prev to.
            new_node = Node(data , self.head , self.head.pointer_to_previous_node)
    
            # the current head must point prev to the new node
            self.head.pointer_to_previous_node = new_node
    
            # define the new node as the new head of the DoublyLinkedList.
            self.head = new_node
            
            # if the DoublyLinkedList is circular: 
            if self.is_circular:
                # let the current tail points to the the new node (circular process)
                self.tail.pointer_to_next_node = new_node

            self.size = self.size + 1
            
        else:
            self.head = Node(data)
            self.tail = self.head
            self.size = 1
            
        
    def insert_at_end(self , data):
        
        if self.size:
            # create a new node that points next to the head and prev to the current head 
            new_node = Node(data , self.tail.pointer_to_next_node , self.tail)
    
            # let the current tail points next to the new node
            self.tail.pointer_to_next_node = new_node
            if self.is_circular:
                # let the head points prev to the the new node
                self.head.pointer_to_previous_node = new_node            
    
            # update the tail with the new node
            self.tail = new_node
            self.size = self.size + 1

        else:
            self.insert_at_beginning(data)
            


    # The new node (this node contains *data*) will be inserted just before the the node that contains *target_data* if existing
    def insert_data(self , data , target_data , direction = "forward" , position="before" , start_node = None):
        
        if self.size > 1:
            if position=="before" and self.head.data == target_data:
                self.insert_at_beginning(data)  
            
            elif position=="after" and self.tail.data == target_data:
                self.insert_at_end(data)
            
            else:
                
                target_node = self.get_node_by_target_data(target_data , direction , start_node)
                if target_node is not None:
                    if position=="before":
                        new_node = Node(data , target_node, target_node.pointer_to_previous_node)
                        target_node.pointer_to_previous_node.pointer_to_next_node = new_node
                        target_node.pointer_to_previous_node = new_node
                        self.size = self.size + 1
                    elif position=="after":
                        new_node = Node(data , target_node.pointer_to_next_node, target_node)
                        target_node.pointer_to_next_node.pointer_to_previous_node = new_node
                        target_node.pointer_to_next_node = new_node
                        self.size = self.size + 1
                
                # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
                else:
                    print(f"The data {target_data} doesn't exist in any of this DoublyLinkedList Nodes. Try some existing nodes please")

        elif self.size == 1:
            if self.head.data == target_data:
                if position == "before":
                    self.insert_at_beginning(data)
                if position == "after":
                    self.insert_at_end(data)
            else:
                print(f"The data {target_data} doesn't exist in the head of this LinkedList. If you want to insert before/after the head use insert_at_beginning/insert_at_end method instead without using target_data argument!")
            

        else:
            print(f"This method functions only when your LinkedList is NOT empty!")


    # Deleting te first Node of the DoublyLinkedList
    def delete_first_node(self):

        if self.size > 1:
            # extract the adress of the the second node 
            second_node = self.head.pointer_to_next_node

            # let the second node points prev  to which the current head points prev (NULL or the tail depending on circularity of the LinkedList)
            second_node.prev = self.head.pointer_to_previous_node
            
            # let the current tail points next to NULL node if the LinkedList is NOT circular, and to the second node otherwise
            self.tail.pointer_to_next_node = second_node if self.is_circular else None
 
            # delete the current head
            del(self.head)
            
            # let the second node be the new head
            self.head = second_node
            
            self.size = self.size  - 1
            
        elif self.size == 1:
            if self.is_circular:
                print(f"Your CircularDoublyLinkedList Must contain at least 2 nodes to perform the Deletion operation. Your current CircularDoublyLinkedList has only One Node!")
            else:
                self.head = None
                self.tail = None
                self.size = 0

        else:
            print(f"Your DoublyLinkedList Must contain at least one node to perform the Deletion operation. Your current LinkedList is Empty")
    

    # Deleting te last Node of the LinkedList
    def delete_last_node(self):

        if self.size > 1: 
             # extract the adress of the penultimate node 
            penultimate_node = self.tail.pointer_to_previous_node           

            # let the penultimate_node points next to the node to which the current tail points next to (NULL or the head depending on circularity of the LinkedList)
            penultimate_node.pointer_to_next_node = self.tail.pointer_to_next_node

            # let the current head points prev to NULL node if the LinkedList is NOT circular, and to the penultimate_node otherwise
            self.head.pointer_to_previous_node = penultimate_node if self.is_circular else None
            
            # delete the current tail
            del(self.tail)
            
            # let the penultimate node be the new tail
            self.tail = penultimate_node

            self.size = self.size  - 1

        elif self.size == 1:
            if self.is_circular:
                print(f"Your CircularDoublyLinkedList Must contain at least 2 nodes to perform the Deletion operation. Your current CircularDoublyLinkedList has only One Node!")
            else:
                self.head = None
                self.tail = None
                self.size = 0

        else:
            print(f"Your DoublyLinkedList Must contain at least one node to perform the Deletion operation. Your current LinkedList is Empty")
    



    # Delete the node containing target_data
    def delete_target_data(self , target_data , direction = "forward" , start_node = None):

        if self.size > 1:

            if self.head.data == target_data:
                self.delete_first_node()  

            elif self.tail.data == target_data:
                self.delete_last_node()  
            
            else:
                target_node = self.get_node_by_target_data(target_data , direction , start_node)
                if target_node is not None:
                    target_node.pointer_to_previous_node.pointer_to_next_node = target_node.pointer_to_next_node
                    target_node.pointer_to_next_node.pointer_to_previous_node = target_node.pointer_to_previous_node
                    del(target_node)
                    self.size = self.size  - 1
    
                # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
                else:
                    print(f"The data {target_data} doesn't exist in any of this DoublyLinkedList Nodes. Try some existing nodes please")                    

        elif self.size == 1:
            if self.is_circular:
                print(f"Your CircularDoublyLinkedList Must contain at least 2 nodes to perform the Deletion operation. Your current CircularDoublyLinkedList has only One Node!")
            else:
                if self.head.data == target_data:
                    self.head = None
                    self.tail = None
                    self.size = 0
                else:
                    print(f"The data {target_data} doesn't exist in the head of this LinkedList. If you want to delete the head use method delete_first_node instead without using target_data argument!")
                    

        else:
            print(f"Your DoublyLinkedList Must contain at least one node to perform the Deletion operation. Your current LinkedList is Empty")

    # Edit the data of the node containing *target_data* node with *data*
    def edit_node_data(self , data , target_data , direction = "forward" , start_node = None):
        
        if self.size:
            if self.head.data == target_data:
                self.head.data = data  
    
            elif self.tail.data == target_data:
                self.tail.data.tail = data
    
            else:
                target_node = self.get_node_by_target_data(target_data , direction , start_node)
                if target_node is not None:
                    target_node.data = data
                else:
                    print(f"The data {target_data} doesn't exist in any of this DoublyLinkedList Nodes. Try some existing nodes please")                    
        else:
            print(f"Your LinkedList Must contain at least one node to perform the editing operation. Your current LinkedList is Empty")


    def get_node_by_target_data(self , target_data , direction = "forward" , start_node = None):
        
        if self.size:
            if direction == "backward":
                pointer_direction = "pointer_to_previous_node"
                if not start_node:
                    start_node = self.tail
            else:
                pointer_direction = "pointer_to_next_node"
                if not start_node:
                    start_node = self.head
            
            current_node = start_node
            # Stop when you find the target node. If you dont' keep the bool until you get back to the starting node if  the DoublyLinkedList is circular, if it is non circular, stop when you find the tail node (pointing to NULL) otherwise
            end_of_list_condition = start_node  if self.is_circular else None
            
            while getattr(current_node, pointer_direction) is not end_of_list_condition and current_node.data != target_data:
                # print(f"I am in first loop: {current_node.data}")
                current_node = getattr(current_node, pointer_direction) 
                
            if getattr(current_node, pointer_direction) is None and current_node.data != target_data:
                # print(f"I am about transition from None to starting : {current_node.data}")
                if (start_node!=self.head and direction == "forward") or (start_node!=self.tail and direction == "backward"):
                    if direction == "forward":
                        current_node = self.head
                    else:
                        current_node = self.tail
                    # print(f"I am in second loop: {current_node.data}")
                    while getattr(current_node, pointer_direction) is not start_node and current_node.data != target_data:
                        current_node = getattr(current_node, pointer_direction)
                        # print(f"I am in second loop: {current_node.data}")  
            
            if current_node.data == target_data:
                return current_node
    
            else:
                print(f"The data {target_data} doesn't exist in any of this DoublyLinkedList Nodes. Try some existing nodes please")
                
        else:
            print(f"Your LinkedList Must contain at least one node to perform 'get node' operation. Your current LinkedList is Empty")        

    def swapping_nodes(self , target_data1 , target_data2  , direction = "forward" , start_node = None):

        if self.size > 1:
            if target_data1 == target_data2:
                print("The two data are the same. Try swapping diffrent nodes please!")
    
            else:
                if direction == "backward":
                    pointer_direction = "pointer_to_previous_node"
                    if not start_node:
                        start_node = self.tail
                else:
                    pointer_direction = "pointer_to_next_node"
                    if not start_node:
                        start_node = self.head
    
                # Searching for the Two Nodes In one PASS/traversal and Swapping their Data
                nodes_found = set()
                    
                current_node = start_node
                # Stop when you find the target node. If you dont' keep the bool until you get back to the starting node if  the DoublyLinkedList is circular, if it is non circular, stop when you find the tail node (pointing to NULL) otherwise
                end_of_list_condition = start_node  if self.is_circular else None 
                while getattr(current_node, pointer_direction) is not end_of_list_condition and len(nodes_found)!=2:
                    if  current_node.data ==  target_data1:
                        node1 = current_node
                        nodes_found.add(target_data1)
                    elif current_node.data ==  target_data2:
                        nodes_found.add(target_data2)
                        node2 = current_node                        
                    current_node = getattr(current_node, pointer_direction) 
            
                if getattr(current_node, pointer_direction) is None and len(nodes_found)!=2:
                    print(f"I am about transition from None to starting node: {current_node.data}")
                    if (start_node!=self.head and direction == "forward") or (start_node!=self.tail and direction == "backward"):
                        print("The condition is don")
                        if direction == "forward":
                            current_node = self.head
                        else:
                            current_node = self.tail
                        print(f"I am in second loop: {current_node.data}")
                        while getattr(current_node, pointer_direction) is not start_node and len(nodes_found)!=2:
                            if  current_node.data ==  target_data1:
                                node1 = current_node
                                nodes_found.add(target_data1)
                            elif current_node.data ==  target_data2:
                                nodes_found.add(target_data2)
                                node2 = current_node                        
                            current_node = getattr(current_node, pointer_direction)
                            print(f"I am in second loop: {current_node.data}")    
                if len(nodes_found)!=2:   
                    if  current_node.data ==  target_data1:
                        node1 = current_node
                        nodes_found.add(target_data1)
                    elif current_node.data ==  target_data2:
                        nodes_found.add(target_data2)
                        node2 = current_node
                if len(nodes_found)==0:
                    print(f"None of the two nodes is found in the this LinkedList. Try two existing nodes please!")
                if len(nodes_found)==1:
                    print(f"The node with data {nodes_found} is found but the other Node is NOT found. Try two existing nodes please!")                
                if len(nodes_found)==2:
                    node1.data , node2.data = node2.data , node1.data

        else:
            print(f"Your LinkedList Must contain at least two nodes to perform the swapping process. Your current LinkedList has {self.size} node!")   

    def shift_right(self):
        # update the new head with the tail
        self.head = self.tail
        # update the new tail with the node just before the previous tail
        self.tail = self.tail.pointer_to_previous_node


    def shift_left(self):
        self.tail = self.head
        self.head = self.head.pointer_to_next_node

    

    # Return the length of the LinkedList when using len(LinkedList) just like for python lists
    def __len__(self):
        return self.size
    
    

    def to_python_list(self):
        node_data_python_list , nodes_python_list , node_pointers_next_python_list , node_pointers_prev_python_list = [] , [] , [] , []
        
        if self.size:
            current_node = self.head
            node_data_python_list.append(current_node.data)
            node_pointers_next_python_list.append(current_node.pointer_to_next_node)
            node_pointers_prev_python_list.append(current_node.pointer_to_previous_node)
            nodes_python_list.append(current_node)
            
            end_of_list_condition = self.head if self.is_circular else None
            while(current_node.pointer_to_next_node) is not end_of_list_condition:
                current_node = current_node.pointer_to_next_node
                node_data_python_list.append(current_node.data)
                node_pointers_next_python_list.append(current_node.pointer_to_next_node)
                node_pointers_prev_python_list.append(current_node.pointer_to_previous_node)
                nodes_python_list.append(current_node)
            
        return node_data_python_list , node_pointers_next_python_list , node_pointers_prev_python_list , nodes_python_list