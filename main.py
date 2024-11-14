def get_filename():
    input_file_name = input('What filename would you like to read?')
    return input_file_name

def read_file_to_list(filename):
    movie_table = []

    try:
        file = open(filename, "r")
        for line in file:
            row = line.split(',')
            row[4] = int(float(row[4])) # Convert worldwide gross to integer
            row[3] = int(float(row[3])) # Convert domestic gross to integer
            row[2] = int(float(row[2]))  # Convert movie budget to integer
            movie_table.append(row)

        file.close()  # Close the file after reading

    except FileNotFoundError:
        print("File doesn’t exist")

    return movie_table


def add_profit_column(movie_table):
    for row in movie_table:
        profit = row[-1]-row[-3]
        row.append(profit)

    return movie_table


def write_table_to_file(movie_table, filename):
    # Open the file for writing
    fd = open(filename, "a")

    # Write each item in the list to the file
    for row in movie_table:
        line = row.join(',')
        line += '\n'
        fd.write(line)



    # Close the file
    fd.close()

def find_highest_profit(movie_table):
    # Initialize the first actress as the youngest for comparison
    highest_row = movie_table[0]

    # Iterate through each actress record
    for row in movie_table:
        # Check if the current actress is younger than the current youngest
        if row[-1] < highest_row[-1]:  # Assuming age is at index 3
            highest_row = row

    # Return the data of the youngest actress
    return highest_row

def find_lowest_profit(movie_table):
    # Initialize the first actress as the youngest for comparison
    lowest_row = movie_table[0]

    # Iterate through each actress record
    for row in movie_table:
        # Check if the current actress is younger than the current youngest
        if row[-1] < lowest_row[-1]:  # Assuming age is at index 3
            lowest_row = row

    # Return the data of the youngest actress
    return lowest_row

def main():
    input_file_name = get_filename()
    movie_table = read_file_to_list(input_file_name)
    add_profit_column(movie_table)
    write_table_to_file(movie_table, 'movies_output.txt')
    highest_row = find_highest_profit(movie_table)
    print(f'The movie with the highest profit is {highest_row}')
    lowest_row = find_lowest_profit(movie_table)
    print(f'The movie with the highest profit is {lowest_row}')

main()
