import requests

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

def main():
    user=input("Click 1. to get a joke\nClick 2. to exit\n")
    if user=='1':
        joke()
    else: print("Goodbye!")


if __name__=="__main__":
    main()