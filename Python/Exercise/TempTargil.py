temp = input("enter the tempuery")
temp = temp.lower()
tav = temp[-1] #C or F
floatn = float(temp[0:-1]) # this is temp

if tav =='c':
    n =((9*floatn)+(32*5))/5
    tav = 'F'
else:
    n =(5*floatn-160)/9
    tav = 'C'

print(n,tav)