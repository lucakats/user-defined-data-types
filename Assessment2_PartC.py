import os

from Assessment2_PartA import StringClass  # Importing StringClass class
from Assessment2_PartB import StringListClass  # Importing StringListClass class


def cls():  # Defining function for clearing screen
    os.system('cls' if os.name == 'nt' else 'clear')


def state(fruit, sweet):  # Defining function for printing current state of objects
    print("Current state of objects: \n")
    print("(1) 'fav_fruit' = " + str(fruit))
    print("(2) 'fav_sweet' = " + str(sweet) + '\n')


cls()
input("This program will demonstrate the functionality of the StringClass and StringListClass classes." + '\n' +
      "Please hit enter at each step to continue...")

cls()
input("Let's first create an instance of the StringClass class. Objects of this class simply handle a single string. "
      "We'll name the object 'fav_fruit' and pass the string 'Banana' as the argument...")
fav_fruit = StringClass("Banana")  # Creating first instance of StringClass class
input("We can print the object...")
print(str(fav_fruit))

input("\nHow about another. This one will be called 'fav_sweet'. We'll also print it...")
fav_sweet = StringClass("Jelly Beans")  # Creating second instance of StringClass class
print(str(fav_sweet))

input("\nWe have now created two StringClass instances, 'fav_fruit' and 'fav_sweet'. Now we can demonstrate "
      "the methods of the objects...")

cls()
search = input("The search method looks for a specific character in the string and returns either True or False "
               "depending on its appearance.\n\nPlease enter a character here: ")
# Testing the 'search' method of StringClass
print("The character '" + search + "' appears in " + str(fav_fruit) + ": " + str(fav_fruit.search(search)))
print("The character '" + search + "' appears in " + str(fav_sweet) + ": " + str(fav_sweet.search(search)))

search = input("\nOne more time. Please enter a character: ")
print("The character '" + search + "' appears in " + str(fav_fruit) + ": " + str(fav_fruit.search(search)))
print("The character '" + search + "' appears in " + str(fav_sweet) + ": " + str(fav_sweet.search(search)))

input("\nNext up is the frequency method...")

cls()
freq = input("The frequency method returns the occurrence of a specific character in the string. "
             "Please enter a character here: ")
# Testing the 'frequency' method of StringClass
print("The character '" + freq + "' appears in " + str(fav_fruit) + " " + str(fav_fruit.frequency(freq)) +
      " times.")
print("The character '" + freq + "' appears in " + str(fav_sweet) + " " + str(fav_sweet.frequency(freq)) +
      " times.")

freq = input("\nOne more time. Please enter a character: ")
print("The character '" + freq + "' appears in " + str(fav_fruit) + " " + str(fav_fruit.frequency(freq)) +
      " times.")
print("The character '" + freq + "' appears in " + str(fav_sweet) + " " + str(fav_sweet.frequency(freq)) +
      " times.")

input("\nAnother method for our StringClass objects is the replace method...")

cls()
print("The replace method allows us to replace every occurrence of a target character with a new character.\n")
target = input("For our 'fav_sweet' object (Jelly Beans), please enter a target character: ")
new = input("Enter a replacement character to print the new string: ")
fav_sweet.replace(target, new)  # Testing the 'replace' method of StringClass
print(str(fav_sweet))

input("\nNext we will demonstrate the lowercase method...")

cls()
while True:
    state(fav_fruit, fav_sweet)
    lower = input("The lowercase method simply converts all alphabet in the string to lowercase. "
                  "Please enter the number of the object you would like to apply the lowercase method to: ")
    if lower == "1":
        print(fav_fruit.lowercase())  # Applying the 'lowercase' method to 'fav_fruit'
        break
    elif lower == "2":
        print(fav_sweet.lowercase())  # Applying the 'lowercase' method to 'fav_sweet'
        break
    else:
        cls()
        print("Please enter a valid number.\n")
        continue

input("\nSimilarly, we have the uppercase method...")

cls()
while True:
    state(fav_fruit, fav_sweet)
    lower = input("Please enter the number of the object you would like to apply the uppercase method to: ")
    if lower == "1":
        print(fav_fruit.uppercase())  # Applying the 'uppercase' method to 'fav_fruit'
        break
    elif lower == "2":
        print(fav_sweet.uppercase())  # Applying the 'uppercase' method to 'fav_sweet'
        break
    else:
        cls()
        print("Please enter a valid number.\n")
        continue

input("\nNext up is the tokenize method...")

cls()
print("The tokenize method allows us to split the string based on a specific delimiter.\n")
print("'fav_fruit': " + str(fav_fruit))
delimiter = input("\nPlease enter a delimiter for this object: ")
print("Tokens: " + str(fav_fruit.tokenize(delimiter)))  # Tokenizing 'fav_fruit'
print("\n'fav_sweet': " + str(fav_sweet))
delimiter = input("\nAnd for our other object: ")
print("Tokens: " + str(fav_sweet.tokenize(delimiter)))  # Tokenizing 'fav_sweet'
input("\nLast up is the overloaded equal method...")

cls()
print("Overloading the method  __eq__ can be helpful to check whether the contents of two objects are the same.")
input("\nHit enter to compare our two objects...")
print(str(fav_fruit == fav_sweet) + '\n')  # Applying 'equal' method to the two existing objects
print("We can also compare a string of your choice with our 'fav_fruit' object (" + str(fav_fruit) + ").")
eq_string = StringClass(input("Enter your string here: "))  # Creating new StringClass object 'eq_string'
print(fav_fruit == eq_string)  # Applying 'equal' method to 'fav_fruit' and 'eq_string'

input("\nHit enter to continue...")

cls()
print("We can now explore the functionality of our StringListClass class. Objects of this class are built to handle "
      "a collection of strings in an array-based structure. We can perform multiple methods on these objects as well.")
while True:
    try:
        size = int(input("\nLet's create our StringListClass object. Please set the size of the array: "))
    except ValueError:  # If input is not a valid number...
        cls()
        print("Please enter a valid number.")
        continue
    else:
        if 5 <= size <= 10:  # If input is between 5 and 10 inclusive, then it is accepted
            break
        else:
            cls()
            print("For the purpose of this program please enter an array size between and 5 and 10 (inclusive).")
            continue

my_list = StringListClass(size)  # Creating my_list instance of StringListClass class
input("\nObject created. Now let's add some strings to the array with the add method...")

cls()
input("We can start by adding our two existing StringClass objects. Let's also print the array...")
# Adding StringClass objects to my_list
my_list.add(fav_sweet)
my_list.add(fav_fruit)
print(my_list)

input("We should fill up the array with strings...")

cls()
items = size - 2
while items > 0:  # Adding the remaining number of elements to my_list
    print(my_list.add(input(str(items) + " space(s) left. Enter a string to add: ")))
    items -= 1

input("Our array is now full. If we try to add another string, say 'Python', we get...")
print(my_list.add("Python"))  # Demonstrating what happens when my_list object is full

input("Now that we have a full array, let's demonstrate the remove method of this object...")

cls()
print("We can remove an item from the array using the remove method. You just need to enter in the string "
      "exactly as it is.")
print(my_list)
my_list.remove(input("Enter the string you would like to remove: "))  # Applying the 'remove' method
print(my_list)
my_list.remove(input("One more try: "))  # Applying the 'remove' method again
print(my_list)

input("We should also now test the overloaded __len__ method. This will tell us how many strings are in the current "
      "array...")
print(len(my_list))  # Printing the number of non-empty elements in the my_list object

input("\nFinally, we have our search method...")

cls()
print("Similar to that of the StringClass class, the search method will return a true or false statement after it has "
      "searched for a string in the array.\nThe array is first sorted using a bubble sort. The search will then be "
      "performed linearly.")
print(my_list)
print(my_list.search(input("Enter a string to search for: ")))  # Applying the 'search' method
print(my_list.search(input("\nOne more time: ")))  # Applying the 'search' method again

input("\nThat completes all demonstrations for both our StringClass and StringListClass classes. Thank you...")
