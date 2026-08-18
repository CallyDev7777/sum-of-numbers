## Task

## To ask for users input and add them together

def Main():
    print("Welcome to the sum of numbers function!")
    print("Current command list:\n" \
    " quit = forces the loop to end and return the result\n" \
    " undo = removes the last number entered and returns it for user validation\n" \
    " list = prints all current numbers held within the list\n")
    numb_list = []
    askInput(numb_list)
    print("Total number sum is... ", sum_of_inputs(numb_list), " with a valid counter of ...", len(numb_list) , "!")

    


def askInput(numb_list):
    while True:
        print("---------------------------------")
        x = input("Please enter a number: ")
        if x.lower() == "quit":
            break
        elif x.lower() == "undo":
            if numb_list:
                removed = numb_list.pop()
                print(removed, "has been removed from the list!")
            else:
                print("Nothing to undo!")
        elif x.lower() == "list":
            if numb_list:
                print(numb_list)
            else:
                print("list of numbers is empty! Please input at least one integer before using list")
        elif not x.isdigit():
            print("Please enter integers only!")
        else:
            numb_list.append(x)


def sum_of_inputs(numb_list):
    total_list = 0
    for x in numb_list:
        total_list += int(x)
    return total_list



Main()