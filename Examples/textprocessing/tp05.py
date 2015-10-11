def read_num_names():
    '''
    :return: prompt the user for the number of names to be read
    '''
    # Q: What happens if the user doesn't enter an legal integer?
    # A: Input validation should be done as close to the input as possible
    # Q: What is a legal integer?  How do we detect when its not?

    try:
        num_names = int(input("Enter total number of names: "))
    except ValueError as ve:
        print("{} is not a legal number".format(ve))
        return None

    # Note: The above will return a valid number or None which isn't of much help to the caller

def read_names(num_names):
    '''
    :param num_names: the number of names to read
    :return: prompt the user to enter a name in the specified format: last, first
    '''
    # Q: How do be detect that the correct format has been used?
    # Q: What should we do if it isn't correct?
    pass

def display_names(names, direction):
    '''
    :param names: a list of names to be displayed
    :param direction: the direction of display: ascending or descending
    :return: None
    '''
    pass

def main():
    # Prompt for number of names in list
    num_names = read_num_names()

    # Prompt for names
    names = read_names(num_names)

    # Display names sorted
    print("Displaying names sorted (ascending)")
    display_names(names, direction=ascending)


    print("Displaying names sorted (descending)")
    display_names(names, direction=descending)


if __name__ == "__main__":
    main()