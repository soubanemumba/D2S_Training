import matplotlib.pyplot as plt

#function for squaring the list entered
def square(list):
    list_of_numbers2 = [x ** 2 for x in list]
    return list_of_numbers2

#function for cubing the list entered
def cube(list):
    list_of_numbers3 = [x ** 3 for x in list]
    return list_of_numbers3

#declared list 
list = []
print("Enter 10 numbers as a list")
#taking user input
for i in range(10):
    number = int(input())
    list.append(number)

#plotting function
def plotting_func(list, Squared, Cubed):
    #creating figure window of 10x5
    plt.figure(figsize=(10, 5))
    #subplot for squared number graph
    plt.subplot(1,2,1)
    #passing all the parameters for the plot
    plt.plot(list,Squared,marker='o',linestyle='-', color = 'blue')
    plt.title('Squared numbers')
    plt.xlabel('Numbers')
    plt.ylabel('Square')

    #subplot for squared number graph
    plt.subplot(1,2,2)
    #passing all the parameters for the plot
    plt.plot(list,Cubed,marker='o',linestyle='-', color = 'red')
    plt.title('Cubed numbers')
    plt.xlabel('Numbers')
    plt.ylabel('Cube')
    #to prevent overlap, it was overlapping
    plt.tight_layout()
    #command to display the plots
    plt.show()

#calling squared func
Squared = square(list)
#calling cube func
Cubed   = cube(list)
#calling plotting func
plotting_func(list,Squared,Cubed)

