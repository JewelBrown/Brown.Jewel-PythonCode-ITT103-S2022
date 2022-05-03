#Jewel Brown
#May 2 2022
#Course: ITT103
#Purpose: Program designed for calculating and printing the commission received by a salesperson

#This statement uses nested function calls to get salesperson number as well as assign value to the variable
nu_mber= int(input ('Enter salesperson number: '))

#This statement uses nested function calls to get sales amount as well as assign value to the variable
sales= int(input ('Enter sales amount: '))

#This statement uses nested function calls to get class as well as assign value to the variable
cl_ass= int(input ('Enter class: '))

#function to calculate commission for salesperson
def calculate_commission(sales):
    
#If statement determining if class is 1
 if cl_ass == 1:
     
    #If statement to determine the value of sales
    if sales <=1000:
        
        #Calculation of commission for class 1 salesperson
        commission = sales * 0.06
        
    #Checking if sales is less than 2000 to determine the commission 
    elif 1000 < sales < 2000:
        
        #Calculation of commission for class 1 salesperson
        commission = sales * 0.07
    else:
        
        #Calculation of commission for salesperson
        commission = sales * 0.10

        
 #If statement determining if class is 2,if class is not 1
 elif cl_ass == 2:
     
    #If statement to determine the value of sales
    if sales < 1000:
        
        #Calculation of commission for class 2 salesperson
        commission = sales * 0.04
    else:
        
        #Calculation of commission for class 2 salesperson
        commission = sales * 0.06
        
 #If statement determining if class is 3, if class is not 2 
 elif cl_ass == 3:
     
    #Calculation of commission for class 3 salesperson
    commission = sales * 0.045
 else:
     
    #Error message
    print( 'Sorry but the class is invalid. Please try again.')
    
 #commission is returned to the function call
 return commission

#function call
commission = calculate_commission(sales)

#Output statement displaying the commission
print('The commission is:', commission)
    
    
