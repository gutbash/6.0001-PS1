# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:31:24 2020

@author: 4gutz
"""

#static information
down_payment_rate = 0.25
annual_savings_rate = 0.04

#calculate down payment
def down_payment():
    
    #state counter variables
    current_savings = 0
    months = 0
    
    #get user data
    print('Please enter the following information...')
    
    total_cost = float(input('Total Home Cost: '))
    annual_salary = float(input('Annual Salary: '))
    monthly_salary_rate = float(input('Monthly Salary Saved Percentage (Decimal): '))
    
    #calculate down payment on house
    down_payment = total_cost * down_payment_rate
    #calculate monthly salary from annual
    salary_monthly = annual_salary / float(12)
    #calculate percentage of monthly salary saved
    monthly_salary_saved = salary_monthly * monthly_salary_rate
    
    #calculate monthly accumulation
    print('Thank you. Calculating...')
    
    #adds to savings until meets down payment requirement
    while not current_savings >= down_payment:
        
        #adds interest earned
        current_savings += (current_savings * annual_savings_rate) / float(12)
        #adds base salary saved
        current_savings += monthly_salary_saved
        #adds to month count
        months += 1
        
    return f'It will take {months} months to save for a ${down_payment} down payment with an ending ${current_savings} in savings'

#start program        
print(down_payment())