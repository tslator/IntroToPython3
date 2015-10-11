def main():
    # Prompt for number of names in list
    num_names = read_num_names()

    # Prompt for names
    names = read_names(num_names)

    # Display names sorted
    print("Displaying names sorted (ascending)")
    display_names_ascending(names)


    print("Displaying names sorted (descending)")
    display_names_descending(names)


if __name__ == "__main__":
    main()