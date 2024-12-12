# The core Element of LinkedLists
class Node():
    def __init__(self , data = None , pointer_to_next_node = None):
        self.data = data
        self.pointer_to_next_node = pointer_to_next_node

class LinkedList():


    def __init__(self , first_node_data = None):
        '''
        Initialize the LinkedList with the first Node.
        '''
        self.head = Node(first_node_data) if first_node_data is not None else None
        self.size = 0 if first_node_data is None else 1

    def insert_at_beginning(self , data):
        # create a new node that points to the current first node and define it as the new first node.
        self.head = Node(data , self.head)
        self.size = self.size + 1
    
    def insert_at_end(self , data):        
        if self.size:
            # start with the first node of the linkedlist
            current_node = self.head
            # loop over the nodes of the LinkedList until you find the last node; the last node is defined by pointing to NULL (None in Python)
            while(current_node.pointer_to_next_node) is not None:
                current_node = current_node.pointer_to_next_node
                
            # create a new node that points to NULL (None in Python)
            last_node = Node(data , pointer_to_next_node = None)
            
            # Let the current last node (current_node)  points to the new last node (last_node) 
            current_node.pointer_to_next_node = last_node
            self.size = self.size + 1
            
        else:
            self.insert_at_beginning(data)            

    # The new node (this node contains *data*) will be inserted just before the the node that contains *target_data*
    def insert_before_target_data(self , data , target_data):
        
        if self.size:
            # start with the first node of the linkedlist
            current_node = self.head
    
            # Since starts always with the first node and it checks *current_node.pointer_to_next_node.data* NOT *current_node.data*, you must give the first node a special treating
            if current_node.data == target_data:
                self.head = Node(data , self.head)
    
            # If the target data is not in the first node , move to next nodes
            else:
                # loop over the nodes of the LinkedList until you find the node just before the node that contains *target_data*  or if it doesn't exist in all the Nodes
                while current_node.pointer_to_next_node is not None and current_node.pointer_to_next_node.data != target_data:
                    current_node = current_node.pointer_to_next_node 
                        
                # If you find target_data in the LinkedList's nodes, insert it right before the node where it exists
                if current_node.pointer_to_next_node is not None:
                    # create the new node
                    new_node = Node(data , current_node.pointer_to_next_node)
            
                    # update the node just before the node that contains *target_data*
                    current_node.pointer_to_next_node = new_node
    
                # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
                else:
                    print(f"The data {target_data} doesn't exist in any of this LinkedList Nodes. Try some existing nodes please")
    
                # # If you find target_data in the LinkedList's nodes, insert it right before the node where it exists
                # if current_node.pointer_to_next_node.data == target_data:
                #     # create the new node
                #     new_node = Node(data , current_node.pointer_to_next_node)
            
                #     # update the node just before the node that contains *target_data*
                #     current_node.pointer_to_next_node = new_node
    
                # # If you dont find *target_data* in this LinkedList, send a message to the user to try another that exists in this LinkedList's nodes
                # else:
                #     print(f"The data {target_data} doesn't exist in any of this LinkedList Nodes. Try some existing nodes please")
        
        else: 
            print(f"This method functions only when your LinkedList is NOT empty!")
    
    # The new node (this node contains *data*) will be inserted just after the the node that contains *target_data*
    def insert_after_target_data(self , data , target_data):
        
        if self.size:
            # Start with the first node of the linkedlist
            current_node = self.head
    
            # loop over the nodes of the LinkedList until you find the node that contains *target_data* or if it doesn't exist in all the Nodes
            while current_node.pointer_to_next_node is not None and current_node.data != target_data:
                current_node = current_node.pointer_to_next_node 
    
            # If data_target node is found
            if current_node.data == target_data:
                # create the new node
                new_node = Node(data , current_node.pointer_to_next_node)
    
                # update the node just after the node that contains *target_data*
                current_node.pointer_to_next_node = new_node
    
            # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
            else:
                print(f"The data {target_data} doesn't exist in any of this LinkedList Nodes. Try some existing nodes please")
                
        else:
            print(f"This method functions only when your LinkedList is NOT empty!")
            

    # Deleting te first Node of the LinkedList
    def delete_first_node(self):
        
        if self.size:
            new_first_node = self.head.pointer_to_next_node
            del(self.head)    
            self.head = new_first_node
            self.size = self.size  - 1
        else:
            print(f"Your LinkedList Must contain at least one node to perform the Deletion process. Your current LinkedList is Empty")
            


    # Deleting te last Node of the LinkedList
    def delete_last_node(self):
        
        if self.size > 1:
            # start with the first node of the linkedlist
            current_node = self.head
            
            # loop over the nodes of the LinkedList until you find the last node; the last node is defined by pointing to NULL (None in Python)
            while(current_node.pointer_to_next_node.pointer_to_next_node) is not None:
                current_node = current_node.pointer_to_next_node 
    
            # delete the current last node
            del(current_node.pointer_to_next_node)
            # let the node just before the last node point to NULL (None in Python) and hence being the new last Node.
            current_node.pointer_to_next_node = None
            self.size = self.size  - 1

        elif self.size == 1:
            self.delete_first_node()
            
        else:
            print(f"Your LinkedList Must contain at least one node to perform the Deletion process. Your current LinkedList is Empty")
            

    # Delete the node containing target_data
    def delete_target_data(self , target_data):
        
        if self.size == 1:
            if self.head.data == target_data:
                self.delete_first_node()
            else:
                print(f"The data {target_data} doesn't exist in the head of this LinkedList. If you want to delete the head use delete_first_node method without using target_data argument!")
                
        elif self.size > 1:
            # start with the first node of the linkedlist
            current_node = self.head
            
            # Since the algorithm starts always with the first node and it checks *current_node.pointer_to_next_node.data* NOT *current_node.data*, you must give the first node a special treating
            if current_node.data == target_data:
                self.delete_first_node()   
    
            else:
                # loop over the nodes of the LinkedList until you find the last node; the last node is defined by pointing to NULL (None in Python)
                while current_node.pointer_to_next_node is not None and current_node.pointer_to_next_node.data != target_data:
                    current_node = current_node.pointer_to_next_node 
                    
                # If data_target node is found
                if current_node.pointer_to_next_node is not None:
                    target_node = current_node.pointer_to_next_node
                    del(current_node.pointer_to_next_node)
                    current_node.pointer_to_next_node = target_node.pointer_to_next_node
                    self.size = self.size  - 1
                    
                # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
                else:
                    print(f"The data {target_data} doesn't exist in any of this LinkedList Nodes. Try some existing nodes please")
        
        elif not(self.size):
            print(f"Your LinkedList Must contain at least one node to perform the Deletion operation. Your current LinkedList is Empty")


    
    # Edit the data of the node containing *target_data* node with *data*
    def edit_node_data(self , data , target_data):

        if self.size:
            # start with the first node of the linkedlist
            current_node = self.head
    
            # loop over the nodes of the LinkedList until you find the node that contains *target_data* or if it doesn't exist in all the Nodes
            while current_node.pointer_to_next_node is not None and current_node.data != target_data:
                current_node = current_node.pointer_to_next_node 
    
            # If the target Node is found, edit its data with *data* instead of *target_data*
            if current_node.data == target_data:
               current_node.data = data 
    
            # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
            else:
                print(f"The data {target_data} doesn't exist in any of this LinkedList Nodes. Try some existing nodes please")
                
        else:
            print(f"Your LinkedList Must contain at least one node to perform the editing operation. Your current LinkedList is Empty")

    
    def swapping_nodes(self , target_data1 , target_data2):
        
        if self.size > 1:
            
            if target_data1 == target_data2:
                print("The two data are the same. Try swapping diffrent nodes please!")
    
            else:
                # Start with the first node of the linkedlist
                current_node = self.head
                
                # Searching for the Two Nodes In one PASS/traversal and Swapping their Data
                n_nodes_found = 0
                nodes_found = set()
                while current_node.pointer_to_next_node is not None and n_nodes_found!=2:
                    if  current_node.data ==  target_data1:
                        n_nodes_found = n_nodes_found + 1
                        node1 = current_node
                        nodes_found.add(target_data1)
                    if current_node.data ==  target_data2:
                        n_nodes_found = n_nodes_found + 1
                        nodes_found.add(target_data2)
                        node2 = current_node
                        
                    current_node = current_node.pointer_to_next_node
        
                if n_nodes_found!=2:   
                    if  current_node.data ==  target_data1:
                        n_nodes_found = n_nodes_found + 1
                        node1 = current_node
                        nodes_found.add(target_data1)
                    elif current_node.data ==  target_data2:
                        n_nodes_found = n_nodes_found + 1
                        nodes_found.add(target_data2)
                        node2 = current_node
                        
                if n_nodes_found==0:
                    print(f"None of the two nodes is found in the this LinkedList. Try two existing nodes please!")
                if n_nodes_found==1:
                    print(f"The node with data {nodes_found} is found but the other Node is NOT found. Try two existing nodes please!")                
                if n_nodes_found==2:
                    node1.data , node2.data = node2.data , node1.data

        else:
            print(f"Your LinkedList Must contain at least two nodes to perform the swapping process. Your current LinkedList has {self.size} nodes")   

    
    # This method search for *target_data* in the LinkedList and return the target Node (with both its data the the Node to which it points
    def get_node_by_target_data(self , target_data):
        
        if self.size:
            # start with the first node of the linkedlist
            current_node = self.head  
            while current_node.pointer_to_next_node is not None and current_node.data != target_data:
                current_node = current_node.pointer_to_next_node
    
            if current_node.data == target_data:
                return current_node
            else:
                print(f"The node you are searching is NOT found. Try an existing node please!")
        else:
            print(f"Your LinkedList Must contain at least one node to perform 'get node' operation. Your current LinkedList is Empty")
                

    # Return the length of the LinkedList when using len(LinkedList) just like for python lists
    def __len__(self):
        return self.size

    
    def to_python_list(self):
        node_data_python_list , nodes_python_list , node_pointers_python_list = [] , [] , []

        if self.size:
            current_node = self.head
            node_data_python_list.append(current_node.data)
            node_pointers_python_list.append(current_node.pointer_to_next_node)
            nodes_python_list.append(current_node)
            
            while(current_node.pointer_to_next_node) is not None:
                current_node = current_node.pointer_to_next_node
                node_data_python_list.append(current_node.data)
                node_pointers_python_list.append(current_node.pointer_to_next_node)
                nodes_python_list.append(current_node)
            
        return node_data_python_list , node_pointers_python_list , nodes_python_list