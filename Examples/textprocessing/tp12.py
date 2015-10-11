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

class NameParseError(Exception):
    pass

def parse_name(value):
    '''
    :param name: the value to be parsed according to the specified format
    :return: return a valid name or raise an exception
    '''
    if not ',' in value:
        raise NameParseError
    else:
        return value

def read_names(num_names):
    '''
    :param num_names: the number of names to read
    :return: prompt the user to enter a name in the specified format: last, first
    '''
    names = []
    num_mistakes = 0

    for i in range(num_names):
        result = input("Please enter name {}: ".format(i))

        # Let's take a similar approach to parsing the name as was done for the integer
        try:
            # Whatever result comes from the user will be passed to our parse_name function and return either a
            # valid name or will raise an exception
            name = parse_name(result)
        except NameParseError:
            # Per the requirements, if the input format is incorrect, we report it and fix it
            num_mistakes += 1
            print(">> Wrong format ... should be 'Last, First'.")
            print(">> You have done this {} time(s) already.  Fixing input ...".format(num_mistakes))

            first, last = result.split(' ')
            name = "{}, {}".format(last, first)

        names.append(name)

    return names

def display_names(names, ascending = True):
    '''
    :param names: a list of names to be displayed
    :param direction: the direction of display: ascending or descending
    :return: None
    '''
    # Q: How to handle direction?  Ascending vs Descending?
    # A: Sort accepts a reverse parameter whose default is False (or ascending)
    names.sort(reverse=not ascending)
    for name in names:
        print("\t{}".format(name))

def main():
    # Prompt for number of names in list
    num_names = read_num_names()

    # Prompt for names
    names = read_names(num_names)

    # Display names sorted
    print("Displaying names sorted (ascending)")
    display_names(names)


    print("Displaying names sorted (descending)")
    display_names(names, False)


if __name__ == "__main__":
    main()