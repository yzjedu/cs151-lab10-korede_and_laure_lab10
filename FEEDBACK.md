

- [LAB-10 Feedback](#lab-10-feedback)
    - [Test Cases](#test-cases)
    - [Blind Test: Running the code](#blind-test-running-the-code)
    - [Open Test: Looking at the code](#open-test-looking-at-the-code)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)

# LAB-10 Feedback

### Test Cases

**Given the movie.csv**

| Test Case | in: in_file_name | in: out_file_name | in: choice   | out: profit | out: title     |
|-----------|------------------|-------------------|--------------|-------------|----------------|
| 1         | bbb.txt          | try again         |  -           |       -     | -              |
| 2         | movie.csv        | updated_movie.csv | highest      | 2686706026  | Avatar         |
| 3         | movie.csv        | updated_movie.csv | lowest       | -274800000  | The Marvels    |

### Blind Test: Running the code
| Result       | Description                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------|
| **YES-**   | Asks the user for an input file name                                                            |
| **YES-**   | Asks user to try again if input file name doesn't exist (try `bbb.txt`)                         |
| **YES-**   | User is asked for name of output file to store profits                                          |
| **YES-**   | Output file has 1 movie per line with commas between each datapoint; like the original  but with extra column |
| **YES-**   | Profit is calculated correctly (see test cases for each movie's profit; you don't need to check all of them) |
| **YES-**   | Highest or lowest is calculated correctly (see test cases; they got to choose if they did highest or lowest) |
| **YES-**   | Highest/lowest outputs all information about that movie                                         |

### Open Test: Looking at the code
| Result       | Description                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------|
| **YES-**   | The algorithm matches the code                                           |
| **YES-**   | Purpose of the program is clearly stated |  
| **YES-**   | Error checking on file name uses `while os.path.isfile(filename)` |
| **YES-**   | There is a function for error checking file name that returns file name                         |
| **YES-**   | There is a function for reading from the file that returns a table(list of lists)                      |
| **YES-**   | There is a function for adding the profit. This may also be the same function that writes to the file |
| **YES-**   | There is a function to find movie with highest/lowest profit                                    |
| **YES-**   | If above function doesn't write to file, another function does that writing                     |



### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**YES-** | Reflection 1   |
|**-NO** | Reflection 2   |
|**YES-** | Algorithm      |

### Comments on the grading
- You could have given the name and the profit level for highest and lowest instead of the row
- 
- 

### Grade: E

### Participation Grade: S
U for korede
 - If participation grade is unsatisfactory check the `NO` in the documents sections
