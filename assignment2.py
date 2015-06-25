

def add_vectors(vector_1, vector_2):
    """Returns a list object representing the result of adding two vectors together.

       Arguments:
       vector_1 -- list representing first vector
       vector_2 -- list representing second vector

       Error checking:
       Both arguments must be of type list.
       Both vectors must of the same length.
       Only vector elements of type int can be added together.
    """
    list_1 = None
    
    # print(vector_1.typ)
    if (vector_1 == None and vector_2 == None):
        print("Error: first argument is not a list")
        print("Error: second argument is not a list")
        return None
    elif (vector_1 == None ):
        print("Error: first argument is not a list")
        return None
    elif (vector_2 == None):
        print("Error: second argument is not a list")
        return None
    elif(not isinstance(vector_2, list) and not isinstance(vector_1, list)):
        print("Error: first argument is not a list")
        print("Error: second argument is not a list")
        return None
    elif(not isinstance(vector_1, list)):
        print("Error: first argument is not a list")
        return None
    elif(not isinstance(vector_2, list)):
        print("Error: second argument is not a list")
        return None
    elif (len(vector_1) != len(vector_2)):
        print("Error: lengths of the two vectors are different")
    else:  
        list_1 = vector_1
        i = 0
        while(i < len(vector_1)):
            if(not isinstance(list_1[i], int) or not isinstance(vector_2[i], int)):
                print(("Error: attempted to add incompatible {} to {}").format(list_1[i], vector_2[i]))
                return None
            list_1[i] = list_1[i] + vector_2[i]
            i = i + 1
        
        enumerate(list_1)
        
    return list_1


def print_frequency(some_text):
    """Prints a table of letter frequencies within a string. 

       Non-letter characters are ignored.
       Table is sorted alphabetically.
       Letter case is ignored.
       Two blank spaces will separate the letter from its count.

       Returns None in all cases.

       Argument:
       some_text -- string containing the text to be analysed.

       Error checking:
       The argument must be a string object.
    """
    if(not isinstance(some_text, str)):
        print("Error: only accepts strings")
        return None
    elif(isinstance(some_text, int)):
        print("Error: only accepts strings")
        return None
    elif (isinstance(some_text, float)):
        print("Error: only accepts strings")
        return None
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index = [0] * 26
    
    for i in some_text:
        if(i.lower() in alphabet):
            index[alphabet.index(i.lower())] = index[alphabet.index(i.lower())] + 1
    
    j = 0
    
    while j < 26:
        if(not (index[j] == 0)):
            print(alphabet[j] + "  " + str(index[j]))
        j = j + 1
    

def verbing(some_text):
    """Returns a string where the each word has ing added to it if it is 3 or more characters or length and 
       ly to shorter words.

       Argument:
       some_text -- string containing the text to be analysed.

       Error checking:
       The argument must be a string object.
    """
    string = ""
    if(not isinstance(some_text, str)):
        print("Error: only accepts strings")
        return None
    elif(isinstance(some_text, int)):
        print("Error: only accepts strings")
        return None
    elif (isinstance(some_text, float)):
        print("Error: only accepts strings")
        return None
    elif(len(some_text) == 0):
        print("''")
        return None
    else: 
        words = some_text.split()
        for x in words:
            if len(x) >=3:
                words.insert(words.index(x), (x + "ing"))            
                words.remove(x)
            elif len(x) < 3:
                words.insert(words.index(x),x + "ly" )
                words.remove(x)
    
        for x in words:
            string = string + x + ' '


    string = string[:-1]
    
    return string




def verbing_file(file_name):
    """Returns the contents of a given file after applying the verbing function to each
       line in the file.

       Argument:
       file_name -- name of the file (assumed to exist in same directory from where the 
                    python script is executed.

       Error checking:
       The argument must be a string object.
       File must exist and be readable (note no need to distinguish these cases).    
    """
    if(not isinstance(file_name, str)):
        print("Error: only accepts strings")
        return None
    finale = ""
    
    file = open(file_name, 'r')
    wordList = []
    for text in file:
        wordList.append(verbing(text))
        wordList.append("\n")
    wordList.append("\n")
    
    for word in wordList:
        finale = finale + word + ''
    finale = finale[:-1]
    
    return finale





import doctest


doctest.testfile("add_vectors.txt")