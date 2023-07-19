from collections import deque
import sys

shopping_list = deque (["Bread","Milk","Toothpaste","Butter"])

#Prompt for user to enter their name 
sys.stdout.write("Enter your name please: ")
username = sys.stdin.readline().strip()

#Welcome message with the users inputted name
sys.stdout.write("\nWelcome " +str(username) + "\n")


def additem():
    '''This adds an item the user entered and adds it to the list,
       after that it displays the list with the added item'''
    sys.stdout.write("\nPlease enter a item to add to the shopping list: ")
    shopping_list_item = sys.stdin.readline().strip()

#If the user enters something with a length which is
#greater than 0 it will add it to the list.
    while (len(shopping_list_item)) > 0:
        shopping_list.append(shopping_list_item)

#Displays the current shopping list alongwith the inputted additional items
        sys.stdout.write("This is your current shopping list\n")
        sys.stdout.write("\n"+str(shopping_list)+"\n")

#Allows the program to assign the new input to the (shopping_list_item) variable
        shopping_list_item = ()
        sys.stdout.write("Is there anything else you would like to add? Press Enter to continue")
        shopping_list_item = sys.stdin.readline().strip()

#Displays to the user the first item in their shopping list
        sys.stdout.write("Here is the first item in your shopping list "+shopping_list[0]+"\n")
additem()
'''Executes the above (additem) function'''

#Asks the user if they would like to remove the first item in the list with a
#"Yes" or "No" question.
sys.stdout.write("Would you like to remove "+shopping_list[0]+" from the list?\n")
sys.stdout.write("Please Anwser Ye or No: ")
remove_item = sys.stdin.readline().strip()

#If the user doesnt enter the correct response to either of the options
#they will be asked to do so again.
while remove_item != "Yes" and remove_item != "No":
    sys.stdout.write("Please Anwser Yes or No!\n")
    remove_item = sys.stdin.readline().strip()

#If the user enters "Yes" they will be given a indication that the first item in the
#list was removed.
if remove_item == "Yes":
    sys.stdout.write("It was removed.\n")
    shopping_list.remove(shopping_list[0])

#In the event they enter anything else they will simiply be displayed the current
#shopping list which includes the changes they made.
else:
    sys.stdout.write("Here is your shopping list\n")
    sys.stdout.write("\n"+str(shopping_list)+"\n")

#Final sys write message to the user showing them one last time the list of items
sys.stdout.write("Thanks "+username+" for shopping with us, this is your current shopping list:\n")
sys.stdout.write("\n"+str(shopping_list)+"\n")

    
    

