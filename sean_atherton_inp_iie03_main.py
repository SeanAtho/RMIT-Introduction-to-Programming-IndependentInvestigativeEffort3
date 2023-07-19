import sys

def main():

    
    sys.stdout.write("Welcome to the Shopping List application...\n")

    from collections import deque
   
    shopping_list = (["Bread","Milk","Toothpaste","Butter"])
    deque = shopping_list
    qty = [1, 1, 2, 2]

    sys.stdout.write("Enter your name please: ")
    username = sys.stdin.readline().strip()

    sys.stdout.write("\nWelcome " +str(username) + "\n")
    sys.stdout.write("\nPlease select from the following options to display current shopping list\n")
    sys.stdout.write("[a] Show Current Shopping List in Alphabetical Order\n")
    sys.stdout.write("[b] Show Current Shopping List in it's Default Order\n")
    response_to_sort = sys.stdin.readline().strip()

    if response_to_sort == "a":
        sys.stdout.write("\nThe Current Shopping List in Alphabetical Order\n")
        alpha_shopping_list = sorted(shopping_list)
        sys.stdout.write("\n "+str(alpha_shopping_list)+"\n")

    if response_to_sort == "b":
        sys.stdout.write("\n"+str(shopping_list)+"\n")

    sys.stdout.write("\nPlease enter a *SINGLE ITEM* to add to the shopping list: ")
    shopping_list_item = sys.stdin.readline().strip()

    
    sys.stdout.write("\nPlease enter a quantity of " +shopping_list_item+" \n")
    item_qty = int(sys.stdin.readline().strip())
    qty.append(item_qty)
    sys.stdout.write(str(item_qty)+" number of " +shopping_list_item+" have been added to the cart.\n")        

    if (len(shopping_list_item)) > 0:
        shopping_list.append(shopping_list_item)
        sys.stdout.write("\nYou added "+str(shopping_list_item)+" to the shopping list\n")
        sys.stdout.write("\nHere is the shopping list\n")
        sys.stdout.write("\n"+str(shopping_list)+"\n")
        shopping_list_item = ()
        sys.stdout.write("Is there anything else you would like to add? \nIf so simply type out the item, otherwise \nPress Enter to continue\n")
        shopping_list_item = sys.stdin.readline().strip()
        sys.stdout.write("Here is the first item in your shopping list "+shopping_list[0]+"\n")

    sys.stdout.write("Would you like to remove "+shopping_list[0]+" from the list?\n")
    sys.stdout.write("Please Anwser Yes or No: ")
    remove_item = sys.stdin.readline().strip()

    while remove_item != "Yes" and remove_item != "No":
        sys.stdout.write("Please Anwser Yes or No!\n")
        remove_item = sys.stdin.readline().strip()


    if remove_item == "Yes":
        sys.stdout.write("It was removed.\n")
        shopping_list.remove(shopping_list[0])

    else:
        sys.stdout.write("\nYou will now be given options of how you would like to view the list.\n")
        
    sys.stdout.write("\nPlease select from the following options to display the current shopping list\n")
    sys.stdout.write("[a] Show Current Shopping List in Alphabetical Order\n")
    sys.stdout.write("[b] Show Current Shopping List in it's Default Order\n")
    response_to_sort2 = sys.stdin.readline().strip()

    if response_to_sort2 == "a":
            sys.stdout.write("\nThe Current Shopping List in Alphabetical Order\n")
            alpha_shopping_list = sorted(shopping_list)
            sys.stdout.write("\n "+str(alpha_shopping_list)+"\n")

    if response_to_sort2 == "b":
            sys.stdout.write("\n"+str(shopping_list)+"\n")
            
    sys.stdout.write("\nThanks "+username+" for shopping with us :)\n")

main()

    
    

