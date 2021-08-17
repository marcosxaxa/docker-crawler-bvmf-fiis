import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import mongo


# Function to retrieve a list of fiis and save it to dynamoDB
now = datetime.now()
today = now.strftime("%Y-%m-%d")
delta_last_month = now - timedelta(days=30)
last_month = str(delta_last_month.strftime("%m/%y"))
current_month = str(now.strftime("%m/%y"))

def get_fii_list():
    # URL to retrieve the data from
    URL = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'
    content = requests.get(URL)
    soup = BeautifulSoup(content.text, 'html.parser')
    # Get the occurencies of class ticker to the variable rows
    rows = soup.find_all("span", {"class": "ticker"})
    # Defines the list to save all the fiis
    fii_table = []
    # Loop to parse and correct every fii ticker and save it to the list
    for row in rows:
        # Get the text from the Beatifulsoup variable
        fii_ticker = row.get_text()
        fii_ticker = fii_ticker.split(sep='"div", {"class": "stylelistrow"}')
        # Append the correct value to the list
        fii_table.append(fii_ticker[0])
    return fii_table


def get_price(fii_ticker):
    fii_price = {}
    base_url = 'https://statusinvest.com.br/fundos-imobiliarios/'
    URL = base_url + fii_ticker.lower()
    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    content = requests.get(URL, headers=headers)
    soup = BeautifulSoup(content.text, 'html.parser')
    for quote in soup.find(
            'div', attrs={'title': 'Valor atual do ativo'}).find_all('strong'):
        quote = quote.text
        quote = quote.replace('.', '').replace(',','.')
    fii_price["ticker"] = fii_ticker
    fii_price["eod_price"] = float(quote)
    fii_price["day"] = now.strftime("%d/%m/%Y")
    return fii_price


def add_price_data_to_table(stock_list):
    for item in stock_list:
        print("Will add {} - {}".format(item,now))
        try:
            price_fii = get_price(item)

            uid_base = str(now.strftime("%2d%m%y")) + '-'
            uid_fii = uid_base + item.lower()

            date = today
            name = price_fii["ticker"].lower()
            price = round(price_fii["eod_price"],2)

            conn = mongo.db.daily_info
        
            item = {
                '_id': uid_fii,
                'date': date,
                'name': name,
                'current_price': price,
            }
            
            conn.replace_one({'_id': uid_fii}, item, upsert=True)

            print("price data for {} added - {}". format(name,now))
        except Exception as e:
            print(e)
            print("There is no info for this fii - {}".format(now))


all_fiis = get_fii_list()
add_price_data_to_table(all_fiis)