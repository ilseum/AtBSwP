def print_table(table):
    num_rows = len(table[0])
    num_columns = len(table)
    col_widths = [len(max(row, key=len)) for row in table]

    for row in range(num_rows):
        for column in range(num_columns):
            print(table[column][row].rjust(col_widths[column]), end=" ")
        print()


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == "__main__":
    main()
