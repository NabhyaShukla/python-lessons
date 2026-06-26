"""

    READ ALL THE NAMES LINE-BY-LINE AND STORE ONLY THOSE NAMES
    IN ANOTHER LIST , WHERE THE LENGTH OF NAMES ARE GREATER THAN 4 
    AND PRINT IN ANOTHER FILE 'WORDS_OUT.TXT'

"""

file = open("word.txt", "r")
lines = file.readlines()
file.close()

ofile = open("words_out.txt", "w")
