
s = "my name is shalom"
#    my na*e is shalo*
#    *y na*e is shalo*
new =[]
for i in  s:
    if i == s[0]:
        new.append("*")
    else:
        new.append(i)
    new[0]= s[0]
print("".join(new))


value = s[0] +s[1::].replace("m","*")
print(value)

