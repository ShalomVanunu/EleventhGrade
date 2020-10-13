

first , Second = 10,20
print(first, Second)

print(" the first grade is %s , and the second grage %s"%(first,Second))
print(f" the first grade is {first}, and the second grage {Second}")
print(" the first grade is {0} , and the second grage {1}".format(first,Second))

print("________________________________________________________________")

def picnic_shopping(list_of_prices):
    total = sum(list_of_prices)
    is_total_ok = total < 150
    return total, is_total_ok


print(picnic_shopping([20,30,40]))
print(type (picnic_shopping([20,30,40])))
print(picnic_shopping([20,30,40])[0])

