
conn=psycopg2.connect(host="webstorage.cokr4mywcowh.us-east-1.rds.amazonaws.com", database="storage_db", user="postgres", password="admin1234")
c=conn.cursor()

    for i in range(1, 11): #For pagination
    website = 'https://www.coingecko.com/?page=' + str(i)
    response = requests.get(website)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find('table', {'class': 'table-scrollable'}).find('tbody').find_all('tr')

    for result in results:

        # name
        try:
            name.append(result.find('span', {
                'class': 'lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
            name1 = result.find('span', {
                'class': 'lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()
        except:
            name.append('n/a')
            name1 = ''

        # price
        try:
            price.append(result.find('td', {'class': 'td-price'}).get_text().strip())
            price1 = result.find('td', {'class': 'td-price'}).get_text().strip()
        except:
            price.append('n/a')
            price = ''

        # change_1h
        try:
            change_1h.append(result.find('td', {'class': 'td-change1h'}).get_text().strip())
            change_1h1 = result.find('td', {'class': 'td-change1h'}).get_text().strip()
        except:
            change_1h.append('n/a')
            change_1h1 = ''

        # change_24h
        try:
            change_24h.append(result.find('td', {'class': 'td-change24h'}).get_text().strip())
            change_24h1 = result.find('td', {'class': 'td-change24h'}).get_text().strip()
        except:
            change_24h.append('n/a')
            change_24h1 = ''

        # change_7d
        try:
            change_7d.append(result.find('td', {'class': 'td-change7d'}).get_text().strip())
            change_7d1 = result.find('td', {'class': 'td-change7d'}).get_text().strip()
        except:
            change_7d.append('n/a')
            change_7d1 = ''

        # volume_24h
        try:
            volume_24h.append(result.find('td', {'class': 'td-liquidity_score'}).get_text().strip())
            volume_24h1 = result.find('td', {'class': 'td-liquidity_score'}).get_text().strip()
        except:
            volume_24h.append('n/a')
            volume_24h1 = ''
        # market_cap
        try:
            market_cap.append(result.find('td', {'class': 'td-market_cap'}).get_text().strip())
            market_cap1 = result.find('td', {'class': 'td-market_cap'}).get_text().strip()
        except:
            market_cap.append('n/a')
            market_cap1 = ''
        script = 'INSERT INTO crypto(coin, price, change1h, change24h, change7d, Volume24h, Marketcap, Day_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (name1, price1, change_1h1, change_24h1, change_7d1, volume_24h1, market_cap1,datetime.now())
        c.execute(script, values)

conn.commit()
