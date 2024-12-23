from Singly_LinkedLists import LinkedList


class LinkedList_hash(LinkedList):
    """
    A class that extends the LinkedList class to specifically handle buckets in a hash table.

    Methods:
        search_key_in_bucket(key): Searches for a key in the bucket (linked list).
        delete_key(key): Deletes a node containing the specified key.
        get_bucket_keys(): Retrieves all keys stored in the bucket.
        get_bucket_values(): Retrieves all values stored in the bucket.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the LinkedList_hash object, inheriting attributes and methods from LinkedList.
        """
        super().__init__(*args, **kwargs)  # Inherit attributes and methods from LinkedList

    
    def search_key_in_bucket(self, key):
        """
        Search if a key is already existing in the bucket (linked list).

        Args:
            key (any): The key to search for.

        Returns:
            Node: The node containing the key, or None if the key is not found.
        """
        if self.size:
            current_node = self.head
            while current_node.pointer_to_next_node is not None and current_node.data[0] != key:
                current_node = current_node.pointer_to_next_node
            if current_node.data[0] == key:
                return current_node
        return None  # Explicitly return None if key is not found

    def delete_key(self, key):
        """
        Deletes the node containing the specified key in the linked list.

        Args:
            key (any): The key to delete.

        Raises:
            KeyError: If the key is not found in the linked list.
        
        Returns:
            bool: True if deletion is successful.
        """
        if self.size == 0:
            raise KeyError("Key not found: LinkedList is empty.")

        if self.head.data[0] == key:
            self.delete_first_node()
            return True  # Indicate successful deletion

        current_node = self.head
        while current_node.pointer_to_next_node is not None:
            if current_node.pointer_to_next_node.data[0] == key:
                target_node = current_node.pointer_to_next_node
                current_node.pointer_to_next_node = target_node.pointer_to_next_node
                del target_node
                self.size -= 1
                return True  # Indicate successful deletion

        raise KeyError(f"Key not found: {key}")

    def get_bucket_keys(self):
        """
        Retrieve all keys stored in the bucket.

        Returns:
            list: A list of keys.
        """
        keys = []
        if self.size:
            current_node = self.head
            keys.append(current_node.data[0])
            while current_node.pointer_to_next_node is not None:
                current_node = current_node.pointer_to_next_node
                keys.append(current_node.data[0])
        return keys

    def get_bucket_values(self):
        """
        Retrieve all values stored in the bucket.

        Returns:
            list: A list of values.
        """
        values = []
        if self.size:
            current_node = self.head
            values.append(current_node.data[1])
            while current_node.pointer_to_next_node is not None:
                current_node = current_node.pointer_to_next_node
                values.append(current_node.data[1])
        return values


class hash_table():
    """
    A class to implement a hash table with separate chaining for collision handling.

    Attributes:
        size (int): The number of buckets in the hash table.
        n_items (int): The number precomputed number of items (key-value pairs).
        array_buckets (list): A list of buckets, each being a LinkedList_hash object.

    Methods:
        _hash(key): Computes the hash index for a given key.
        insert(key, value): Inserts or updates a key-value pair in the hash table.
        search(key): Searches for a key and returns its value.
        delete(key): Deletes a key-value pair.
        load_factor(): Computes the load factor of the hash table.
        resize(size): Resizes the hash table when necessary.
        __iter__(): Iterates over all key-value pairs in the hash table.
        __len__(): Returns the number of key-value pairs in the hash table.
        get_items(): Retrieves all key-value pairs as a list.
        get_keys(): Retrieves all keys in the hash table.
        get_values(): Retrieves all values in the hash table.
        visualize_hash_table(): Provides a visual representation of the hash table.
    """

    def __init__(self, size):
        """
        Initialize the hash table with a specified number of buckets.

        Args:
            size (int): The number of buckets in the hash table.
        """
        self.size = size
        self.n_items = 0
        self.array_buckets = [None for _ in range(size)]

    def _hash(self, key):
        """
        Compute the hash index for a given key.

        Args:
            key (any): The key to hash.

        Returns:
            int: The index of the bucket for the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert or update a key-value pair in the hash table.

        Args:
            key (any): The key to insert or update.
            value (any): The value associated with the key.
        """
        bucket_index = self._hash(key)
        if self.array_buckets[bucket_index] is None:
            self.array_buckets[bucket_index] = LinkedList_hash()
            self.array_buckets[bucket_index].insert_at_beginning((key, value))
            self.n_items = self.n_items + 1
        else:
            key_node = self.array_buckets[bucket_index].search_key_in_bucket(key)
            if key_node is not None:
                key_node.data = (key, value)  # Update existing key-value pair
            else:
                self.array_buckets[bucket_index].insert_at_beginning((key, value))
                self.n_items = self.n_items + 1

    def search(self, key):
        """
        Search for a key and return its value.

        Args:
            key (any): The key to search for.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        bucket_index = self._hash(key)
        if self.array_buckets[bucket_index] is None:
            print("This key doesn't have a corresponding bucket yet. Try an existing key!")
            return None
        key_node = self.array_buckets[bucket_index].search_key_in_bucket(key)
        if key_node is not None:
            return key_node.data[1]
        else:
            print("This key is not found in the buckets. Try an existing key!")
            return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.

        Args:
            key (any): The key to delete.

        Raises:
            KeyError: If the key is not found.
        """
        bucket_index = self._hash(key)
        if self.array_buckets[bucket_index] is None:
            raise KeyError("Key not found in the hash table.")
        bucket = self.array_buckets[bucket_index]
        bucket.delete_key(key)
        self.n_items = self.n_items - 1
        if bucket.size == 0:
            self.array_buckets[bucket_index] = None

    def load_factor(self):
        """
        Compute the load factor of the hash table.

        Returns:
            float: The load factor of the hash table.
        """
        return  len(ht) / self.size

    
    def resize(self, size=None):
        """
        Resize the hash table when the load factor exceeds the threshold.

        Args:
            size (int, optional): The new size of the hash table. Defaults to doubling the current size.
        """
        print("Resizing hash table...")
        old_array_buckets = self.array_buckets
        self.size = 2 * self.size if size is None else size
        self.array_buckets = [None for _ in range(self.size)]
        self.n_items = 0
        for bucket in old_array_buckets:
            if bucket is not None:
                current_node = bucket.head
                while current_node is not None:
                    key, value = current_node.data
                    self.insert(key, value)
                    current_node = current_node.pointer_to_next_node

    def __iter__(self):
        """
        Iterate over all key-value pairs in the hash table.

        Yields:
            tuple: Key-value pairs.
        """
        for bucket in self.array_buckets:
            if bucket is not None:
                current_node = bucket.head
                while current_node is not None:
                    yield current_node.data
                    current_node = current_node.pointer_to_next_node

    def __len__(self):
        """
        Return the number of key-value pairs in the hash table.

        Returns:
            int: The total number of key-value pairs.
        """
        return self.n_items
        

    def get_items(self):
        """
        Retrieve all key-value pairs as a list.

        Returns:
            list: A list of key-value pairs.
        """
        items = []
        for bucket in self.array_buckets:
            if bucket is not None:
                for item in bucket.to_python_list()[0]:
                    items.append(item)
        return items

        
    def get_keys(self):
        """
        Retrieve all keys in the hash table.

        Returns:
            list: A list of keys.
        """
        keys = []
        for bucket in self.array_buckets:
            if bucket is not None:
                for key in bucket.get_bucket_keys():
                    keys.append(key)
        return keys

    def get_values(self):
        """
        Retrieve all values in the hash table.

        Returns:
            list: A list of values.
        """
        values = []
        for bucket in self.array_buckets:
            if bucket is not None:
                for value in bucket.get_bucket_values():
                    values.append(value)
        return values

    def visualize_hash_table(self):
        """
        Provide a visual representation of the hash table.

        Returns:
            dict: A dictionary where keys are bucket indices and values are the contents of each bucket.
        """
        vis = {}
        for i, bucket in enumerate(self.array_buckets):
            if bucket is None:
                vis[f"bucket_{i}"] = ""
            else:
                vis[f"bucket_{i}"] = bucket.to_python_list()[0]
        return vis