
""" Targil 1"""
list = [5,11,8,10,26,14,5,7,1,18]
def avarage(list):
    avarage_even = 0
    avarage_odd = 0
    # for even numbers
    count =0
    sum =0
    for number in list[1::2]:
        sum += number
        count += 1

    avarage_even =sum/count

    count = 0
    sum = 0
    for number in list[::2]:
        sum += number
        count += 1
    avarage_odd =  sum / count

    return avarage_even,avarage_odd


print(avarage(list))