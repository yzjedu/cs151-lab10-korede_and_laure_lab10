# Programmers:  Laure Patera and Korede Oni
# Course:  CS151, Dr. Zee
# Due Date: 11/21/24
# Lab Assignment:  Lab 10
# Problem Statement: analyze data on movies, their budgets, and their profits, creating a new file to update movies.csv with new values and make certain values searchable
# Data In: input_filename (which file the user would like the program to read), output_filename (which file the user would like the program to write to)
# Data Out: data for movie with the highest profit, data for movie with the lowest profit, outfile (.csv file, updated version of movies.csv)
# Credits: Codes from our class repository and the readme file
# Input Files: must be .csv, movies.csv expected



# Purpose: get user input of which file to read
# Parameters: none
# Return: input_filename, string, represents name of the file that will be read
def get_input_filename():
    #asks user which file they would like to read
    input_filename = input('What filename would you like to read?')
    return input_filename


# Purpose:  reads the file to a list
# Parameters: filename, string, the name of the file that will be read
# Return: movie_table, table, table of data for each movie from the file
def read_file_to_list(filename):
    #creates empty table
    movie_table = []
    #Tries to open file for reading and adds each line of the file to movie_table
    try:
        file = open(filename, "r")
        for line in file:
            row = line.split(',')
            movie_table.append(row)
            row[4] = int(float(row[4]))  # Convert worldwide gross to integer
            row[3] = int(float(row[3]))  # Convert domestic gross to integer
            row[2] = int(float(row[2]))  # Convert movie budget to integer

        file.close()  # Close the file after reading

    #If there is an error because the file does not exist, tell the user
    except FileNotFoundError:
        print("File doesn’t exist")

    # return the data of movie_table
    return movie_table


# Purpose: get user input of which file to write to
# Parameters: none
# Return: output_filename, string, represents name of the file that will be created and written to
def get_output_filename():
    #asks user which file they would like to write to
    output_filename = input('What is the name of the file you would like to output?')
    return output_filename


# Purpose:  writes the table to a new file
# Parameters: movie_table (table, table of data from each movie), output_filename (string, name of file that will be created where the data will be written)
# Return: none
def write_table_to_file(movie_table, output_filename):
    # Open the file for writing
    outfile = open(output_filename, "w")

    for row in movie_table:
        #create row for profit, and calculate it by international gross minus the budget
        profit = row[-1] - row[-3]
        row.append(profit)
        line = ''
        # Write each item in the table to the file
        for item in row:
            line += str(item) + ','
        outfile.write(line + '\n')

    # Close the file
    outfile.close()


# Purpose: finds which movie has the highest profit
# Parameters: table (table, which table to find the highest profit from)
# Return: highest_row (string, which row has the highest profit)
def find_highest_profit(table):
    # Initialize the first row as the highest profit for comparison
    highest_row = table[0]

    # Iterate through each movie record
    for row in table:
        # Check if the current movie has a higher profit than the current highest
        if row[-1] > highest_row[-1]:  # Assuming profit is at index -1
            highest_row = row

    # Return the data of the highest row
    return highest_row


# Purpose:  finds which movie has the lowest profit
# Parameters: table (table, which table to find the lowest profit from)
# Return: lowest_row (string, which row has the lowest profit)
def find_lowest_profit(table):
    # Initialize the first row as the lowest profit for comparison
    lowest_row = table[0]

    # Iterate through each movie record
    for row in table:
        # Check if the current movie has a lower profit than the current lowest
        if row[-1] < lowest_row[-1]:  # Assuming profit is at index -1
            lowest_row = row

    # Return the data of the lowest row
    return lowest_row


# Purpose:  main function
# Parameters: none
# Return: none
def main():

    #Output welcome message and purpose of the program
    print('Welcome! This program analyzes data on movies from a file. \nAfterwards it calculates profit to a new updated version of the file, and outputs the movies with highest and lowest profits.')

    #call get_input_filename to set input_filename equal to user input
    input_filename = get_input_filename()

    #read the data from input_filename onto movie_table
    movie_table = read_file_to_list(input_filename)

    # call get_output_filename to set input_filename equal to user input
    output_filename = get_output_filename()

    #Write the data from movie_table onto a new file
    write_table_to_file(movie_table, output_filename)

    #find the movie with the highest profit and output it to the user
    highest_row = find_highest_profit(movie_table)
    print(f'The movie with the highest profit is {highest_row}')

    #find the movie with the lowest profit and output it to the user
    lowest_row = find_lowest_profit(movie_table)
    print(f'The movie with the lowest profit is {lowest_row}')

    #Output exit message to the user
    print('Thank you for using this program!')

# Call main function
main()
