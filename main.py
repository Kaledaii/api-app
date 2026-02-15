import requests
from random import randint as r 

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
    url="https://api.freeapi.app/api/v1/public/quotes/random"
    try:
        response=requests.get(url)
        data=response.json()
        range=r(0, len(data)-1)
        author=data[range]['author']
        quote=data[range]['content']
        print(f"Quote: {quote}\nAuthor: {author}")
        user=input("Click 1. to get another quote\nClick 2. to exit\n")
        if user=='1':
            quote()
        else: print("Goodbye!")
    except Exception as e:
        print("Error fetching quote:", e)
  


def main():
    user=input("Click 1. to get a joke\nClick 2. to get a quote\nClick 3. to exit\n")
    if user=='1':
        joke()
    elif user=='2':
        quote()
    else: print("Goodbye!")


if __name__=="__main__":
    main()