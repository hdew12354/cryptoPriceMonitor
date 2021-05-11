
import serial
import time

# import coinmarketcap

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

lastInfo = cg.get_price(ids='dogecoin', vs_currencies='gbp')
lastPrice = 0
sleepTime = 10

s = serial.Serial()
s.port = 'COM3'
s.baudrate = 9600
s.open()

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

name, price = parse()

print("name = " + name)
print("price = " + price)

time.sleep(2)
# s.write('Welcome to Doge.'.encode('utf-8'))
while True:
    
    # Getting Price Information
    infoFromAPI = cg.get_price(ids='dogecoin', vs_currencies='gbp')
    
    if(infoFromAPI != lastInfo):
        print(infoFromAPI)
        lastInfo = infoFromAPI

        # Parse Information 

        info = parse()
        name = info[0]
        price = info[1]
        
        # price = coinmarketcap.price('dogecoin')

        price = float(price)

        # Debug Output
        print("name = " + name)
        print("price = " + str(price))

        # Calculate Change in Price
        priceChange = price-lastPrice
        priceChange ="{:.7f}".format(round(priceChange, 6)) #Convert to string, 
        lastPrice = price

        print("priceChange = " + str(float(priceChange)))
    else:
        print("No Change")
    # s.write(str("s").encode('utf-8'))
    s.write(str(price).encode('utf-8'))
    print("s.write(str('price').encode('utf-8'))")
    time.sleep(sleepTime)