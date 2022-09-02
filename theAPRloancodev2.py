# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:49:57 2022

@author: tyler nelson

8/22/2022
"""
#^ doc file
import numpy as np

#float pv 
#float r = 
#float nm = 
#Pmt =  r/1200*PV/(1-(1+(r/1200))**(-n)) 

def payment(pv, rapr, nmonths): 
    """
    
    Parameters
    ----------
    pv : TYPE floating point number
        DESCRIPTION. how much money you are borrowing.
    rapr : TYPE floating point number
        DESCRIPTION. annumal percent interest rate
    nmonths : TYPE int
        DESCRIPTION. number of months, term length of loan

    Returns
    -------
    Pmt: TYPE float
    
        DESCRIPTION. monthly payment

    """
    #PV = present value  # / = division # * = multiply # ** = expontent
    Pmt =  rapr/1200*pv/(1-(1+(rapr/1200))**(-nmonths)) 
    
    return Pmt

'''
write a loop 
input pv, n , rapr
print out the input variables 
print out the payment 
and loop back to get a new case
if present pv is put in as '0', exit the loop

'''
while(1):
    
    pv = input('input pv ')
    
    if pv == '0': #or if float(pv) == 0:
        break
    print(pv)
    
    apr = input('whats the apr ')
    nmonths = input('how many months ')
    
    pay = payment(float(pv),float(apr),float(nmonths))
    print(pay)
    
print('out of loop')

#pv = 41000
#n = 48
#rapr = 7



paymentDollars = payment(float(input('input pv '), 6, 38))
print('payment is {:.2f}'.format(paymentDollars))


amount = input('how much money you want?: ')
print(amount)


#carPayment = payment(pv, rapr, n)
#carPayment = payment(41232, 3.5, 36)

#print('car payment is: ${:.2f}'.format(round(carPayment),2))
#print('car payment is: ${:.2f}'.format(carPayment))