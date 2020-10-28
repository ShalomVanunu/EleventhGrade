

list_dict = {"notepad": 5 , "pen": 2,"folder" :7  }


user_basket = []
user_list = input("enter what you want to buy and quantity :\n")
while user_list != "END":
    user_basket.append(user_list)
    user_list = input('')
print(user_basket)

sum1 =0

for i in range(1,len(user_basket),2):
    amount = int(user_basket[i])
    item = user_basket[i-1] # item
    print(item)
    cost = list_dict[item] #cost of item
    print(cost)
    sum1 += cost*amount
    print(sum1)