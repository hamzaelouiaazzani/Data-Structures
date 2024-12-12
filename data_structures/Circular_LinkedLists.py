# The core Element of LinkedLists

class Node():
    def __init__(self , data = None , pointer_to_next_node = None):
        self.data = data
        self.pointer_to_next_node = pointer_to_next_node

class CircularLinkedList():

    def __init__(self , first_node_data):
        '''
        Initialize the LinkedList with the first Node.
        '''
        self.head = Node(first_node_data)
        self.head.pointer_to_next_node = self.head
        self.tail = self.head
        self.size = 1
        
    
    def insert_at_beginning(self , data):
        # create a new node that points to the current head
        new_node = Node(data , self.head)

        # let the current tail points to the the new node (circular process)
        self.tail.pointer_to_next_node = new_node

        # define the new node as the new head of the CircularLinkedList.
        self.head = new_node
        
        self.size = self.size + 1

    def insert_at_end(self , data):
        # create a new node that points to the current head
        new_node = Node(data , self.head)

        # let the current tail points to the new node
        self.tail.pointer_to_next_node = new_node

        # define the new node as the new tail of the CircularLinkedList
        self.tail = new_node

        self.size = self.size + 1
    

    # The new node (this node contains *data*) will be inserted just before the the node that contains *target_data* if existing
    def insert_before_target_data(self , data , target_data):
        # start with the first node of the linkedlist
        current_node = self.head

        # since the algorithm starts always with the first node and it checks *current_node.pointer_to_next_node.data* NOT *current_node.data*, you must give the first node a special treating
        if self.data == target_data:
            self.insert_at_beginning(data)

        

        # If the target data is not in the first node , move to next nodes
        else:
            # loop over the nodes of the CircularLinkedList until you find the node just before the node that contains *target_data*  or if it doesn't exist in all the Nodes
            while current_node.pointer_to_next_node is not self.head and current_node.pointer_to_next_node.data != target_data:
                current_node = current_node.pointer_to_next_node                 
                
            # If you find target_data in the CircularLinkedList's nodes, insert it right before the node where it exists
            if current_node.pointer_to_next_node is not self.head:
                # create a new node that points to target node
                new_node = Node(data , current_node.pointer_to_next_node)
        
                # update the node just before the node that contains *target_data* to point to the new node
                current_node.pointer_to_next_node = new_node

                self.size = self.size + 1
                
            # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
            else:
                print(f"The data {target_data} doesn't exist in any of this CircularLinkedList Nodes. Try some existing nodes please")


    # The new node (this node contains *data*) will be inserted just after the the node that contains *target_data* if existing
    def insert_after_target_data(self , data , target_data):
        # start with the first node of the Circularlinkedlist
        current_node = self.head

        # loop over the nodes of the LinkedList until you find the node that contains *target_data* or if it doesn't exist in all the Nodes
        while current_node is not self.tail and current_node.data != target_data:
            current_node = current_node.pointer_to_next_node 


        # If target_data is found in the last node (tail)
        if current_node == self.tail and current_node.data == target_data:
            self.insert_at_end(data)
        
        # If data_target node is found in one of the other nodes
        elif current_node is not self.tail:
        
            # create the new node
            new_node = Node(data , current_node.pointer_to_next_node)

            # update the node just after the node that contains *target_data*
            current_node.pointer_to_next_node = new_node

            self.size = self.size + 1

        # If you dont find *target_data* in this CircularLinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
        else:
            print(f"The data {target_data} doesn't exist in any of this CircularLinkedList Nodes. Try some existing nodes please")



    # Deleting te first Node of the CircularLinkedList
    def delete_first_node(self):

        if self.size > 1:
            # extract the adress of the the second node
            second_node = self.head.pointer_to_next_node
            
            # let the current tail points to the second node
            self.tail.pointer_to_next_node = second_node  
            
            # delete the current head
            del(self.head)
            
            # let the second node be the new head
            self.head = second_node

            self.size = self.size - 1
        else:
            print(f"Your CircularLinkedList Must contain at least 2 nodes to perform the Deletion operation. Your current LinkedList contains: {self.size} nodes!")
    
    
    # Deleting te last Node of the LinkedList
    def delete_last_node(self):
        
        if len(self)>1: 
            # start with the first node of the linkedlist
            current_node = self.head
            
            # loop over the nodes of the CircularLinkedList until you find the last node pointing to the head of the CircularLinkedList (circular process)
            while(current_node.pointer_to_next_node.pointer_to_next_node) is not self.head:
                current_node = current_node.pointer_to_next_node 

            # delete the current tail
            del(current_node.pointer_to_next_node)
            
            # let the node just before the last node point to the head of the CircularLinkedList (circular process).
            current_node.pointer_to_next_node = self.head
            
            # let the node that points to the last node (current tail) be the new tail
            self.tail = current_node

            self.size = self.size - 1

        else:
            print(f"Your LinkedList Must contain at least 2 nodes to perform the Deletion process.Your current LinkedList contains: {self.size} node!")
           

    # Delete the node containing target_data
    def delete_target_data(self , target_data):

        if len(self)>1:
            # start with the first node of the linkedlist
            current_node = self.head
            
            # since the algorithm starts always with the first node and it checks *current_node.pointer_to_next_node.data* NOT *current_node.data*, you must give the first node a special treating
            if current_node.data == target_data:
                self.delete_first_node()   
            
            else:
                # loop over the nodes of the CircularLinkedList until you find the target node or the tail node
                while current_node.pointer_to_next_node is not self.tail and current_node.pointer_to_next_node.data != target_data:
                    current_node = current_node.pointer_to_next_node 

                # If target_data is found in the last node (tail)
                if current_node.pointer_to_next_node == self.tail and current_node.pointer_to_next_node.data == target_data:
                    self.delete_last_node()
                    
                # If data_target node is found in one of the other nodes
                elif current_node.pointer_to_next_node is not self.tail:
                    target_node = current_node.pointer_to_next_node
                    del(current_node.pointer_to_next_node)
                    current_node.pointer_to_next_node = target_node.pointer_to_next_node
                    self.size = self.size - 1

                # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
                else:
                    print(f"The data {target_data} doesn't exist in any of this CircularLinkedList Nodes. Try some existing nodes please")
        else:
            print(f"Your LinkedList Must contain at least 2 nodes to perform the Deletion process. Your current LinkedList contains: {self.size} node!")
    


    # Edit the data of the node containing *target_data* node with *data*
    def edit_node_data(self , data , target_data):
        # start with the first node of the linkedlist
        current_node = self.head

        # loop over the nodes of the CircularLinkedList until you find the node that contains *target_data* or if it doesn't exist in all the Nodes
        while current_node.pointer_to_next_node is not self.head and current_node.data != target_data:
            current_node = current_node.pointer_to_next_node 

        # If the target Node is found, edit its data with *data* instead of *target_data*
        if current_node.data == target_data:
           current_node.data = data 

        # If you dont find *target_data* in this LinkedList, send a message to the user telling him to try another target_data that exists in this LinkedList's nodes
        else:
            print(f"The data {target_data} doesn't exist in any of this LinkedList Nodes. Try some existing nodes please")


    def swapping_nodes(self , target_data1 , target_data2):
        if self.size > 1:
            
            if target_data1 == target_data2:
                print("The two data are the same. Try swapping diffrent nodes please!")
              
            else:
                # Start with the first node of the linkedlist
                current_node = self.head
                
                # Searching for the Two Nodes In one PASS/traversal and Swapping their Data
                nodes_found = set()
                while current_node.pointer_to_next_node is not self.head and len(nodes_found)!=2:
                    if  current_node.data ==  target_data1:
                        node1 = current_node
                        nodes_found.add(target_data1)
                    elif current_node.data ==  target_data2:
                        nodes_found.add(target_data2)
                        node2 = current_node
                        
                    current_node = current_node.pointer_to_next_node
                
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

    # This method search for *target_data* in the LinkedList and return the target Node (with both its data the the Node to which it points
    def get_node_by_target_data(self , target_data):
        # Start with the first node of the linkedlist
        current_node = self.head  
        
        while current_node.pointer_to_next_node is not self.head and current_node.data != target_data:
            current_node = current_node.pointer_to_next_node

        if current_node.data == target_data:
            return current_node
        else:
            print(f"The node you are searching is NOT found. Try an existing node please!")
            return None


    def shift_right(self):
        # Start with the first node of the linkedlist
        current_node = self.head  

        # travel until you find the tail
        while current_node.pointer_to_next_node is not self.tail:
            current_node = current_node.pointer_to_next_node

        # update the new head with the tail
        self.head = self.tail

        # update the new tail with the node just before the previous tail
        self.tail = current_node


    def shift_left(self):
        self.tail = self.head
        self.head = self.head.pointer_to_next_node


    # Return the length of the LinkedList when using len(LinkedList) just like for python lists
    def __len__(self):
        return self.size
        
    
    def to_python_list(self):
        node_data_python_list , nodes_python_list , node_pointers_python_list = [] , [] , []
        
        current_node = self.head
        node_data_python_list.append(current_node.data)
        node_pointers_python_list.append(current_node.pointer_to_next_node)
        nodes_python_list.append(current_node)
        
        while(current_node.pointer_to_next_node) is not self.head:
            current_node = current_node.pointer_to_next_node
            node_data_python_list.append(current_node.data)
            node_pointers_python_list.append(current_node.pointer_to_next_node)
            nodes_python_list.append(current_node)
            
        return node_data_python_list , node_pointers_python_list , nodes_python_list