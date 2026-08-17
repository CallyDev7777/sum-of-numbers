## Task

## To ask for users input and add them together

def Main():
    print("Welcome to the sum of numbers function!")
    print("Please enter as many numbers as you want, when you want the function to stop, please say 'quit'!")
    print("If you would like to undo the previous input, please say 'undo'!")
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