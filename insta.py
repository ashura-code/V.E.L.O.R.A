import requests


def information(username):
    # username = input("enter your username: ")

    url = f"https://instagram174.p.rapidapi.com/api/v1/user/{username}/id"

    headers = {
        "X-RapidAPI-Key": "cc7365826amsh843b939188aa9ebp14e9dajsn4316a1950472",
        "X-RapidAPI-Host": "instagram174.p.rapidapi.com"
    }
    data = requests.get(url, headers=headers)
    ide = data


    try:
        idw =data.json()["result"]
    except:
        ide = data.json()




    if ide["status"] == "failed":
        print("No username found")
        # id = data.json()['result']
    else:

        print("Got into the database ,checking now...")

        url = f"https://instagram174.p.rapidapi.com/api/v1/user/{idw}/info"

        headers = {
            "X-RapidAPI-Key": "cc7365826amsh843b939188aa9ebp14e9dajsn4316a1950472",
            "X-RapidAPI-Host": "instagram174.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)


        info = (response.json())
        print(info)
        if info['status'] == "failed":
            print("No account found or something went wrong.")
        # print(info)
        else:
            print("Username:  ", info['result']['username'])
            print("Fullname: ", info['result']['full_name'])
            print("Description: ", info['result']['biography'])
            print("Followers: ", info['result']['follower_count'])
            print("Following: ", info['result']['following_count'])
