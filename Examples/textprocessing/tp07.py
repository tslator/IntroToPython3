def parse_int(value):
    '''
    :param value: the value to be converted into an integer
    :return: a valid integer or None
    '''
    try:
        return int(value)
    except ValueError:
        return None

def read_num_names():
    '''
    :return: a valid integer
    '''
    valid_name = False
    result = None
    while not valid_name:
        result = parse_int(input("Enter total number of names: "))
        if result:
            valid_name = True
        else:
            print("That was not a number.  Try again.")

def read_names(num_names):
    '''
    :param num_names: the number of names to read
    :return: prompt the user to enter a name in the specified format: last, first
    '''
    # Q: How do be detect that the correct format has been used?
    # Q: What should we do if it isn't correct?
    names = []
    for i in range(num_names):
        result = input("Please enter name {}: ".format(i))

        #---------------------------------------------------------------------
        # Note: We need to implement the requirements for handling errors here
        #---------------------------------------------------------------------

        names.append(result)

    return names

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