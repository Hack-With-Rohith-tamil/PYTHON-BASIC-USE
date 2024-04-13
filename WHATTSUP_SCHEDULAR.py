""" BEST SCHEDULAR TO SEND WHATTSUP MESSAGE EARLIER WHEN YOU WANT
                      --> BY HACK WITH ROHIT TAMIL"""
import pywhatkit
import pyfiglet

msg = pyfiglet.figlet_format("Hack With Rohit")
print(msg)

phone_number = input("Enter the phone number : ")
msg = input("Enter the message : ")
hour = int(input("Enter hour : "))
minutes = int(input("Enter minute : "))

pywhatkit.sendwhatmsg(phone_number,msg,hour,minutes)
