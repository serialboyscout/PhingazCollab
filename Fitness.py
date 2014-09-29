
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
