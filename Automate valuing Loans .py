#!/usr/bin/env python
# coding: utf-8

# In[7]:


#"""Part 1: Automate the Calculations.

loan_costs = [500, 600, 200, 1000, 450]
a=len(loan_costs)   # number of loans
b=sum(loan_costs)   #sum of loans
avg=b/a             #average of loans
print("number of loans: " + str(a))
print("total value of costs: "+ str(b))
print("average loan amount: " + str(avg))


# In[25]:


#"""Part 2: Analyze Loan Data.

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")              #Extract 'future value'
remaining_months = loan.get("remaining_months")      #Extract 'remaining months'

print("future Value: " + str(future_value))          #Extract 'future value'
print("remaining Months: " + str(remaining_months))  #Extract 'remaining months'

discount_rate = .20

present_value = future_value/ (1+(discount_rate/12))**remaining_months

print("present value: " + str(present_value))

loan_price = loan.get("loan_price")

if (present_value > loan_price):                     # conditional statement to determine and print the loan's fair value
    print('the loan is worth at least the cost to buy it')
else: 
    print('loan is too expensive and not worth the price')
    


# In[6]:



# """Part 3: Perform Financial Calculations.


new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")


def present_value(future_value, remaining_months, discount_rate):   #new function to calculate present value, parameters included and present_value returned
    b=future_value/(1+(discount_rate/12))**remaining_months
    return (b)

get_present_value = present_value(future_value, remaining_months,0.2)


print("present value: " + str(get_present_value))


# In[85]:


#"""Part 4: Conditionally filter lists of loans.


inexpensive_loans = []   #empty list, inexpensive_loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]



for x in loans:                                  # for loop to determine if loan_price is less than 500
    if (x.get("loan_price") <= 500):
        inexpensive_loans.append(x)              #Append the inexpensive_loans list with loan_price that are less than 500
print("inexpensive list: "+ str(inexpensive_loans)) #Print the inexpensive_loans list
            
            


# In[5]:


#"""Part 5: Save the results.

inexpensive_loans = []
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


for x in loans:
    if (x.get("loan_price") <= 500):
        inexpensive_loans.append(x)
           
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

import csv
with open('inexpensive_loans.csv', mode='w') as inexpensive_loan:                       #open a new CSV file
    inexpensive_writer = csv.writer(inexpensive_loan ,  delimiter=',', quotechar='"')  #Create csvwriter using the csv library. 
    inexpensive_writer.writerow(header)                                               #csvwriter to write the header variable in the first row
    for x in inexpensive_loans :                                                      #for loop to iterate through each loan in inexpensive
        inexpensive_writer.writerow(x.values())                                       #csvwriter to write the loan.values() to a row in the CSV file
   
output_path = Path("inexpensive_loans.csv")


# In[ ]:




