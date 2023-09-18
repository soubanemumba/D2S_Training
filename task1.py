#divisible by 7
#not multiple of 5
# 7, 14, 21, 28, 

print("*This program will print only the numbers between 2000-3500 which are divisible by 7 but not multiple of 5*")

#creating list to save the numbers in the format of list later
numberlist = []

#loop to iterate 1200 times but within the range fo 1200 to 3200
for i in range (2000, 3200):
    #check statement for divisible by 7 & not multiple of 5
    if i%7==0 and i%5 !=0:
        #adding/appending each approved value to list
        numberlist.append(i)

#printing the values 
for numberlist in numberlist:
    #printing the list with 'end' function to specify appending ',' at the end of each printed item
    print(numberlist, end=",")