import requests 

api_key = "cc4c8c0f47904947b3827addf7c2e83d"
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
response=requests.get(url)
if response.status_code == 200:
    # Request successful
    news_data=response.json()
    articles = news_data["articles"]
    for article in articles:
        title = article["title"]
        description = article["description"]
        print(f"Title: {title}")
        print(f"Description: {description}")
        print("-" * 50)
        print("\n")
        
else:
    # Request unsuccessful
    print("Error occurred while retrieving news data.")

