actual_cost = float(input(" Please Enter the Actual Product Price:"))
sale_amount = float(input(" Please Enter the Sales Amount: "))


if(sale_amount > actual_cost):
    profit = sale_amount - actual_cost
    print("Profit=", profit)
elif(actual_cost > sale_amount):
    loss= actual_cost - sale_amount
    print("Loss=", loss)


else:
    print("No profit.. no loss!!")