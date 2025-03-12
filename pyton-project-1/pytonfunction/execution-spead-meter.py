import time
import datetime
from datetime import datetime #if this function calling used dont have to call library.object.function --> datetime.datetime.now()
'''
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Execution Time: {end_time - start_time} seconds")
        return result
    return wrapper

@execution_time
def sample_function():
    # Simulate a function that takes some time to execute
    for x in range(1, 10):
        print(x)
        time.sleep(2)
    print("Function executed")

if __name__ == "__main__":
    sample_function() 
    '''

def print_time():
        print ("Task completed")
        print (datetime.now())
        print ()
        
first_name = "Kirubel"
print_time ()
start_time = time.time()
for x in range (1, 10):
    print(x)
print_time()
end_time = time.time()
print (f"the comlition time is: {end_time - start_time} seconds")



#paramiters in function
def print_time2(paramiter1):
        print(paramiter1)
        print(datetime.now())
first_name1 = "Kirubel"
print_time2("first name assigned") #this string passed to as a paramiter for the function print_time2()
for x in range(1,10):
    print(x)
print_time2("loop completed")


#accept user name and display the first charater of the name string
first_name = input("enter your firsst name")
#this will return the first character from the string 0 being the string first index and 1 being the number of characters
first_name_initial = first_name[0:1]
last_name = input("enter your firsst name")
last_name_initial = last_name[0:1]
print("your initial are: " + first_name_initial + last_name_initial)

#accept user name and display the first charater of the name string using functtion
def get_initials(name):
        name_initial = name[0:1].upper()#the ,upper function will force the returned value to be capital leter
        return name_initial
first_name3 = input("Enter your first name")
first_name3_initial = get_initials(first_name3)
last_name3 = input("Enter your lastt name")
last_name3_initial = get_initials(last_name3)
print("your initial are: " + first_name3_initial + last_name3_initial)
print("your initial are: " + get_initials(first_name3) + get_initials(last_name3))#we can directly put the returen value in to print function

    