# Algorithm Document

----------------------
* Purpose: get user input of which file to read
* Name: get_input_filename
* Parameters: none
* Return: input_filename, string, represents name of the file that will be read
* Algorithm:
1. Set variable input_filename set user to user input, given the output "What filename would you like to read?"
2. return input_filename
-------------------------------
* Purpose: reads the file to a list
* Name: read_file_to_list
* Parameters: filename, string, the name of the file that will be read
* Return: movie_table, table, table of data for each movie from the file
* Algorithm:
1. create empty table movie_table
2. try
   1. open filename for reading
   2. for each line in the file
      1. create a row for each line split along the commas
      2. add each row to the table movie_table
      3. convert index 4 of each row to an integer
      4. convert index 3 of each row to an integer
      5. convert index 2 of each row to an integer
   3. Close the file
3. Except for a filenotfound error
   1. output to the user "File does not exist"
4. Return movie_table
------------------
* Purpose: get user input of which file to write to
* Name: get_output_filename
* Parameters: none
* Return: output_filename, string, represents name of the file that will be created and written to
* Algorithm:
1. set output_filename equal to user input given the output, "What is the name of the file you would like to output?"
2. return output_filename
-----------------
* Purpose: writes the table to a new file
* Name: write_table_to_file
* Parameters: movie_table (table, table of data from each movie), output_filename (string, name of file that will be created where the data will be written)
* Return: none
* Algorithm:
1. open output_filename for writing, setting it equal to the variable outfile
2. for each row in the movie_table
   1. set profit equal to row index -1 - row index -3
   2. add a row to the table for profit
   3. create an empty line
   4. for each item in row
      1. add item to the line with a comma separating it
      2. write each line to the outfile
3. close outfile
-----------------
* Purpose: finds which movie has the highest profit
* Name: find_highest_profit
* Parameters: table (table, which table to find the highest profit from)
* Return: highest_row (string, which row has the highest profit)
* Algorithm:
1. Initialize the first row of the table as the highest_row for comparison
2. for each row in the table
   1. if index -1 of the row is greater than index -1 of highest_row
      1. Highest row is set equal to row
3. Return highest_row
-----------------
* Purpose: finds which movie has the lowest profit
* Name: find_lowest_profit
* Parameters: table (table, which table to find the lowest profit from)
* Return: lowest_row (string, which row has the lowest profit)
* Algorithm:
1. Initialize the first row of the table as the lowest_row for comparison
2. for each row in the table
   1. if index -1 of the row is less than index -1 of lowest_row
      1. lowest_row is set equal to row
3. Return lowest_row
-----------------
* Purpose: main function
* Name: main
* Parameters: none
* Return: none
* Algorithm:
1. Output welcome message and purpose of the program
2. call get_input_filename and set it equal to input_filename
3. call read_file_to_list with the argument input_filename and set it equal to movie_table
4. call get_output_filename and set it equal to output_filename
5. call write_table_to_file with the arguments movie_table and output_filename
6. call find_highest_profit with the argument movie_table and set it equal to highest_row
7. output to the user "The movie with the highest profit is {highest_row}"
8. call find_lowest_profit with the argument movie_table and set it equal to lowest_row
9. output to the user "The movie with the lowest profit is {lowest_row}"
10. output exit message to the user
-----------------
1. Call the main function

