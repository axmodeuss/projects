import sys
import requests
import json

if len(sys.argv) >1 :
    username = sys.argv[1]

    r = requests.get(f"https://api.github.com/users/{username}/events")
    if r.status_code != 200 :
        print("User not found")
    else:
        print(r.status_code)
        data = r.json()
        # print(json.dumps(data,indent=4))
        
        for event in data:
            print(f"{event+1} = >")
            if event["type"] == "PushEvent":
                print(f"Pushed to {event["repo"]["name"]}")
            elif event["type"] == "CreateEvent":
                print(f"Created {event["repo"]["name"]}")
            elif event["type"] == "WatchEvent":
                print(f"Watch {event["repo"]["name"]}")
            elif event["type"] == "ForkEvent":
                print(f"fork {event["repo"]["name"]}")
            elif event["type"] == "IssuesEvent":
                print(f"Isseues {event["repo"]["name"]}")
            print("\n ==============================")
    
    
    



else :
    print("Usage: python main.py <username>")