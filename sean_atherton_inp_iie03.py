from collections import deque
import sys

shopping_list = deque([])

def greetings():
    sys.stdout.write("Enter your name please: ")
    username = sys.stdin.readline().strip()
    sys.stdout.write("\nWelcome " +str(username) + "\n") 
greetings()


def display_current_shopping_list():
    sys.stdout.write("These are the current items in your shopping list\n")
    sys.stdout.write(" " +str(shopping_list)+"\n")

    while(len(shopping_list)) < 0:
        sys.stdout.write("Would you like to add any other items to the list?: ")
        promt_additem_shopping_list = sys.stdin.readline().strip()
        if (prompt_additem_shopping_list == "yes"):
           return create_shopping_list()
        if (prompt_additem_shopping_list == "no"):
            sys.stout.write("\nThanks for shopping with us!")
        
    else:
        if(len(shopping_list)) > 0:
           return no_item_shopping_list()
display_current_shopping_list()

def no_item_shopping_list():
        sys.stdout.write("There aren't any items currently in your shopping list" +str(shopping_list))
        sys.stdout.write("\nDo you want to add some items to the list?\n")
        response_promt_add = sys.stdin.readline().strip()

        if(promt_no_itemlistadd != "yes") and (promt_no_itemlistadd != "no"):
            sys.stdout.write("Please awnser with either 'yes' or 'no' please!:" )
            promt_no_itemlistadd = sys.stdin.readline().strip()

        if (promt_no_itemlistadd == "yes"):
            start_creating_shopping()

        else:
            (promt_no_itemlistadd == "no")
            sys.stdout.write("tes")
no_item_shopping_list()










