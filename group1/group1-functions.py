# Alphabetize our colors
'''
Write a Python function that accepts a hyphen-separated sequence of words in a string as input and prints the words in a 
hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
Your code should be simple, extremely readable, and well commented. Test thoroughly through every step. Be sure to use type hinting and proper documentation
'''

def alphabetical(input_str: str)-> str: # Defining a function

	word =  input_str.split('-') # splitting the input_string at each " - "

	sort_word = sorted(word) # Sorting each word alphabetically

	finish_str = "-".join(sort_word) # Joining each word back together with a " - "
	return finish_str # Returning your finished string

input_str = "green-red-yellow-black-white" # Entering your sample string 

# print(alphabetical(input_str)) # 


# How many miles?
'''
Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.
Your code should be simple, extremely readable, and well commented. Test thoroughly through every step. Be sure to use type hinting and proper documentation
	'''
# userkilometers = float(input("Enter value in kilometers: "))
def km_to_miles(userkilometers):
	
	mile_test = userkilometers / 1.609
	return mile_test

# print(km_to_miles(userkilometers))




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
#[i for i in records if (i['title'] == 'developer')]
# for key, value in dictionary.items():
#     print(key, value)

#sorted(iterable, key=key==lambda, #optional reverse=True/False)
# First create a function that delivers true or false depending on if the user owns a chevy
# name = input("Which driver would you like ot check? ")
# def chevy_owner(name): # Taking in the name
# 	global cars # pulling in the dictionary for the cars
# 	for Driver in cars: # Check for the driver we are looking for
# 		if Driver['Driver'] == name: # if the driver is = to the driver we are looking for continue
# 			if Driver["Car"] == "Chevy": # if they drivers car is chevy return false
# 				return False
				
# 			else:
# 				return True # if the driver doesn't own a chevy send them the mail
# print(chevy_owner(name))
def chevy_owner2(owner):
	if owner["Car"] == "Chevy":
		return False
	else:
		return True
# Next test that your function works on 1 dictionary in the list of cars

# Create and test lambda from function

# Use the filter function to deliver dictionaries with chevy owners
# print(list(filter(chevy_owner2, cars)))
# Loop through and deliver the name of the drivers in whatever format you prefer
result = list(filter(chevy_owner2, cars))
for owner in result:
	print(owner['Driver'])


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







