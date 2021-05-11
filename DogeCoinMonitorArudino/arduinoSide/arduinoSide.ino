#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
const int potValPin = 9;
String coinName = "NoNameYet";
String newName;
String lastRead = "not the same!!!!";
String price = "0.00000000000000";
String priceChange = "0.00000000000000";
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  // lcd.print("Welcome To Doge!");
  // delay(1000);
}

void loop() {
  String incoming = Serial.readStringUntil('#');
  if(incoming != lastRead){
    // lcd.print(incoming);
    if (incoming.charAt(0) == 'n'){
      incoming.remove(0);
      newName = incoming;
      if(newName != coinName){
        coinName = newName;
        lcd.clear();
        lcd.setCursor(0,1);
        lcd.print(coinName);
      }
    }
    // }else if (incoming.charAt(0) == 'p'){
    //   incoming.remove(0);
    //   price = incoming; 
    // }else if (incoming.charAt(0) == 'c'){
    //   incoming.remove(0);
    //   priceChange = incoming; 
    // }
  
    // lcd.setCursor(0, 0);
    // lcd.print(coinName + " GPB/Coin");
  
    // lcd.setCursor(0, 1);
    // lcd.print(price);
    delay(100);
  }
  lastRead = incoming;
}
