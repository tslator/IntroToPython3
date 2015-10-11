column_spacing = 20
payment_num_col_width = 10
payment_col_format_width = 10
balance_col_format_width = 10
currency_precision = 2
payment_data_width = 5
balance_data_width = 6


column = ' ' * column_spacing

# Explanation of the formatting:
#   {:^%d}
#    || |___ Integer placeholder for column width specified in payment_num_col_width.  'Old' style format helps to not hardcode the value
#    ||_____ Center the column data
#    |______ Replacement field Separator required by Python
payment_num_col_format = '{:^%d}' % (payment_num_col_width)
payment_col_format = '{:^%d}' % (payment_col_format_width)
balance_col_format = '{:^%d}' % (balance_col_format_width)

payment_data_precision = currency_precision
balance_data_precision = currency_precision

# Creates a string from the payment/balance values that includes the '$' so that the entire string can be centered in the
# column.
#
#  Explanation of the formatting
#   ${:%d.%df}
#   | | || ||__ Indicates to display value as floating point.  Note, without 'f', Python uses scientific notation by default
#   | | || |___ Integer placeholder for precision.  'Old' style format helps to not hardcode the value
#   | | ||_____ Decimal point
#   | | |______ Integer placeholder for minimum field width
#   | |________ Format spec separator
#   |__________ Character literal to be included in the final string
payment_format_str = '${:%d.%df}' % (payment_data_width, payment_data_precision)
balance_format_str = '${:%d.%df}' % (balance_data_width, balance_data_precision)

row_format = payment_num_col_format + column + payment_col_format + column + balance_col_format

def main():
    num_payment = 0
    balance = float(input("Enter opening balance: "))
    payment = float(input("Enter monthly payment: "))

    # Print the table header
    print("")
    print("")
    print(row_format.format("", "Amount", "Remaining"))
    print(row_format.format("Pymt#", "Paid", "Balance"))

    # Calculate and print the payment number, payment, and balance
    while balance > 0:
        payment_str = payment_format_str.format(payment)
        balance_str = balance_format_str.format(balance)
        print(row_format.format(num_payment, payment_str, balance_str))
        balance = balance - min(balance, payment)
        num_payment += 1

    payment_str = payment_format_str.format(payment)
    balance_str = balance_format_str.format(balance)
    print(row_format.format(num_payment, payment_str, balance_str))


if __name__ == "__main__":
    main()