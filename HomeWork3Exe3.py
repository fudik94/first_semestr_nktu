def price_difference(initial_price, monthly_payment, num_months):

    if initial_price < 0 or monthly_payment < 0 or num_months < 0:
        print("All inputs must be incorrect numbers!try again with positive numbers.")
        return None  

    total_installment_price = monthly_payment * num_months
    difference = total_installment_price - initial_price

    return difference

initial_price = float(input("The initial price of the product? "))
monthly_payment_1 = float(input("The monthly payment on the first installment plan? "))
num_months_1 = int(input("How many months does the first installment plan last? "))
monthly_payment_2 = float(input("The monthly payment on the second installment plan? "))
num_months_2 = int(input("How many months does the second installment plan last? "))


difference_1 = price_difference(initial_price, monthly_payment_1, num_months_1)
difference_2 = price_difference(initial_price, monthly_payment_2, num_months_2)


if difference_1 is not None and difference_2 is not None:
    if difference_1 < difference_2:
        print("The first installment plan is better!")
    elif difference_1 > difference_2:
        print("The second installment plan is better!")
    else:
        print("Bingo!Both installment plans are equally good!Good Boy!")
