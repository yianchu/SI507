########################## Lab 2 Solutions ##########################

# 1. write a function named CelsiusToFarenheit 
#    your function should ask the user for a temperature in celsius
#    your function should convert the temperature to farenheit
#    your function should print the Farenheit Temperature
#    The formula for conversion is (°C × 9/5) + 32 = °F 
#    Check your answer 0 Celsius should be 32°F  and 100 

def CelsiusToFarenheit():
    # method 1: use try/except statements for validation
    temp = input("Enter a temperature (as a number) you want to convert from celsius to farenheit: ")
    while True:
        try:
            temp = float(temp)
            break
        except: 
            temp = input("Error. Please enter a number (e.g., 24) \nEnter a temperature (as a number) you want to convert from celsius to farenheit: ")

    farenheit = (temp * 9/5) + 32

    print(farenheit)

CelsiusToFarenheit()

def CelsiusToFarenheit_alt():
    # method 2: use using isdigit() + replace() to check for floats
    temp = input("Enter a temperature (as a number) you want to convert from celsius to farenheit: ")
    while True:
        # assign to a new value so we don't alter the original
        temp_check = temp.replace('.', '').isnumeric() 
        # if our check shows we have a number, move forward with the calculation
        if temp_check is True: 
            temp = float(temp)
            break
        else: 
            temp = input("Error. Please enter a number (e.g., 24) \nEnter a temperature (as a number) you want to convert from celsius to farenheit: ")

    celsius = (temp * 9/5) + 32

    print(celsius)

CelsiusToFarenheit_alt()


# """
# 2. write a function named MarketingCampaign.
#    your function should accept the following parameters:
#        DigitalAds - an integer representing the budget for buying internet ads
#        TVAds - an integer representing the budget for buying television ads 
#        PrintAds - an integer representing the budget for buying newspaper ads 

#    Calculation: Assume that at your company a single marketing campaign consists of 
#             7 digital ads (cost: 1 unit per ad = 7 units)
#             3 television ads (cost: 1 unit per ad = 3 units)
#             6 print ads. (cost: 1 unit per ad = 6 units)
#             and that ads of all types cost 1 unit.

#     Return Value: 
#        An integer representing the number of full marketing campaigns you can run


#    Hint: there is a built-in python function called min() that may be useful
#    Hint2:  you can solve this without conditionals.
#    self-check your function if you have budget of 400 for digital, 22 for TV and 125 for print your output should be 7
# """
def MarketingCampaign(DigitalAds, TVAds, PrintAds):
    # keep in mind that you can't have a partial ad, so we use // instead of /
    num_digital = DigitalAds // (7 * 1) # floor division: round the result down to the nearest whole number
    num_tv = TVAds // (3 * 1)
    num_print = PrintAds // (6 * 1)

    num_campains = min([num_digital, num_print, num_tv])
    # print("you can run {} marketing campains".format(num_campains))
    print(f"you can run {num_campains} marketing campains")

MarketingCampaign(400, 22, 125)


'''
2B. make a second function that also asks the user to input the current prices for the three 
types of ads before calculating the number of marketing campaigns that can be run at the new
prices.
NOTE: a single marketing campaign still consists of: 
    7 digital ads (cost per add to be input by user)
    3 television ads (cost per add to be input by user)
    6 print ads (cost per add to be input by user)

'''
def MarketingCampaign2(DigitalAds, TVAds, PrintAds):
    # keep in mind that you can't have a partial ad, so we use // instead of /

    while True:
        cost_of_digital = input("What's the price of Digital Ads? ")
        cost_of_tv = input("What's the price of TV Ads? ")
        cost_of_print = input("What's the price of Print Ads? ")
        
        try:
            cost_of_digital = float(cost_of_digital)
            cost_of_tv = float(cost_of_tv)
            cost_of_print = float(cost_of_print)
            break
        except:
            print("Error. One or more of the add priced entered is not a number. Please try again.")
    
    num_digital = DigitalAds // (7 * cost_of_digital)
    num_tv = TVAds // (3 * cost_of_tv)
    num_print = PrintAds // (6 * cost_of_print)

    num_campains = min([num_digital, num_print, num_tv])
    print("you can run {} marketing campains".format(num_campains))

MarketingCampaign2(400, 22, 175)