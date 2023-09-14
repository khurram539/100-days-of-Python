# Day 32 - Send emails and manages dates


import smtplib

my_email = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password="XXXXXXXX")
    connection.sendmail(
        from_addr=my_email,
        to_addrs="xxxxxxxxxxx",
        msg="Subject:Hello\n\nThis is the body of my email."
    )