import argparse
import math

#func for user input
#creates argumentparser obj with description
def user_input():
    parser           = argparse.ArgumentParser(description="Enter integer or floating-point values for the directions mentioned:")
    
    #defining the list of arguments as directions value
    directions_value = ['int1','int2','int3','int4']
    
    #loop for adding the arg names to argumentparser & 
    #rounding the value to int value if float is entered
    for directions_value in directions_value:
        parser.add_argument(directions_value, type=convert_to_nearest_int)
    
    #parsing for command line arguments
    args = parser.parse_args()
    
    #extracting the values of int1,int2,int3,int4
    int1 = args.int1
    int2 = args.int2
    int3 = args.int3
    int4 = args.int4

    #calling the func to calcualte the distances using the parsed argument
    calculation(int1, int2, int3, int4)

# Custom type conversion function to convert to nearest integer if float is entered
def convert_to_nearest_int(value):
    try:
        #rounding the called value in float to make it int
        return round(float(value))
    #return any anomly
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid value: {value}. Please enter a valid number.")

#func to change any negative value to positive
def absolute_value(value):
    if isinstance(value,(int,float)):
        return abs(value)

#calculation func using values
def calculation(int1, int2, int3, int4):

    distance        =  int1 + int2 + int3 + int4
    displacement1   = absolute_value((int1 - int2))
    displacement2   = absolute_value((int3 - int4))
    #value generated for the distance from final point to original position
    disp            = absolute_value((math.sqrt((displacement1 ** 2) + (displacement2 ** 2))))
    output(int1, int2, int3, int4, distance,disp)



def output(int1, int2, int3, int4, distance,disp):

    print(f"UP                                {int1}")
    print(f"DOWN                              {int2}")
    print(f"LEFT                              {int3}")
    print(f"RIGHT                             {int4}")
    print(f"T. Travelled distance             {convert_to_nearest_int(distance)}")
    print(f"distance from original position   {convert_to_nearest_int(disp)}")

if __name__ == '__main__':
    user_input()
