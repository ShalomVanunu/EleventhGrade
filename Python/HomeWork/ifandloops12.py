x=3#ערך ראשוני
i=0#ערך ראשוני
while (i<3):#ניכנס ללולאה מכיוון שi=0
    x+=1#אם בכל הרצה של הלולאה מגדילים את i ב 1 אז מ0 ל1 ומ1 ל2 ומ2 ל3 זה 3 הרצות של פנים הלולאה ולכן בסוף x+=3
    i+=1#הלולאה רצה 3 פעמים אם נגדיל את i ב1 כשערך התחלתי הוא 0 ולכן כשi=3 לא ניכנס ללולאה
print (x)#חשוב לזכור שההדפסה נמצאת מחוץ ללולאה ולכן רק הx הסופי יודפס. הבנו שבלולאה סיכום הפקודות הוא x+=3 והערך ההתחלתי הוא 3
#לכן נדפיס 3+3 =6