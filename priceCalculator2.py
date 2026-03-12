# Phone types with their prices are stored in a dictionary
phoneProfit = {"Apple iphone": 120.45, "Android Phone": 99.50, "Apple Tablet":75.69, "Android Tablet": 65.73, "Windows Tablet": 51.49}
# This dictionary is used for matching user input with a corresponding type of phone
indexController={1: "Apple iphone", 2: "Android Phone", 3: "Apple Tablet", 4: "Android Tablet", 5: "Windows Tablet"}

days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Stores the final output of the total profit
totalProfit=0.0
# Used for Calculating price based on two parameters given which are the type of phone and number of items that are defined from the user
def calculate_profit(phoneType,numberOfItems):
  global totalProfit
  itemProfit=phoneProfit[phoneType]*numberOfItems
  totalProfit+=itemProfit
# This function is used for calling the calculate_profit function so that the total profit will be calculated until the user input is 0
def mainHelper(productNumber):
  while(productNumber!=0):
      quantity=int(input("Enter quantity sold: \n")) # getting the amount
      itemSelected=indexController[productNumber] #Getting type of product from the user
      calculate_profit(itemSelected,quantity) #passing those two arguments to calculate the profit
      productNumber=int(input("Enter product number 1-5, or enter 0 to stop.\n"))
      # If the product number or item defined from the user is outside of the requirements it will force the user to put a valid number
      while(productNumber<0 or productNumber>5):
        print("Invalid input, please enter a valid number")
        productNumber=int(input("Enter product number 1-5, or enter 0 to stop.\n"))
#The main function will be used to execute the whole logic
def main(inputNumber):
  if(inputNumber==1):
    daySelected=input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n")

    print(f"For {daySelected}:")
    productNumber=int(input("Enter product number 1-5 or enter 0 to stop.\n"))
    mainHelper(productNumber) # Passing the item selected for calculating its profit
    
    print(f"Total Profit for the {daySelected} is: ${totalProfit:.2f}.")
    #Checking if the day exceeds the profit target
    if(totalProfit>10000):
      print(f"You did well this {daySelected}! Keep up the great work!")
    else:
      print(f"More hard work needed... The last {daySelected} wasn't the best")
  elif(inputNumber==2):
    #It will iterate the whole days of the week by getting input from user for the items selected
    for day in days:
      print(f"For {day}:")
      productNumber=int(input("Enter product number 1-5 or enter 0 to stop.\n"))
      mainHelper(productNumber)

    print(f"Total Profit for the week is: ${totalProfit:.2f}.")
    #Checking if the week exceeds the profit target
    if(totalProfit>10000):
      print("You did good this week")
    else:
      print("More hard work needed... The last week wasn't the best")
  elif(inputNumber==3):
    #It will iterate only the week days  by getting input from user for the items selected
    for day in days[:5]:
      print(f"For {day}:")
      productNumber=int(input("Enter product number 1-5 or enter 0 to stop.\n"))
      mainHelper(productNumber)

    print(f"Total Profit for the week (business days) is: ${totalProfit:.2f}.")
    #Checking if the week (business days) exceeds the profit target
    if(totalProfit>10000):
      print("You did good this week (business days)")
    else:
      print("More hard work needed... The last week (business days) wasn't the best")
  elif(inputNumber==4):
    #It will iterate only the weekend days by getting input from user for the items selected
    for day in days[5:]:
      print(f"For {day}:")
      productNumber=int(input("Enter product number 1-5 or enter 0 to stop.\n"))
      mainHelper(productNumber)

    print(f"Total Profit for the weekend is: ${totalProfit:.2f}.")
    #Checking if the weekend exceeds the profit target
    if(totalProfit>10000):
      print("You did good this weekend")
    else:
      print("More hard work needed... The last weekend wasn't the best")
  elif(inputNumber==0):
    print("Program End!")
  else:
    print("Invalid input, please enter a valid input")

print("Welcome to Circle Phones profit calculator.\n")
print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend\n")
inputNumber=int(input("Enter:\n 1 - For specifc Day\n 2 - For the Week\n 3 - For Week Business Days\n 4 - For Weekend days\n 0-Exit\n"))


main(inputNumber)
