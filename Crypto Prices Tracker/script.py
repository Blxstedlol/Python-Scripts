from plyer import notification
import requests
import time
def send_noti(title, msg):
    notification.notify(
        title=f"{title}",
        message=f"{msg}",
        timeout=5
    )

def get_crypto_price(crypto_id, vs_currency):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={vs_currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data[crypto_id][vs_currency]
        send_noti(f'{crypto_id} Price has changed', f'Price: {price}')
    else:
        return None
coin = 'nano' # making the script work for nano (XNO) 
currency = 'gbp' # making the script work for GBP
while True:
    get_crypto_price(coin, currency)
    time.sleep(30)
    # Change time for rate limiting

