def price_difference(initial_price, monthly_payment, num_months):
 
    if initial_price < 0 or monthly_payment < 0 or num_months < 0:
        print("All inputs must be incorrect numbers!try again with positive numbers. ")
        return None  

    total_installment_price = monthly_payment * num_months
    difference = total_installment_price - initial_price

    return difference


initial_price = float(input("the initial price of the product : "))
monthly_payment = float(input("the monthly payment : "))
num_months = int(input("the number of months : "))

difference = price_difference(initial_price, monthly_payment, num_months)

if difference is not None:  
    print(" The difference is : ",difference)
