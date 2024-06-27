class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 1 # size of the array
        self.size = 0 # total no. of ele in the array
        self._array = [None] * self._capacity # the array

    def _resize(self) -> None:
        """
        Internal method to double the size of the array and copy elements over
        :return: None
        """
        # to resize we need to do a few things:
        # 1. update the capacity
        # 2. update the array

        ## Point 1 ##
        new_capacity = self._capacity * 2
        self._capacity = new_capacity

        ## Point 2 ##
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self._array[i]
        self._array = new_array


    def append(self, item) -> None:
        """
        Public method that inserts a new item at the end of the array
        :param: Item to add to the end of the array
        """
        # checking if current size is at the capacity limit
        if self.size == self._capacity:
            self._resize()

        # append the item at the end of the array
        self._array[self.size] = item
        # update the size of the array
        self.size += 1
        
    def insert(self, item, index) -> None:
        """
        Public method to insert an item at a specific index in the array
        :param item: element to place into the array
        :param index: position to put the element in the array
        """
        # when inserting we need to push all the elements from i onwards to the right
        
        # checking if current size is at the capacity limit
        if self.size == self._capacity:
            self._resize()

        # Logic: 
        # 1. create a new array with the same capacity
        # 2. copy over the elements from the old array
        # 3. shift the elements on the right of the index to the right by one
        new_arr = [None] * self._capacity
        for i in range(self.size + 1):
            if i < index:
                new_arr[i] = self._array[i]
            elif i == index: 
                new_arr[i] = None
            else:
                new_arr[i] = self._array[i-1]
        new_arr[index] = item
        self._array = new_arr
        self.size += 1

    def remove(self, index) -> None:
        """
        Public method to remove the element at the index
        :param index: position of the element that user wants to remove
        :return: None
        """
        if self.size == self._capacity:
            self._resize()
        
        new_arr = [None] * self._capacity
        # remove logic
        # the items on the left side of the index remains the same
        # the items on the right of the index must move back one position
        for i in range(self.size + 1):
            if i < index:
                new_arr[i] = self._array[i]
            elif i == index:
                new_arr[i] = None
            else:
                new_arr[i-1] = self._array[i]
        self._array = new_arr
        self.size -= 1
    
    def __str__(self) -> str:
        """Return a string representation of the array."""
        return str([self._array[i] for i in range(self.size)])


# Example usage
dynamic_array = DynamicArray()
print(dynamic_array)  # Output: []

dynamic_array.append(1)
dynamic_array.append(2)
print(dynamic_array)  # Output: [1, 2]

dynamic_array.append(3)
print(dynamic_array)  # Output: [1, 2, 3]

dynamic_array.insert(4, 0)
print(dynamic_array)

dynamic_array.insert(4, 2)
print(dynamic_array)

dynamic_array.insert(4, 5)
print(dynamic_array)

dynamic_array.remove(2)
print(dynamic_array)

dynamic_array.remove(0)
print(dynamic_array)

dynamic_array.remove(3)
print(dynamic_array)