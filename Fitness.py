
''' Just a starting .py file for the github repository. Needed a file present to create a repository from Eclipse
    and commit to github.'''
from boto.dynamodb.condition import NULL
    
''' Looks good G!! JJB-123 '''



''' Odd or Even function
Uses the Modulus operator to determine Odd or Even '''
def OddorEven(n):
    if n % 2 == 0:
        print 'The integer is Even!'
        return 
    else:
        print 'The integer is Odd!'
        return 

#Class testing - Here I'll define a class
class User:
    # Create the User Name - Passing the name into the Function
    def setUserName(self, Name):
        self.Name = Name
    # Returning the User's Name
    def returnUserName(self):
        return self.Name
    # Create the User Age - Passing the age into the Function
    def setUserAge(self, Age):
        self.Age = Age
    # Returning the User's Age
    def returnUserAge(self):
        return self.Age
    # Weight info - Use Pounds
    def setUserWeight(self, Weight):
        self.Weight = Weight
    def returnUserWeight(self):
        return self.Weight
    # Height info - Use Inches
    def setUserHeight(self, Height):
        self.Height = Height
    def returnUserHeight(self):
        return self.Height
    # Use Weight and Height to determine BMI of the user
    def returnBMI(self):
        # This function is requires Height and Weight to be set
        # If either of these is NOT set - then tell the user it's missing them
        # This currently DOESN'T work however... The program errors without the values set
        if self.Weight is None or self.Height is None:
            print 'Need Height and Weight value to calculate. Please provide both.'
            return
        else:
            BMI = (self.Weight * 703)/(self.Height * self.Height) 
            print 'Your BMI is %d' %BMI
            return 
    
    

'''MAIN START'''
import random
    
intTest = random.randint(0,100)

# This IF statement just looks to see if the random is bigger or smaller than 50  
if intTest >= 50:
    print 'The random # is bigger than 50'
else:
    print 'The random # is smaller than 50'

# This function returns an Odd or Even statement 
OddorEven(intTest)

print(intTest)

print 'Check out this integer: %d' % intTest


''' Class code is below here '''
# Creating some Class instances - First 'Jason' Object
Jason = User()
# Pass the name to the Class for the Name variable
Jason.setUserName('Jason')
# Pass the age to the Class Object Jason for the Age variable
Jason.setUserAge(30)
# Return both of them
print 'Hello, my name is %s' %Jason.returnUserName() 
print 'I am %d' %Jason.returnUserAge()
# Do math with a Class Variable 
print 'In 10 years I will be %d' %(Jason.returnUserAge() + 10)

# Testing BMI and Height and Weight settings
Jason.setUserWeight(170)
Jason.setUserHeight(12*6)

print Jason.returnUserWeight()
print Jason.returnUserHeight()

# I don't need a Print statement here - this function contains the Print statement
Jason.returnBMI()




