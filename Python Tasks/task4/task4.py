#importing 'random' for generating random numbers, 'argparse' to allow
#using of argument parsing through terminal, 'json' to let the code read json files
import random
import argparse
import json


#main code for generating random numbers (x,y) 7 calculating estimations
def estimate_pi(iterations):
    #variables for points inside circle and swuare
    points_inside_circle = 0
    points_inside_square = 0

    #loop for 
    for _ in range(iterations):
        #generating random values between -1 to 1 in x and y directions
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        #calcualting the location
        original_distance = rand_x ** 2 + rand_y ** 2
        #checking if the point lies inside the circle or square
        if original_distance <= 1:
            points_inside_circle += 1
        else:
            points_inside_square += 1
    #calculating the probabilty of the PI & returning
    pi = 4 * (points_inside_circle / iterations)
    return pi

#main func to handle the userinput through argparse
def main():
    #argument parser
    parser = argparse.ArgumentParser(description='Monte Carlo simulation to estimate the value of pi.')
    #command line arguments
    parser.add_argument('-i', '--iterations', type=int, help='Number of iterations')
    parser.add_argument('-j', '--json', help='Read iterations from a JSON file')
    parser.add_argument('-H', '--custom-help', action='store_true', help='Display help message')
    args = parser.parse_args()

    #the message for help when user enters '-h'
    if args.custom_help:
        print("Monte Carlo Pi Estimation Tool")
        print("Usage: python monte_carlo_pi.py -i <iterations>")
        print("Options:")
        print("  -i, --iterations   Number of iterations")
        print("  -j, --json         Read iterations from a JSON file")
        print("  -H, --custom-help  Display this help message")
        return
    
    #if user chooses json file to enter iterations
    if args.json:
        try:
            #opens the json file and reads the command
            with open(args.json, 'r') as json_file:
                data = json.load(json_file)
                if 'iterations' in data:
                    #if 'iterations' is mentioned in file, it fetches the value
                    args.iterations = data['iterations']
                else:
                    print("JSON file should contain 'iterations' key.")
                    return
        #else for any problem displays erorr
        except FileNotFoundError:
            print(f"File not found: {args.json}")
            return
    #if user enters no iteration value in '-i' option
    #or the json file doesnt contain 'iteration' value
    #this message is displayed
    if args.iterations is None:
        print("You must specify the number of iterations either with -i or -j.")
        return
    #estimation of pi value
    pi = estimate_pi(args.iterations)
    print(f"Estimation of PI using {args.iterations} iterations:", pi)

if __name__ == "__main__":
    main()
