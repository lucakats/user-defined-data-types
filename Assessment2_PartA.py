class StringClass:

    def __init__(self, str_value):
        self.str_data = []  # Creates empty list
        for i in str_value:
            self.str_data += [i]  # Adds each character as an element to the list

    def as_string(self):  # Used to return str_data as a string
        display = ""  # Creates empty string
        for i in self.str_data:
            display += i  # Adds each element of the list to the string
        return display

    def search(self, target_char):
        for i in self.str_data:  # Linear search algorithm
            if target_char == i:
                return True  # Returns 'True' if match
        return False  # Returns 'False' if no match

    def frequency(self, target_char):
        occ = 0  # Creates occurrence variable
        for i in self.str_data:
            if target_char == i:
                occ += 1  # +1 to occurrence for every match
        return occ

    def replace(self, target_char, new_char):
        index = -1  # Creates index variable
        for i in self.str_data:
            index += 1  # +1 to index for every item
            if target_char == i:
                self.str_data[index] = new_char  # Replaces item at index with new character

    def lowercase(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        lower = []  # Creates an empty list
        for i in self.str_data:
            if i in alphabet:  # If an item of str_data is found in alphabet...
                index = 25  # Sets index to beginning of lowercase letters for future retrieval
                for a in alphabet:
                    index += 1  # +1 to index for every letter searched
                    if i == a:
                        if index >= 52:  # Index will be >= 52 if the match was made to a lowercase letter
                            lower += i  # Adds original str_data item
                        else:
                            lower += alphabet[index]  # Adds lowercase converted str_data item
            else:
                lower += i
        self.str_data = lower  # Writes new list to 'str_data'

        return self.as_string()

    def uppercase(self):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper = []  # Creates an empty list
        for i in self.str_data:
            if i in alphabet:  # If an item of str_data is found in alphabet...
                index = 25  # Sets index to beginning of uppercase letters for future retrieval
                for a in alphabet:
                    index += 1  # +1 to index for every letter searched
                    if i == a:
                        if index >= 52:  # Index will be >= 52 if the match was made to an uppercase letter
                            upper += i  # Adds original str_data item
                        else:
                            upper += alphabet[index]  # Adds uppercase converted str_data item
            else:
                upper += i
        self.str_data = upper  # Writes new list to 'str_data'

        return self.as_string()

    def tokenize(self, delimiter):
        tokens = [[]]  # Creates tokens list
        for i in self.str_data:
            if i == delimiter:
                tokens += [[]]  # Adds an empty list for each delimiter; concludes with delimiter + 1 empty lists

        index = 0  # Creates index variable
        for i in self.str_data:
            if delimiter != i:
                tokens[index] += i  # Adds str_data item to a tokens list if item is not a delimiter...
            else:
                index += 1  # If delimiter, +1 to index to move to next tokens list

        # Removes empty token in case of a delimiter as an end character
        tokens = [t for t in tokens if t != []]

        return tokens

    def __eq__(self, compare):
        self.compare = compare  # Creating instance variable from argument
        return self.compare == self.str_data

    def __str__(self):
        return self.as_string()
