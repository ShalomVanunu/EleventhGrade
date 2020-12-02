"""
try:
הרץ את הקוד
אם נזרקת חריגה לעצור
וללכת ל except המתאים

except:
אם נזרקה חריגה,
הרץ הקוד הבא

else :
לא נזרקה אף חריגה
הרץ את קטע קוד הזה

 finally:
 בסוף תמיד הרץ
 את הקטע קוד הזה
"""

num1 = 6
num2 = input('write')

try:
    print(num1/int(num2))

except Exception as e: # catch the error

    if str(e) == 'division by zero':
       print(e)
    else:
       print ("the error is",e)

