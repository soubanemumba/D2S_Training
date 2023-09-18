import asyncio
import time
from pprint import pprint

async def async_find_divisibles(in_range,divisor):
    #fetching the time-1
    start = time.time()
    print("find_divisibles called with range", in_range, "and divisor",divisor,"\n")
    #list variable for storing the number which are divisible by the divisor    
    numbers_divisible_by_divisor= []
    #iterative loop to check dividend and appending the
    #required number in the list
    for num in range (1, in_range+1):
        if num % divisor == 0:
           numbers_divisible_by_divisor.append(num)
           await asyncio.sleep(0)
    
    print(numbers_divisible_by_divisor)
    # fetching the time-2, to calculate the difference
    end = time.time()
    #finding the elapsed time by difference
    total_time_elapsed = end - start
    print("find_divisibles called with range" , in_range , "and divisor" , divisor, "and it took" , total_time_elapsed , "second \n")
    return(numbers_divisible_by_divisor)

# This is the main co-routine that calls the async_find_divisibles function
async def main():
    # function calling
    print("\n")
    result1 = await async_find_divisibles(5080000,34113)
    print("\n")
    result2 = await async_find_divisibles(100052,3210)
    print("\n")
    result3 = await async_find_divisibles(500,3)

if __name__ == "__main__":
    asyncio.run(main())