import matplotlib.pyplot as plt
from dataCollection import last_Name, current_Rating, max_Rating, friend_Count
from userPompt import prompt
from sys import exit
from generateColor import generate_Color


def final_Plot():
    while True:
        prompt()
        Choice = int(input("\t   Enter Your Choice : "))
        if Choice == 1:
            C = generate_Color(current_Rating)
            plt.bar(last_Name, current_Rating, color=C)
            plt.title("Current Rating Vs User", fontsize=15)
            plt.xlabel("Last Name or User Name")
            plt.ylabel("Current Rating")
            plt.show()
        elif Choice == 2:
            C = generate_Color(max_Rating)
            plt.bar(last_Name, max_Rating, color=C)
            plt.title("Max Rating Vs User", fontsize=15)
            plt.xlabel("Last Name or User Name")
            plt.ylabel("Maximum Rating")
            plt.show()
        elif Choice == 3:
            # Current
            current_Color = generate_Color(current_Rating)
            plt.subplot(2, 2, 1)
            plt.bar(last_Name, current_Rating, color=current_Color)
            plt.title("Current Rating Vs User", fontsize=15)
            plt.xlabel("Last Name or User Name")
            plt.ylabel("Current Rating")

            # Max
            max_Color = generate_Color(max_Rating)
            plt.subplot(2, 2, 2)
            plt.bar(last_Name, max_Rating, color=max_Color)
            plt.title("Max Rating Vs User", fontsize=15)
            plt.xlabel("Last Name or User Name")
            plt.ylabel("Maximum Rating")

            # Final
            plt.suptitle("Current & Max Rating Vs User", fontsize=20)
            plt.show()
        elif Choice == 4:
            plt.barh(last_Name, friend_Count, color="Black")
            plt.title("Total Friend Vs User", fontsize=15)
            plt.ylabel("Last Name or User Name")
            plt.xlabel("Total Friend")
            plt.show()
        elif Choice == 5:
            exit("\t   Exited ^_+ ")
