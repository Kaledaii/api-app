import requests,os,csv
from random import randint 
from datetime import datetime, timedelta

def joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        joke_data = response.json()
        print(joke_data['joke'])
        with open("jokes.txt",'a')as f:
            f.write(joke_data['joke']+'\n')
        user=input("\nClick 1. to get another joke\nClick 2. to exit\n")
        if user=='1':
            joke()
        else: print("Goodbye!")
    except Exception as e:
        print("Error fetching joke:", e)    

def quote():
    url="https://api.freeapi.app/api/v1/public/quotes"
    try:
        response=requests.get(url)
        data=response.json()
        quote_list=data['data']['data']
        range=randint(0, len(quote_list)-1)
        author=quote_list[range]['author']
        content=quote_list[range]['content']
        print(f"{content}\n-{author}\n")
        with open("quotes.txt",'a')as f:
            f.write(f"{content}\n-{author}\n")
        user=input("Click 1. to get another quote\nClick 2. to exit\n")
        if user=='1':
            quote()
        else: print("Goodbye!")
    except Exception as e:
        print("Error fetching quote:", e)
  
def news(country='us',category='general'):
    api=f'9db0badab9c34cec86b29ccd96393d9c'
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api}"
   

    try:
        response=requests.get(url)
        data=response.json()
        articles=data.get('articles', [])
        if not articles:
            print("No news articles found.")
            return
        with open("news.txt",'a')as f:
            for i, article in enumerate(articles[:5], start=1):
                title = article.get("title", "No title")
                desc = article.get("description", "No description")
                url = article.get("url", "")
                date = article.get("publishedAt", "Unknown date")
                source = article.get("source", {}).get("name", "Unknown source")
                print(f"{i}. {title}\n   {desc}\n   Source: {source}, Date: {date}\n   URL: {url}\n")
                f.write(f"{i}. {title}\n   {desc}\n   Source: {source}, Date: {date}\n   URL: {url}\n\n")
    except Exception as e:
        print("Error fetching news:", e)

def weather(city="Kathmandu"):
    api='85d4e818f5941edafd29e1fe235a08d6' 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    try:
        response=requests.get(url)
        data=response.json()
        if response.status_code == 200:
            temp=data['main']['temp']
            desc=data['weather'][0]['description']
            feels_like=data['main']['feels_like']
            humidity=data['main']['humidity']
            pressure=data['main']['pressure']
            wind_speed=data['wind']['speed']
            wind_deg=data['wind']['deg']
            timestamp = data.get("dt")
            if timestamp:
               updated_dt = datetime.utcfromtimestamp(timestamp)
               now_dt = datetime.utcnow()
               # Calculate difference
               diff = now_dt - updated_dt
               minutes_ago = int(diff.total_seconds() // 60)
               if minutes_ago < 1:updated_time = "just now"
               elif minutes_ago == 1:
                updated_time = "1 minute ago"
               elif minutes_ago < 60:
                updated_time = f"{minutes_ago} minutes ago"
               else:
                hours_ago = minutes_ago // 60
                updated_time = f"{hours_ago} hours ago"
            else:
                updated_time = "Unknown"


            print(f"Weather in {city} (updated {updated_time}):")
            print(f"   Temperature: {temp}°C (feels like {feels_like}°C)")
            print(f"   Condition: {desc}")
            print(f"   Humidity: {humidity}%")
            print(f"   Pressure: {pressure} hPa")
            print(f"   Wind: {wind_speed} m/s, direction {wind_deg}°")
            with open("weather.csv","a",encoding="utf-8")as f:
                writer=csv.writer(f)
                writer.writerow([city,updated_time,temp,desc,humidity,pressure,wind_speed,wind_deg])
    except Exception as e:
        print("Error fetching weather:", e)

def main():
    user=input("Click 1. to get a joke\nClick 2. to get a quote\nClick 3. to get news\nClick 4. to get weather\nClick 5. to exit\n")
    if user=='1':
        joke()
    elif user=='2':
        quote()
    elif user=='3':
        country=input("Enter country code us/au/gb/in/ca/it/fr/de/jp/ru/sa/ae\n")
        category=input("Enter category business/entertainment/general/health/science/sports/technology\n")
        news(country,category)
    elif user=='4':
        city=input("Enter city name: ")
        weather(city)
    else: print("Goodbye!")


if __name__=="__main__":
    main()