import discord
from discord.ext import commands
import json
import requests
import datetime
@client.command()
async def weather(ctx,*, location):
    mykey = 'YOURAPIKEY' #get your api key from https://openweathermap.org/
    link = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+mykey
    api_link = requests.get(link)
    api_data = api_link.json()

    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    feelslike_temp = ((api_data['main']['feels_like']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    visibility = api_data['visibility']
    #date_time = datetime.date().strftime("%d %b %Y | %I:%M:%S %p") {round(client.latency * 1000)}

    title = f'⛅ Weather Information for {location}.'

    description = f'🌡️ Temperature: {round(temp_city * 1)}°C \n \n 🔥 Feels Like: {round(feelslike_temp * 1)}°C \n \n☁️ Type: {weather_desc}. \n \n 🥵 Humidity: {hmdt}. \n \n 💨 Wind Speed: {wind_spd} km/h \n \n 👀 Visbility: {visibility} Metres'

    embed = discord.Embed(title = title, description = description, color = discord.Colour.orange())
    await ctx.send(embed=embed)
