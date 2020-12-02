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



try:
    with open("file.txt", 'r') as reader:
        reader.read()

except OSError:
    print("OSError Type")

