column_spacing = 10
column = ' ' * 4
payment_num_col_format_str = '{0:^5s}'
payment_num_col_format_dec = '{0:^5d}'
payment_col_format_str = '{1:^7s}'
balance_col_format_str = '{2:^9s}'

payment_format_str = '${0:5.2f}'
balance_format_str = '${0:6.2f}'

header_row = payment_num_col_format_str + column + payment_col_format_str + column + balance_col_format_str
payment_row = payment_num_col_format_dec + column + payment_col_format_str + column + balance_col_format_str

def main():
    num_payment = 0
    balance = float(input("Enter opening balance: "))
    payment = float(input("Enter monthly payment: "))

    # Print the table header
    print("")
    print("")
    print(header_row.format("", "Amount", "Remaining"))
    print(header_row.format("Pymt#", "Paid", "Balance"))

    # Calculate and print the payments and balance
    payment_str = payment_format_str.format(payment)
    balance_str = balance_format_str.format(balance)
    print(payment_row.format(num_payment, payment_str, balance_str))

    while balance >= payment:
        balance -= payment
        num_payment += 1
        payment_str = payment_format_str.format(payment)
        balance_str = balance_format_str.format(balance)
        print(payment_row.format(num_payment, payment_str, balance_str))

    if balance > 0:
        payment_str = payment_format_str.format(balance)
        balance_str = balance_format_str.format(balance-balance)
        print(payment_row.format(num_payment, payment_str, balance_str))


if __name__ == "__main__":
    main()