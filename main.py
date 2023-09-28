import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url=f"https://www.boredapi.com/api/activity/{word}");
        # print(res);

        if res.status_code == 404:
            loop();

        else:
            data = res.json();
            print(data);
            print(res.status_code);
            print(word);

loop();

# res = requests.get("https://www.boredapi.com/api/activity");
# print(res);

# data = res.json();
# print(data);