import time
now = (time.strftime("%H : %M : %S"))
if now < "12 : 00 : 00":
    print("Good morning! It's ", now)
elif now < "17 : 00 : 00":
    print("Good afternoon! It's ", now)
elif now < "21 : 00 : 00":
    print("Good evening! It's ", now)
else:
    print("Good night! It's ", now)