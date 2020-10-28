
count = 0

def user_choice(counter):
    number_choise = input("Plese enter a Number [Exit] :")
    counter +=1
    return int(number_choise), counter

def compare(num1,num2):
    if num1 > num2:
        return "High"
    elif num1 < num2 :
        return "Low"
    else: return "Equal"