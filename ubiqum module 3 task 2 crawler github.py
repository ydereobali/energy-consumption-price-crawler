##########################################################################
# Title:  ubiqum module 3 task 2 crawler github
# Author: Yigit Dereobali
# Description: Crawl day ahead hourly power prices from EPEX power exchange
# and save them in an CSV file.
# Date: 21.06.2019
# Version: 1.0
##########################################################################
print("*****************************")

# libraries
import requests
from bs4 import BeautifulSoup
import csv
import datetime


# read source html
r = requests.get("https://www.epexspot.com/de/marktdaten/dayaheadauktion")
doc = BeautifulSoup(r.text, "html.parser")


# year
now = datetime.datetime.now()
year = now.year


# get date and add year
for th in doc.select("#tab_de_lu .list.hours.responsive tbody"):
    th = th.select("th")[-1].text
    th = th[4:]
    th = th.replace(".", "-")
    th = th + str(year)

print("Hourly power prices for {} ".format(th))


# get hourly power prices and add to the list
hourly_prices = [th]

for td in doc.select("#tab_de_lu .list.hours.responsive .no-border"):
    td = td.select("td")[8].text
    td = td.replace(",", ".")
    hourly_prices.append(td)

print(hourly_prices)


# save the hourly power price list as csv
with open('current_hourly_power_prices.csv', 'w', newline='') as csvfile:
    pricewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for price in hourly_prices:
        pricewriter.writerow([price])


print("*****************************")

