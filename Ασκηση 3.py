import urllib.request
import json
from datetime import date
import datetime

todaysDate = datetime.datetime.today()
month = todaysDate.month
if month < 10:
    month = str(0) + str(month)


print("")
print("   ------" + "KINO" + "-----")
print(" "*3 + "ballots of the month")
print("")
for tempDay in range(todaysDate.day):
    day = tempDay + 1
    if tempDay < 9:
        day = str(0) + str(tempDay + 1)

    print(f"First ballot of {todaysDate.year}-{month}-{day}")
    url = f"https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{month}-{day}/2021-{month}-{day}"
    temp = urllib.request.urlopen(url)
    temp = temp.read()
    data = json.loads(temp)
    for dataContent in data["content"]:
        if "winningNumbers" in dataContent:
            print("The winning numbers of kino are " +
                  str(dataContent["winningNumbers"]["list"]))
            break
    else:
        print("The ballot has not started yet...")
        print("-"*40)
        break

    print("-"*40)
