from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from myclass.Mongo import MongoConnect


class Crawler(MongoConnect):

    '''This is a docstring '''

    # Function to retrieve a list of fiis and save it to dynamoDB
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    delta_last_month = now - timedelta(days=30)
    last_month = str(delta_last_month.strftime("%m/%y"))
    current_month = str(now.strftime("%m/%y"))


    def __init__(self):
        print("Debug!")


    def get_fii_list(self):
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


    def __get_price__(self,fii_ticker):
        fii_price = {}
        base_url = 'https://statusinvest.com.br/fundos-imobiliarios/'
        URL = base_url + fii_ticker.lower()
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; \
                 Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        content = requests.get(URL, headers=headers)
        soup = BeautifulSoup(content.text, 'html.parser')
        for quote in soup.find(
                'div', attrs={'title': 'Valor atual do ativo'}).find_all('strong'):
            quote = quote.text
            quote = quote.replace('.', '').replace(',','.')
        fii_price["ticker"] = fii_ticker
        fii_price["eod_price"] = float(quote)
        fii_price["day"] = self.now.strftime("%d/%m/%Y")
        return fii_price



    def add_price_data_to_table(self,stock_list):

        for item in stock_list:
            print(item)
            try:
                price_fii = self.__get_price__(item)

                uid_base = str(self.now.strftime("%2d%m%y")) + '-'
                uid_fii = uid_base + item.lower()

                date = self.today
                name = price_fii["ticker"].lower()
                price = round(price_fii["eod_price"],2)

                conn = MongoConnect.connect(self)
                
                
                if conn.find_one({"_id": uid_fii}):
                    conn.update_one({'_id': uid_fii}, {'$set': {'current_price': price}})
                    print("Price for {} updated!".format(item))
                else:
                    print("Will add {} - {}".format(item,self.now))
                    item = {
                        '_id': uid_fii,
                        'date': date,
                        'name': name,
                        'current_price': price,
                    }
                    
                    conn.replace_one({'_id': uid_fii}, item, upsert=True)

                    print(f"Price data for {name} added - {self.now}")
            except Exception as e:
                print(e)
                print(f"There is no info for this fii - {self.now}")