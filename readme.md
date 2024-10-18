# Dzongkha Spell Checker

## Project Overview
In my Dzongkha Spell Checker, I have downloaded the input file and saved it to a directory named STD_code.txt and read the contents in it. Then we converted the dictionary( initially a .docx file ) to dict.txt and further refined it by extracting Dzongkha words and removing the unwanted lines and storing it in a new file(cleaned_dict).Finally we took the input file and cleaned_dict and extracted the words from each line in input file and comparing it to the words in the cleaned_dict. finally, I returned the line number , word number and the word which was detected as error.


## Table of Contents
-  ### Usage
-  ### Implementation-details
-  ### Data-structures
-  ### Algorithms
-  ### Challenges and Solutions
-  ### Future improvements
-  ### References

## Usage

- The spell checker has three different events:
 1. Downloading and reading the input file 
 2. Processing the dictionary.docx
 3. Comparison of words and error detection
              
### 1 . Downloading and reading the input file

- Install requests module.
- Provide a url to the input file and use requests.get( ) to download the file.
- Check if the download was successful (.statuscode == 200)
we save the download as a file(STD_code.txt) using with( ) open function in "w" write mode.
- Read the file contents using with() open in "r" read mode.


### 2 . Processing the dictionary.docx
- Convert the .docx file to .txt using the docx module and save it using with open( ) in write mode as dict.txt.
- The code reads the text file dict.txt and uses regular expressions to find and extract Dzongkha words based on their Unicode range (\u0F00 to \u0FFF).
The extracted Dzongkha words are saved into a new file, cleaned_dict.
- The first 182 lines of cleaned_dict are removed, keeping only relevant data from line 183 onward using slicing.

### 3 . Comparison of words and error detection
- we import regex module.
- we take the input file and cleaned_dict and store them into variables.
- Read the 343.txt file and split it into lines.
- Read the cleaned dictionary and split it into words by '་'
- Clean up any extra spaces around words in the dictionary.
- we define a sub function to get words from a line.
- traverse through each line in input.txt and find any words that aren't in the cleaned_dict.
- Print out the error : ine_number, word_number, error words.

## Implementation
- This code starts by downloading a file from the internet using the requests library, targeting a specific URL. It checks if the download was successful by verifying that the response's status code is 200. If successful, it prints "Input file downloaded"; otherwise, it notifies the user that the download failed.
Once the download is confirmed, the content is written into a local file named 343.txt, ensuring proper text encoding (UTF-8). This file is then created or overwritten with the downloaded content.Additionally, the code defines a readfile() function, which opens the newly created file, reads its entire content, and stores it in the contents variable

- The code begins by importing the necessary libraries, specifically the Document class from the python-docx library to handle .docx files and the re module for regular expression support. It then opens the Word document (dictionary.docx) and stores its content in a variable called dict_doc. A new text file named dict.txt is created for writing, where the code loops through each paragraph in dict_doc, writing the text of each paragraph to the text file and adding a newline for separation.Next, the code compiles a regular expression pattern to match characters within the Dzongkha Unicode range (\u0F00 to \u0FFF). It opens the dict.txt file for reading and creates a new file called cleaned_dict for writing. The code then loops through each line in dict.txt, using the regex pattern to find all Dzongkha words and writing each of these words to cleaned_dict, with each word on a new line.Finally, the code opens cleaned_dict in read mode to retrieve all lines, storing them in a list, and then opens the file again in write mode to keep only the lines from index 183 onwards, effectively removing the first 182 lines. The result is a final text file containing only the relevant Dzongkha words extracted from the original document.

- The provided code identifies and returns words from a text file (343.txt) that are not present in a cleaned dictionary (cleaned_dict). It begins by importing the regular expression library and defining file paths for both the input and the dictionary files. The code reads the contents of 343.txt into a list of lines and subsequently reads the cleaned dictionary, splitting it into individual words based on the character '་' while stripping any extra whitespace. A sub function, get_words_from_line(), is defined to extract words from each line using a regular expression that matches sequences of non-whitespace characters followed by the character. The code then traverses through each line, using the sub function to retrieve words and checking each word against the dictionary. Any word not found in the dictionary is recorded, along with its line and word position. Finally, the code prints out each error word, displaying its line number and index for easy identification. 

## Data structures
- The data structures I used in the entire code are :
- 1 . List: 

* lines_in_filepath: This list keeps all the lines from the 343.txt file.
* dictionary_words: This list holds individual words taken from the cleaned dictionary file (cleaned_dict). It is created by splitting the dictionary text at the character '་' and removing any extra spaces around the words.
* error_words: This list contains tuples. Each tuple has the line number, word index, and an error word from 343.txt. It helps track which words are missing from the cleaned dictionary.

- 2 . Tuple:

* Items in error_words: Each item in the error_words list is a tuple with three parts: the line number, word index, and the error word. This makes it easy to group related information.


## Alogorithms

- The key algorithms used are :

* HTTP Request : "requests.get( )" makes an HTTP request to download content from a specified URL and checks the response status to ensure the request was successful ( download_file.200 ).

* File Writing and Reading: " with open () as file : " to write content to files (343.txt, dict.txt, cleaned_dict) and read from them, processing the content either line by line or as a whole.

* Document Processing:The code uses the docx library (from docx import Document*) to read the contents of a .docx file. It iterates through the paragraphs, extracting text to be written to a new text file.
* Regular Expression Matching:Pattern Matching: Regular expressions (regex) are employed to identify and extract Dzongkha words based on their Unicode range (\u0F00-\u0FFF). The regex pattern matches character sequences within this specified range. we also used it for comapring word while
extracting word between whitespaces and "་" .

 * Traversing lines and characters : Use of for loops "for line_number, line in enumerate(lines_in_filepath, start = 1): " to iterate through line number and word number in line of the 343.txt file.

### Performance analysis 
 * 1.Downloading and file operations for input file : 
 -  Time complexity = O(n) as the time taken for these operations is directly proportional to the size of the file. Thus, the time complexity is O(n).
- Space complexity = O(n) as space required to store the contents of the file is directly proportional to the size of the file.


* 2.Processing the dictionary : 
- Time complexity = O(n) as time complexity is directly proportional to the number of lines in the file, hence O(n) where n is the number of lines in the file.
- Space complexity = O(n+o+p) considering the additional space required for variables, data structures, and temporary storage.

* 3.Spell-checking : 
- Time complexity = O(n^2) as the code reads the lines from the file and then for each line, it extracts words using regular expressions. For each word extracted, it checks if it is in the dictionary_words list. This involves nested loops where the outer loop iterates over the lines and the inner loop iterates over the words in each line. Therefore, the overall time complexity is O(n^2) where n is the total number of words in the lines of the input file.
- Space complexity = O(n)

## Challenges and Solutions
* Some of the challenges faced are :
- 1 . Handling files of different format and of common encoding("utf-8").
- 2 . Network connectivity and download failures.
- 3 . Handling large files which is heavy on the storage files.
- 4 . Assuring the content integrity while converting from .docx to .txt.
- 5 . Variations while extracting the words from input file before comparing it with cleaned dictionary.

* Below are some attempts to ensure that the error is prevented :

- 1 . Always specify encoding='utf-8' when reading or writing files to avoid encoding issues and validating appropriate filepath.
- 2 . using status code to check if the request was successful. or adding a timeout (optional)
eg; requests.get(url,timeout=20 )
- 3 . Process files line by line using iterators to avoid loading the entire file into memory.
eg; with open("343.txt", "r", encoding="utf-8") as file:
    for line in file:
- 4 . Using the regex module for detecting regular expressions.
- 5 . Ensuring Python-docx module is installed.

## Future Improvements

- Firstly, we need to define functions for downloading and file operations , conversion and comparison for clean coding layout and for userfriendly code( easy to undersatnd). These aspects are not fulfilled and are to be improvised.

- Usage of other methods like two pointers to address the problem.
- Currently, the solution has a time complexity of O(n^2). Thus we need to achieve the solution with better run time like O(logn).

- Refer to other spell checkers like the Japanese spell checker and implement changes to our spell checker


## References
- Here are the resources I used for the assignment :

* 1 . [Geekforgeeks]( https://www.geeksforgeeks.org/how-to-download-files-from-urls-with-python/ )
* 2 . [StackOverflow](https://stackoverflow.com/questions/62859658/how-to-convert-docx-to-txt-in-python)
* 3 .[W3Schools](https://www.w3schools.com/python/python_file_handling.asp)
* 4 .[Geekforgeeks2](https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/)
* 5 . [Pynative](https://pynative.com/python-delete-lines-from-file/)
* 6 . [Medium](https://medium.com/@nitin.data1997/spell-checker-in-python-create-your-own-spell-checker-a14758272ff5)
* 7 .[Youtube1](https://www.youtube.com/watch?v=ac3nbZ0V9PU)
* 8 .[Youtube2](https://www.youtube.com/watch?v=XxRtj-GU5_8)
* 9 .[Youtube3](https://www.youtube.com/watch?v=LyymFN9t4kw)
* 10.[Youtube4](https://www.youtube.com/watch?v=26vNgM_wSAE)