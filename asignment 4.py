"""Topic : File handling
Exercise 1:
Write a Python program to read a file and display its contents"""

"""file1 = open("hello.py","r")
print(file1.read())
file1.close()"""

"""Exercise 2:
Write a Python program to count the number of lines in a file"""
"""file1 = open("hello.py","r")
print("number of line in the file is \t", len(file1.readlines()))
file1.close()

Exercise 3:
Write a Python program to write some text to a file"""

"""file1= open("hello.py","w")
file1.write("Data science and Machine Learning \n Computer science")
file1.close()

file1 = open("hello.py","r")
print(file1.read())
file1.close()

Exercise 4:
Write a Python program to append some text to a file."""

"""file1= open("hello.py","a")
file1.write(" \nI am taking classes for data science and machine learning course")
file1.close()

file1 = open("hello.py","r")
print(file1.read()
file1.close()

Exercise 5:
Write a Python program to copy the contents of one file to another file"""

"""with open("new_file1","r") as file1, open("new_file2","w") as file2:
    content = file1.read()
    new_content = file2.write(content)
    print(new_content)
"""


"""file1 = open("sample1","r")
content=file1.read()
file1.close()
file2 = open("newhello.py","w")
new_content=file2.write(content)
file1.close()
print(new_content)"""

"""with open("SAMPLE.py",'r') as firstfile, open('newhello.py','w') as secondfile:
      
    # read content from first file 
    for line in firstfile: 
               
             # write content to second file 
             secondfile.write(line)

file1 = open("newhello.py","r")
print(file1.read())
file1.close()

Exercise 6:
Write a Python program to read the content of a file and count the total number of words in that file."""

"""with open("newhello.py","r") as file1:
    content = file1.read()
    content=content.split()
    print("total number of words in the file is ",len(content))
    
    
Exercise 7:
Write a Python program to read the content of a file and count the number of occurrences of a specific word in that file"""

"""with open("newhello.py","r") as file1:
    content = file1.read()
    content = content.count("SHANTHI")
    print("Total occurrence of the word \"SHANTHI\"",content)
    
Exercise 8:
Write a Python program to read the content of a file and count the number of unique words in that file."""

def countUniqueWords(fileName):
    file = open(fileName, 'r')
    read_file = file.read().lower()
    words_in_file = read_file.split()
    count_map = {}


    for i in words_in_file:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1


    count = 0

    for i in count_map:
        if count_map[i] == 1:
            count += 1
    file.close()
    return count

with open("gfg.txt", "w") as file:
    file.write("Data science combines math and statistics, specialized programming,\n"
               " advanced analytics, artificial intelligence (AI), and machine learning with \n"
               "specific subject matter expertise to uncover actionable insights \n"
               "hidden in an organization's data.")

print('Number of unique words in the file are:',
      countUniqueWords('gfg.txt'))







