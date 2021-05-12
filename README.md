# cryptoPriceMonitor
## Arduino and Python based Cryptocurrency Price Monitor

So, to start, you'll want to upload the file 'lcdTest.ino' to the arduino.
Then, you'll want to run either the fasterAPI.py script or the GettingLCDToPrintFromPython.py script, depending on which api you want to use!


*the FasterAPI.py script uses the [UPDATE ON NEXT COMMIT WHEN THAT'S ACTUALLY A THING] API. This api refreshes the price [AGAIN, INSERT WHEN UPDATED], good for more intense monitoring.
*the GettingLCDToPrintFromPython.py uses the coinGecko API. This api refreshes the price about once every 1-3 minutes, good for desk ornaments.

if you want to change the coin that is being monitored, just open up the chosen python script, then change the name on line 51!
you can also open the lcdTest.ino file and change the name to the correct name for your chosen coin, though this only impacts what is actually shown on the lcd, this can be changed on line 24.

The circuit diagram is in 'image.png' for y'all. i suggest usign a breadboard for the connections otherwise it can get a bit confusing to fix if a wire comes out!
