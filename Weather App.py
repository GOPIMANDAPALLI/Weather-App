#import tkinter
from tkinter import *
from tkinter import ttk
import requests
from key import API_KEY #import API_KEY value from key file

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+f"&appid={API_KEY}").json()
    country_label1.config(text=data["sys"]["country"])
    weather_label1.config(text=data["weather"][0]["main"])
    weather_description_label1.config(text=data["weather"][0]["description"])
    temperature_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pressure_label1.config(text=data["main"]["pressure"])
    wind_speed_label1.config(text=data["wind"]["speed"])

weather=Tk()
weather.title("Mini Weather App")
weather.config(bg="pink")
weather.geometry("500x850")

name_label=Label(weather,text="WEATHER APP",font=("Times new Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()

#intilize country wise city names

list_name=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
           "Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
           "Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
           "Tripura","Uttar Pradesh","Uttarakhand","West Bengal","New York", "Los Angeles", "Chicago",
           "Houston", "Phoenix","Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose","London",
           "Birmingham", "Manchester", "Liverpool", "Leeds","Sheffield", "Bristol", "Glasgow", "Leicester",
           "Edinburgh", "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa","Edmonton", "Winnipeg",
           "Quebec City", "Hamilton", "Kitchener",      "Sydney", "Melbourne", "Brisbane", "Perth",
           "Adelaide","Canberra", "Gold Coast", "Newcastle", "Wollongong", "Hobart","Berlin", "Hamburg",
           "Munich", "Cologne", "Frankfurt","Stuttgart", "Düsseldorf", "Leipzig", "Dortmund", "Essen",
           "Paris", "Marseille", "Lyon", "Toulouse", "Nice","Nantes", "Strasbourg", "Montpellier", "Bordeaux",
           "Lille","Beijing","Shanghai", "Guangzhou", "Shenzhen", "Chengdu","Wuhan", "Xi'an", "Hangzhou",
           "Nanjing", "Tianjin","São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza",
           "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre", "Tokyo", "Yokohama", "Osaka",
           "Nagoya", "Sapporo","Fukuoka", "Kobe", "Kyoto", "Sendai", "Hiroshima"
           ]

com=ttk.Combobox(weather,values=list_name,font=("Times new Roman",20,"bold"),textvariable=city_name)
com.place(x=50,y=120,height=50,width=400)

country_label=Label(weather,text="Country",font=("Times new Roman",20))
country_label.place(x=20,y=260,height=50,width=210)
country_label1=Label(weather,font=("Times new Roman",20))
country_label1.place(x=250,y=260,height=50,width=210)

weather_label=Label(weather,text="Weather Climate",font=("Times new Roman",20))
weather_label.place(x=20,y=330,height=50,width=210)
weather_label1=Label(weather,font=("Times new Roman",20))
weather_label1.place(x=250,y=330,height=50,width=210)

weather_description_label=Label(weather,text="Weather Description",font=("Times new Roman",17))
weather_description_label.place(x=20,y=400,height=50,width=210)
weather_description_label1=Label(weather,font=("Times new Roman",20))
weather_description_label1.place(x=250,y=400,height=50,width=210)

temperature_label=Label(weather,text="Temperature",font=("Times new Roman",20))
temperature_label.place(x=20,y=470,height=50,width=210)
temperature_label1=Label(weather,font=("Times new Roman",17))
temperature_label1.place(x=250,y=470,height=50,width=210)

pressure_label=Label(weather,text="Pressure",font=("Times new Roman",20))
pressure_label.place(x=20,y=540,height=50,width=210)
pressure_label1=Label(weather,font=("Times new Roman",17))
pressure_label1.place(x=250,y=540,height=50,width=210)

wind_speed_label=Label(weather,text="Wind Speed",font=("Times new Roman",20))
wind_speed_label.place(x=20,y=610,height=50,width=210)
wind_speed_label1=Label(weather,font=("Times new Roman",17))
wind_speed_label1.place(x=250,y=610,height=50,width=210)

#done_button is used to search the current weather in the city

done_button=Button(weather,text="DONE",font=("Times new Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

weather.mainloop()
