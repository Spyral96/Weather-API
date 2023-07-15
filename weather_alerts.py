# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:32:29 2023

@author: Dan
"""
#First Github post!
######  imports/data points  ######################
import requests
from win10toast import ToastNotifier 
import pandas as pd
import webbrowser as wb
import smtplib
from email.message import EmailMessage
url =  'https://api.weatherbit.io/v2.0/current?key=22925c63ccdb4e5bbf1197647603cbad&units=I&city=New+York,New+York'
#########   loading dataframe   ########################

response = requests.get(url)

weather_data = response.json()

current_weather = pd.DataFrame(weather_data['data'])
current_weather.columns

#########  Accessing specific values ##################

rain = current_weather.iloc[0,17]
temp = current_weather.iloc[0,-10]

#########         variables          #############
rainy_link = "https://www.youtube.com/watch?v=sTt026NTQfE&ab_channel=DubstepGutter"
not_rainy = "https://www.youtube.com/watch?v=oLOyVDP_ckQ&ab_channel=VideoGamesMusic"

#########     functions               #############

###Rain?
def rain_music():
    if rain == 1:
        wb.open(rainy_link)
    elif rain == 0:
        wb.open(not_rainy)
    
###Temp?
temp_comment = ""

if temp >= 70: 
        temp_comment = f"Oh my gosh, it's {temp} degrees out! Turn on your AC!"
elif 55 <= temp <= 69:
        temp_comment = f"It's {temp} degrees. A boring day."
elif 0 <= temp <=54:
        temp_comment = f"BRRR... it's {temp} degrees out! Bring a coat."


#######             Command         ###############        

rain_music()

#######         Desktop Notification win #############
 
weather_update = ToastNotifier()


#if statment wether rain = 1 or 0 and prints depending string

if rain == 0:
    rain_statement = "it is not raining."
else:
    rain_statement = "it is raining"
    
#displaying notifaction
weather_update.show_toast("Todays Weather",f"{temp_comment} \nAlso {rain_statement}",duration=11)



#building email message

email_mess = f"Todays Weather {temp_comment} \nAlso {rain_statement}"


message = EmailMessage()
message['From'] = 'your email'
message['To'] = 'send to email'
message['Subject'] = 'Pokemon Daily Stats'
message.set_content(email_mess)
     
#connect with server
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()
     
     smtp.login('your email','temp password made from google')
     
    
     #send email  
     smtp.send_message(message)
   
#confirmation     
print("email has sent")
 

