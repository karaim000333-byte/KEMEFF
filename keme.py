
import os
import json
import requests
import time

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"
X = "\033[0m"

API_URL = "YOUR_API_ENDPOINT"
API_KEY = "YOUR_API_KEY"

def banner():
    os.system("clear")
    print(R + r"""
 _  __ _____ __  __ _____
| |/ /| ____|  \/  | ____|
| ' / |  _| | |\/| |  _|
| . \ | |___| |  | | |___
|_|\_\|_____|_|  |_|_____|

       FREE FIRE TOOL
""" + X)
    print(C + "        KEME TEAM" + X)
    print("-" * 40)

def search_player(uid, region):
    if "YOUR_API_ENDPOINT" in API_URL:
        print(R + "API is not configured yet!" + X)
        print(Y + "Add a valid API endpoint and API key first." + X)
        return

    try:
        headers = {"x-api-key": API_KEY}
        params = {"uid": uid, "region": region}

        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=20
        )
        response.raise_for_status()
        data = response.json()

        print(G + "\nPLAYER INFORMATION" + X)
        print(json.dumps(data, indent=4, ensure_ascii=False))

    except requests.RequestException as error:
        print(R + "Connection Error: " + str(error) + X)
    except ValueError:
        print(R + "Invalid API response!" + X)

def main():
    while True:
        banner()

        print(W + """
[1] Search Player By ID
[2] Player Level
[3] Account Information
[4] Guild Information
[5] Player Statistics
[6] Rank Information
[7] Check Player ID
[0] Exit
""" + X)

        choice = input(C + "KEME >> " + X).strip()

        if choice == "0":
            print(G + "Thanks for using KEME!" + X)
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print(R + "Invalid option!" + X)
            time.sleep(1)
            continue

        uid = input(Y + "\nEnter Player ID: " + X).strip()

        if not uid.isdigit():
            print(R + "Invalid Player ID!" + X)
            input("Press Enter...")
            continue

        region = input("Enter Region (me/sg/ind/br): ").strip().lower()

        if not region:
            region = "me"

        search_player(uid, region)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
