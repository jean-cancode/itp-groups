# print("Hello World")

# The Quick Brown Fox
'''
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brown Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 13
Your code should be simple, extremely readable, and well commented. Test thoroughly through every step. Be sure to use type hinting and proper documentation
'''
    
# def brown_fox(word: str) -> str:
#     '''We are looping through the string 
#     to count upper and lower case characters'''
#     upper_count = 0
#     lower_count = 0
    
#     result = word.replace(" ","")
#     # we are going to loop through each character in a string 
#     for i in word:
#         if i.islower():
#             lower_count += 1
#         elif i.isupper():
#             upper_count += 1
            
#     print(f"No. of Upper case characters : {upper_count}\nNo. of Lower case Characters : {lower_count} ")
	

    


# brown_fox("Coding Is Fun Until Its Challenging")
    




# Highest of our two numbers
''' Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers. 
Your code should be simple, extremely readable, and well commented. Test thoroughly through every step. Be sure to use type hinting and proper documentation
'''

# def get_highest(x: int, y: int) -> int:
#     """ The function will return 
#     the highest of two numbers"""
#     if x > y:
#         return x
#     else:
#         return y
# print(get_highest(20, 10))
    
    
    
    





# New job at Chevy
'''
You have been hired by Chevy to look for non-chevy owners to send mailings to.  You have a simple list below of some drivers and the cars they own. Use Lambdas and the filter function to step through and solve this problem.

cars = [{ "Driver": "Mike", "Car": "Honda"},
        { "Driver": "Anthony", "Car": "Ford"},
        { "Driver": "Reynelle", "Car": "Subaru"},
        { "Driver": "Bri", "Car": "Subaru"},
        { "Driver": "Julie", "Car": "Chevy"},
        { "Driver": "Sam", "Car": "Chevy"},
        { "Driver": "Judith", "Car": "Chevy"}]

1. Write a function that will deliver true or false against a single dictionary in the list. After it is tested and you are sure the test results are correct write a lambda function.

2. Write and test your lambda function based on the previously created function.

3. Create a filter function based on your dataset and your lambda

4. Deliver your data to management with just the driver's name (however you prefer)
Your code should be simple, extremely readable, and well commented. Test thoroughly through every step. Be sure to use type hinting and proper documentation
'''

# Using Filter function lets grab everyone in this list who owns a chevy

cars = [{ "Driver": "Mike", "Car": "Honda"},
        { "Driver": "Anthony", "Car": "Ford"},
        { "Driver": "Reynelle", "Car": "Subaru"},
        { "Driver": "Bri", "Car": "Subaru"},
        { "Driver": "Julie", "Car": "Chevy"},
        { "Driver": "Sam", "Car": "Chevy"},
        { "Driver": "Judith", "Car": "Chevy"}]



# First create a function that delivers true or false depending on if the user owns a chevy

car = { "Driver": "Mike", "Car": "Chevy"}
def locate_chevy(car):
    if car["Car"] == "Chevy":
        return True
    else:
        return False
# print(locate_chevy(car))
        
    
locate_chevy(car)

# lambda arguments : expression
chevy = lambda car : True if car["Car"] == "Chevy" else False

# print(chevy(car))

add_two_lambda = lambda x,y : x + y
# print(add_two_lambda(2,3))
# print((add_two_lambda)(2,3))

chevy_filter = filter(lambda car : True if car["Car"] != "Chevy" else False, cars)
print(list(chevy_filter))






# Next test that your function works on 1 dictionary in the list of cars

# Create and test lambda from function

# Use the filter function to deliver dictionaries with chevy owners

# Loop through and deliver the name of the drivers in whatever format you prefer


# Group 1 / Group 2
'''
Your development team is creating a large application. Group 1 is in charge of creating a function which will take a list of dictionaries.  From the data, please extract email addresses and deliver to Group 2 as a list which will be used for marketing.

data = [
	{
		"name": "Fay Duke",
		"email": "sed.nunc.est@protonmail.couk",
		"phone": "1-240-443-8652"
	},
	{
		"name": "Stuart Strong",
		"email": "sit@protonmail.com",
		"phone": "1-113-229-6241"
	},
	{
		"name": "Adria Ortega",
		"email": "ultricies.ornare@icloud.net",
		"phone": "(425) 517-3787"
	},
	{
		"name": "Angela Willis",
		"email": "porttitor.vulputate@outlook.edu",
		"phone": "1-847-221-3669"
	},
	{
		"name": "Byron Guthrie",
		"email": "aliquam.auctor@yahoo.ca",
		"phone": "1-778-467-5941"
	}
]

Group 2, you will create a function that takes in this list of valid email addresses. and return a list of only valid email addresses. Accepted top level domains (.com, .edu, .net) and other standard email format testing as needed. 
'''










































































































