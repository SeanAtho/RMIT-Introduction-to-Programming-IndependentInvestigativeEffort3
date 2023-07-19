import sys

def main():
    """Introduction the the shopping list program and menus. Starts by
    defining all the functions."""

    sys.stdout.write("Welcome to the Shopping List application...\n")

    from collections import deque
   
    shopping_list = ["Bread","Milk","Toothpaste","Butter"]
    shopping_list_quantities = [2, 2, 1, 2]

    # Username variable gives indication of which profile they are on.
    sys.stdout.write("Enter your name please: ")
    username = sys.stdin.readline().strip()
    
    # Alternative to multiptable writes which cleans up code this is
    # also easier to keep track of aswell when displaying text/interfaces
    # to user.
    #
    # Each is displayed on a new line to make it clearer to the user what
    # the options they have to choose from are. 
    menu=""
    menu+="\nMain Menu for Shopping list\n"
    menu+="===========================\n"
    menu+="Welcome " +str(username) + "\nWhat would you like today?\n\n"
    menu+="Enter [a] to display the shopping list\n"
    menu+="Enter [b] to add a item to the shopping list\n"
    menu+="Enter [c] to remove item from list\n"
    menu+="[L]eave\n"
    menu+="\n"
    menu+="Enter Option: "

    sys.stdout.write(menu)
    
    # Whatever the user inputs is assigned to the variable which is given
    # the below name as a indication that refering to the main options
    # they are given at the start of the program. 

    option_selection = sys.stdin.readline().strip().lower()

    # If user selects inputs the desired input they will be directed down
    # the relevant path, this will end with them returning to the original
    # main menu print were they can start the proccess again or select
    # another option.
    #
    # Having them each of the options on its own 'branch' with the ablity
    # to return back to the start means they arent cut off from any of the
    # options if they make a change of move forward.
    while (option_selection != "L"):
        sys.stdout.write("\n\n")

        if (option_selection == "b"):
            sys.stdout.write("\n")
            sys.stdout.write("Enter a item to add\n")
    # Once they enter a item they would like to add its again given to the
    # approapelty named variable which is presented back to them when they
    # enter the amount of the said item, these are both added to the end
    # of the shopping list and are thus in the correct order.
    #
    # This remains the same for the removal of all items as well.
            shopping_item = sys.stdin.readline().strip()
            sys.stdout.write("Enter item amount of "+shopping_item+": \n")
            shopping_item_amount = int(sys.stdin.readline())

    # prevent the user from entering a negative number and indicates
    # they need to enter a postive number, this proccess is contained
    # in a loop which stops them from progressing.
            while (shopping_item_amount<0):
                sys.stdout.write("Please enter a postive number for the amount\n")
                shopping_item_amount = int(sys.stdin.readline())
            shopping_list.append(shopping_item)
            shopping_list_quantities.append(shopping_item_amount)

    # The user will be given the option to remove the first item in the list,
    # Although this is limiting in this scenario of having a pre-made shopping
    # list I believe accounting for the possiblity of the user removing all the
    # items in the list to be one that would almost be somewhat unrealistic.
    # They would more than likely be using another program if they wanted to
    # the ablity to perform that action. 
        if (option_selection == "c"):
            sys.stdout.write("Would you like to remove " +str(shopping_list[0])+": " +str(shopping_list_quantities[0])+"? "
                             "Yes or No\n")
            remove_item_response = sys.stdin.readline().strip()
    # While loop is created for a yes, no or none scenario meaning the user will need
    # to enter the correct input in order to remove the first item. This prevents
    # or atleasts attempts to mitagate a scenario where there is a mis-input
    # from the user. 
            while (remove_item_response == "Yes"):
                sys.stdout.write("The item " +str(shopping_list[0])+": " +str(shopping_list_quantities[0])+" has been removed\n")
                shopping_list.remove(shopping_list[0])
                shopping_list_quantities.remove(shopping_list_quantities[0])
                sys.stdout.write("Please Press Enter to Return to Menu\n")

                if (remove_item_response == "No"):
                    sys.stdout.write("We wont remove " +str(shopping_list[0])+": " +str(shopping_list_quantities[0])+" from the list\n")

                elif (remove_item_response != "Yes" and remove_item_response != "No"):
                    sys.stdout.write("Please enter either Yes or No\n")
                remove_item_response = sys.stdin.readline().strip() 

        elif (option_selection == "a"):
            sys.stdout.write("Display Shopping List\n")
            sys.stdout.write("\n"+str(shopping_list)+": ")
            sys.stdout.write(str(shopping_list_quantities)+"\n")

    # If the user enters a invalid input from the desired one they are presented with
    # a write statement indicating they need to try again. After this is given to them
    # they are presetented the original menu and their next input is assigned and the
    # proccess starts again allowing them to go back to the start. 
            
        else:
            sys.stdout.write("Please enter a valid input")
        sys.stdout.write(menu)
        option_selection = sys.stdin.readline().strip().lower()
main()
"""Call to main"""

    
    

