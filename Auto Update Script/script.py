import requests
def check():
    url = 'https://raw.githubusercontent.com/Blxstedlol/Python-Scripts/main/Auto%20Update%20Script/version.txt'
    response = requests.get(url=url)
    if response == 200:
        latest_version = response.text
        with open('version.txt', 'r') as file:
            current_version = file.read()
            file.close()
        with open('version.txt', 'w') as file:
            if latest_version > current_version:
                file.write(latest_version)
                print('Latest Version has been installed!')
check()
