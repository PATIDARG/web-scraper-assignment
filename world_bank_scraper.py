from bs4 import BeautifulSoup
import requests
import csv

# Step 1: Send a GET request to the URL
url = "https://ieg.worldbankgroup.org/data"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')

    rows = table.find_all('tr')

    with open('world_bank_tenders.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            columns = row.find_all('td')
            data = [col.text.strip() for col in columns]
            writer.writerow(data)

    print("Data saved to world_bank_tenders.csv")

else:
    print("Failed to fetch data.")
