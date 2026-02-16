from unicodedata import category
import requests
from random import randint 

def joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        joke_data = response.json()
        print(joke_data['joke'])
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
        user=input("Click 1. to get another quote\nClick 2. to exit\n")
        if user=='1':
            quote()
        else: print("Goodbye!")
    except Exception as e:
        print("Error fetching quote:", e)
  
def news(country='us',category='general',query=None):
    if country == 'us':
        # US works fine on free tier
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=YOUR_API_KEY"
    else:
        # fallback for other countries
        search_term = query if query else country
        url = f"https://newsapi.org/v2/everything?q={search_term}&apiKey=YOUR_API_KEY"

    try:
        response=requests.get(url)
        data=response.json()
        articles=data.get('articles', [])
        if not articles:
            print("No news articles found.")
            return
        for i, article in enumerate(articles[:5], start=1):
            title = article.get("title", "No title")
            desc = article.get("description", "No description")
            url = article.get("url", "")
            date = article.get("publishedAt", "Unknown date")
            source = article.get("source", {}).get("name", "Unknown source")
            print(f"{i}. {title}\n   {desc}\n   Source: {source}, Date: {date}\n   URL: {url}\n")
    except Exception as e:
        print("Error fetching news:", e)

def weather():
    api='88c229e46cd428771d88b819e1ae885d'
    url=f''

def main():
    user=input("Click 1. to get a joke\nClick 2. to get a quote\nClick 3. to get news\nClick 4. to exit\n")
    if user=='1':
        joke()
    elif user=='2':
        quote()
    elif user=='3':
        country=input("Enter country code us/au/gb/in/ca/it/fr/de/jp/ru/sa/ae\n")
        category=input("Enter category business/entertainment/general/health/science/sports/technology\n")
        query=input("Enter a keyword to search for news (optional, press enter to skip): ")
        news(country,category,query)
    else: print("Goodbye!")


if __name__=="__main__":
    main()