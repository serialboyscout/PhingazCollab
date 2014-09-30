
''' Just a starting .py file for the github repository. Needed a file present to create a repository from Eclipse
    and commit to github.'''
    
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
    def createUserName(self, Name):
        self.Name = Name
    # Returning the User's Name
    def returnUserName(self):
        return self.Name
    # Create the User Age - Passing the age into the Function
    def createUserAge(self, Age):
        self.Age = Age
    # Returning the User's Age
    def returnUserAge(self):
        return self.Age
    

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
Jason.createUserName('Jason')
# Pass the age to the Class Object Jason for the Age variable
Jason.createUserAge(30)
# Return both of them
print 'Hello, my name is %s' %Jason.returnUserName() 
print 'I am %d' %Jason.returnUserAge()
# Do math with a Class Variable 
print 'In 10 years I will be %d' %(Jason.returnUserAge() + 10)




