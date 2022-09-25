class StringListClass:

    def __init__(self, size):
        self.str_list = ["''"] * size  # Creates empty list with 'size' elements
        self.index = 0  # To keep track of position within str_list

    def bbl_sort(self):
        bbl_sorted = self.str_list[:]  # We'll do our bubble sort on a new variable so that str_list remains unchanged

        index = 0
        r = []  # Creates empty list for range
        for i in bbl_sorted:
            r += [index]  # Adds range elements
            index += 1

        r = r[:index - 1]  # Removes last element from range

        for a in r:  # Perform 'range' iterations on bbl_sorted
            for i in r:  # For each iteration...
                if bbl_sorted[i] > bbl_sorted[i + 1]:  # If element is larger than element to its right...
                    bbl_sorted[i], bbl_sorted[i + 1] = bbl_sorted[i + 1], bbl_sorted[i]  # Swap the elements

        return bbl_sorted  # Returns bubble sorted list

    def add(self, new_item):
        try:  # Tries to add new item to str_list
            self.str_list[self.index] = str(new_item)
            self.index += 1  # Adjusts position within str_list
            return "String added successfully.\n"
        except IndexError:  # IndexError is raised if str_list is full
            return "No more strings can be added to this object.\n"

    def remove(self, target_item):
        count = 0
        for i in self.str_list:
            if i == target_item:
                count += 1  # Counts occurrences of target_item in str_list
        self.str_list = [s for s in self.str_list if s != str(target_item)]  # Writes over str_list without target_item
        self.str_list += ["''"] * count  # Adds the number of elements that were taken out
        self.index -= 1 * count  # Adjusts position within str_list

    def search(self, target_item):
        bbl_sorted = self.bbl_sort()  # Assigns bubble sorted list to a variable to avoid changing str_list
        for i in bbl_sorted:
            if target_item >= i:
                if target_item == i:
                    return True  # Returns true if match

        return False  # Returns false if the target item is less than a bbl_sorted item

    def __len__(self):
        n = 0
        for i in self.str_list:
            if i != "''":
                n += 1  # +1 to n for every non-blank element

        return n

    def __str__(self):
        s = "\n"
        for i in self.str_list:
            s += str(i) + '\n'  # Each item is string converted and then added to s, plus a new line

        return s
