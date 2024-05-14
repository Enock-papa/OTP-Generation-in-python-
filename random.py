import os
import math
import random
import smtplib
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp =  "Your Random number Generated is" + OTP

msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("generatorotp1@gmail.com", "kpidpefymqqjpxbb")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")