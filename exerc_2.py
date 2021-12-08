import functools


def function(num, item):
    return num + 1


password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")

# נכון:תשובה נכונה. הפונקציה reduce מקבלת את הסיסמה שהזין המשתמש כרשימת מספרים,
# ולוקחת את ערך האיבר הראשון ברשימה ומוסיפה לו את הערך 1 עבור כל איבר נוסף ברשימה. בהמשך, ביטוי הלמבדה בודק
# האם תוצאת החישוב מתחלקת ב-4 ואם כן מודפס הפלט "!Correct password".
# הערך הראשון בסיסמה הוא 1, ויש עוד שלושה איברים ברשימה, לכן מחברים לערך זה 1 + 1 + 1,
# ומתקבלת התוצאה 4. מאחר ו-4 מתחלק ב-4 ללא שארית, מתקבל הפלט המבוקש.
