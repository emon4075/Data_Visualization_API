import requests

# Declaring Empty Lists
current_Rating = []
max_Rating = []
friend_Count = []
last_Name = []


def data_Collection():
    print()
    try:
        user_Name = input("\t   Enter User Name : ")
        response = requests.get(
            "https://codeforces.com/api/user.info?handles=" + user_Name
        ).json()
        if response["status"] == "OK":
            user_Info = response["result"][0]
            if "lastName" in user_Info and user_Info["lastName"]:
                last_Name.append(user_Info["lastName"])
            else:
                last_Name.append(user_Info["handle"])
            if "rating" in user_Info and user_Info["rating"]:
                current_Rating.append(user_Info["rating"])
            else:
                current_Rating.append(0)
            if "maxRating" in user_Info and user_Info["maxRating"]:
                max_Rating.append(user_Info["maxRating"])
            else:
                max_Rating.append(0)
            if "friendOfCount" in user_Info and user_Info["friendOfCount"]:
                friend_Count.append(user_Info["friendOfCount"])
            else:
                friend_Count.append(0)
        else:
            print(f"Error: {response['comment']}")
            last_Name.append("Invalid")
            current_Rating.append(0)
            max_Rating.append(0)
            friend_Count.append(0)
    except Exception as e:
        print(f"An Error Occurred: {e}")
