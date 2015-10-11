def read_num_names():
    '''
    :return: prompt the user for the number of names to be read
    '''
    pass

def read_names(num_names):
    '''
    :param num_names: the number of names to read
    :return: prompt the user to enter a name in the specified format
    '''
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