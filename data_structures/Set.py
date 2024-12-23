from data_structures.Hash_Table import hash_table

class Set(hash_table):
    
    def __init__(self, size=8):
        super().__init__(size)

    def add(self, element):
        """Add an element to the set."""
        if self.load_factor() > 0.75:  # Resize if load factor exceeds threshold
            self.resize()
        self.insert(element, None)  # Use None as the value


    def remove(self, element):
        """Remove an element from the set."""
        self.delete(element)

    def search(self, element):
        """
        Search for an element in the set.

        Args:
            element (any): The element to search for.

        Returns:
            any: The element if found.
        """
        bucket_index = self._hash(element)
        if self.array_buckets[bucket_index] is None:
            print("This key doesn't have a corresponding bucket yet. Try an existing key!")
            return None
        key_node = self.array_buckets[bucket_index].search_key_in_bucket(element)
        if key_node is not None:
            return key_node.data[0]
        else:
            print("This key is not found in the buckets. Try an existing key!")
            return None
    
    def __contains__(self, element):
        """Check if an element exists in the set."""
        return self.search(element) is not None

    def union(self, other_set):
        """Return a new set with elements from this set and another."""
        result = Set()
        for item in self.get_keys():
            result.add(item)
        for item in other_set.get_keys():
            result.add(item)
        return result

    def intersection(self, other_set):
        """Return a new set with elements common to both sets."""
        result = Set()
        for item in self.get_keys():
            if item in other_set:
                result.add(item)
        return result

    def difference(self, other_set):
        """Return a new set with elements in this set but not in the other."""
        result = Set()
        for item in self.get_keys():
            if item not in other_set:
                result.add(item)
        return result

    def __iter__(self):
        """Iterate over all elements of the set."""
        for bucket in self.array_buckets:
            if bucket is not None:
                current_node = bucket.head
                while current_node is not None:
                    yield current_node.data[0]
                    current_node = current_node.pointer_to_next_node