import requests
def check():
    version_url = 'https://raw.githubusercontent.com/Blxstedlol/Python-Scripts/main/Auto%20Update%20Script/version.txt'
    response = requests.get(url=version_url)
    latest_version = response.text
    print(latest_version)
    with open('version.txt', 'r') as file:
        current_version = file.read().strip()
        
        print(current_version)
    if current_version < latest_version:
        with open('version.txt', 'w') as file:
            file.write(f'{latest_version}')
            print('Updated Version.txt')
    
check()
