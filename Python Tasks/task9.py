
print("How much words you want to enter? ")
#taking input from user about the amount of number of words
n_number_of_words = int(input())

#initialize an empty dictionary to store words 
dictionary = {}
#an empty list to store all type of words
list_of_words = []
#for storing the count of distinct words
distinct_words = []

#loop to process each words
for i in range(n_number_of_words):
    temp_word = input()                 #reading input from users
    if temp_word not in dictionary:     #if the word is not present in the dictionary
        list_of_words.append(temp_word) #append that words inside the dictionary
        dictionary[temp_word] =1        #change count into 1 for that specific word
    
    #if the word is present
    else:
        dictionary[temp_word] +=1       #increment the count for the existing words

#loop for generating the count of distinct words inside the dictionary
for temp_word in list_of_words:         
    distinct_words.append(str(dictionary[temp_word]))   

#display the number of distinct words
print(len(list_of_words))

#printing the occurences of each words without spaces
print("".join(distinct_words))