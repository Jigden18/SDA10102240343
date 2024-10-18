#################################################
#https://github.com/Jigden18/SWE_CAP1_Dzo_Spell_Checker.git

# Jigden Shakya
# "A"
# 02240343
##################################################
#REFERENCES

# https://www.geeksforgeeks.org/how-to-download-files-from-urls-with-python/
# https://stackoverflow.com/questions/62859658/how-to-convert-docx-to-txt-in-python
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
# https://pynative.com/python-delete-lines-from-file/
# https://medium.com/@nitin.data1997/spell-checker-in-python-create-your-own-spell-checker-a14758272ff

# PROBLEM : We are assigned with a Dzongkha text file (dzo.txt) which contains multiple spelling errors 
# which we are tasked to compare with a dzongkha dictionary file (initially a docx file) and get the errors
# in the txt file with the respective line number and word number in line . 
# prerequisites : you need to have a dzongkha dictionary saved as dictionary.docx

# https://www.youtube.com/watch?v=ac3nbZ0V9PU
# https://www.youtube.com/watch?v=XxRtj-GU5_8
# https://www.youtube.com/watch?v=LyymFN9t4kw
# https://www.youtube.com/watch?v=26vNgM_wSAE

##########################################################
# SOLUTION
##########################################################

# Read the input file
# first we use python requests module to get the file from url
import requests
url = "https://csf101-server-cap1.onrender.com/get/input/343"
download_file = requests.get(url)

# checking download request was successful the status code attribute
if download_file.status_code == 200 :
    print("Input file downloaded")
else:
    print("Input file not downloaded")

# we write(create) a file and write the contents in it
with open("343.txt", "w", encoding="utf-8") as file : # we use the encoding for python to read the file contents.
        file.write(download_file.text)

# Read the input file
def readfile(filename):
    with open(filename,"r",encoding="utf-8") as file : 
           contents = file.read()

readfile("343.txt")

# now we need to convert the dictionary.docx to a txt file.
from docx import Document # for that, we use the docx module of python.

dict_doc = Document("dictionary.docx") # then we open the docx file and store in a variable.

with open("dict.txt","w", encoding="utf-8") as file :#then we create/write a txt file and write the contents of docx file to it.
       for line in dict_doc.paragraphs :# we loop through each line and write content in each line to our txt file.
              file.write(line.text + "\n")


# now we only want to keep only the Dzongkha words from the dictionary
# for that we use another module (regex or regular expression) to seperate the dzongkha words from other
import re
# the dzongkha unicode characters ranges fron UTF value \u0F00 to \u0FFF
dzongkha_series = re.compile(r"[\u0F00-\u0FFF]+")# we now define the unicode range for dzo words
# Now we need to read the our file and write a new file and save our dzongkha words in it.
with open ("dict.txt","r",encoding="utf-8") as draft :
    with open ("cleaned_dict","w",encoding="utf-8") as final_dict :
        # next step we need to loop through every line and select the characters under the range we assigned.
        for line in draft:
            dzo_words = dzongkha_series.findall(line)

            for words in dzo_words :
                final_dict.write(words+"\n")
# after that the output file will appear as a file
# the cleaned dictionary has unwanted lines till line 182
# read lines in your cleaned dictionary 
with open("cleaned_dict", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# we remove the lines till 182  and write the remaining 
with open("cleaned_dict", 'w', encoding='utf-8') as f:
    f.writelines(lines[183:])

import re

filepath = "343.txt"
cleaned_dictpath = "cleaned_dict"

#Read the 343.txt file and split it into lines
with open(filepath, 'r', encoding='utf-8') as file :
    lines_in_filepath = file.readlines()  # List of lines in the file

#Read the cleaned dictionary and split it into words by '་'
with open(cleaned_dictpath, 'r', encoding='utf-8') as dict_file:
    dictionary_words = dict_file.read().split('་') 

#Clean up any extra spaces around words in the dictionary
dictionary_words = [word.strip() for word in dictionary_words]

# we define a sub function to get words from a line
def get_words_from_line(line):
    # This regex matches sequences of non-whitespace characters followed by "་"
    return re.findall(r'(\S+?)་', line)  # Extract words ending with "་"

# traverse through each line in input.txt and find any words that aren't in the cleaned_dict
error_words = []

for line_number, line in enumerate(lines_in_filepath, start = 1):# fileline starts from 1
    # Get all words in this line
    words_in_line = get_words_from_line(line)  
    
    for word_index, word in enumerate(words_in_line, start = 1): #wordcount starts from 1
        if word not in dictionary_words:  # If word are not in dictionary, it is error
            error_words.append((line_number, word_index, word))  # Store line, word number, and the error word

#Print out the error
for line_number, word_number, word in error_words:
    print(f"Line {line_number}, Word {word_number}: Error Word - {word}")
