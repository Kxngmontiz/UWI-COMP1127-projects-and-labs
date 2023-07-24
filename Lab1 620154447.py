def mystery():

     lastDigit = input("Enter last digit of your cellphone number: ")
     lastDigit = int (lastDigit)
     birthYear = input("Enter your year of birth: ")
     birthYear = int (birthYear)

     result = ((((lastDigit * 2) + 5) * 50)  + 1772)- birthYear

     return result

def fuzzbiz(num):

    if num%3 == 0 and num%5 == 0:

        return "FuzzBiz"
 
    elif num % 3 == 0:

        return "Fuzz"

    elif num % 5 == 0:

          return "Biz"
    
    else:
          return "No Fuzz No Biz"


def isLeapYear(year):

     if year % 4 == 0 and year % 100 != 0:

           return True
          
     elif year % 100 == 0 and year % 400 == 0:
          
          return True
     else:
          
          return False

    
