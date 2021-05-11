print("go")
from pycoingecko import CoinGeckoAPI
import time
import serial
cg = CoinGeckoAPI()
lastInfo = cg.get_price(ids='dogecoin', vs_currencies='gbp')
lastPrice = 0
sleepTime = 10

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()
print("Serial Port: " + str(ser))

print("Getting Price for DogeCoin")

def parse():
    # print("after parsing")
    preparse = cg.get_price(ids='dogecoin', vs_currencies='gbp')
    # print(preparse)
    split = str(preparse).split("'")
    # print(split)
    priceA = str(split[4]).split("}")
    # print("a" + str(priceA))
    priceB = str(split[4]).split(": ")
    # print("b" + str(priceB))

    name = split[1]
    priceC = priceB[1]

    size = len(priceC)
    price = priceC[:size - 2]
    

    # print("name = " + name)
    # print("price = " + price)
    return name, price


print(cg.get_price(ids='dogecoin', vs_currencies='gbp'))

info = parse()
name = info[0]
price = info[1]

print("name = " + name)
print("price = " + price)

ser.write(('n' + str(name) + '#').encode('utf-8'))
ser.write(('p' + str(price) + '#').encode('utf-8'))
ser.write(('c' + 'No Change Yet' + '#').encode('utf-8'))

print("gone into loop")
while True:
    infoFromAPI = cg.get_price(ids='dogecoin', vs_currencies='gbp')
    if(infoFromAPI != lastInfo):
        print(infoFromAPI)
        lastInfo = infoFromAPI

        info = parse()
        name = info[0]
        price = info[1]
        price = float(price)

        print("name = " + name)
        print("price = " + str(price))

        priceChange = price-lastPrice
        priceChange ="{:.7f}".format(round(priceChange, 6))
        lastPrice = price

        print("priceChange = " + str(float(priceChange)))
    else:
        print("No Change")
        # time.sleep(sleepTime)
    # Send To Arduino
    ser.write(('n' + str(name) + '#').encode('utf-8'))
    ser.write(('p' + str(price) + '#').encode('utf-8'))
    # ser.write(('c' + str(priceChange) + '#').encode('utf-8'))
    time.sleep(sleepTime)