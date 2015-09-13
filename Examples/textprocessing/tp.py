def main():
    names = []
    num_mistakes = 0

    # Prompt for number of names in list
    num_names = int(input("Enter total number of names: "))

    # Prompt for each name
    for i in range(num_names):
        name = input("Please enter name {0}: ".format(i))
        if not ',' in name:
            num_mistakes += 1
            print(">> Wrong format... should be Last, First.")
            print(">> You have done this {0} time(s) already.  Fixing input...".format(num_mistakes))

            first, last = name.split(' ')
            name = "{0}, {1}".format(last, first)

        names.append(name)

    # Print sorted list
    print("The sorted list (by last name) is:")
    names.sort()
    for name in names:
        print("\t{0}".format(name))


if __name__ == "__main__":
    main()