
def read_file_to_list(filename):
    movie_table = []

    try:
        file = open(filename, "r")
        for line in file:
            row = line.split(',')
            row[-1] = int(row[-1])  # Convert worldwide gross to integer
            row[-2] = int(row[-2])  # Convert domestic gross to integer
            row[-3] = int(row[-3])  # Convert movie budget to integer
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


def write_list_to_file(movie_table, filename):
    # Open the file for writing
    fd = open(filename, "a")

    # Write each item in the list to the file
    for row in movie_table:
        fd.write(str(row) + ',')

    # Close the file
    fd.close()

def main():
    input_file_name = input('')
    movie_table = read_file_to_list(input_file_name)
    add_profit_column(movie_table)
    output_file_name = input('')
    write_list_to_file(movie_table, output_file_name)