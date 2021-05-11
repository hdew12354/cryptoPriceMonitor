// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

bool prevConnected = false;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.setCursor(0,0);
  lcd.write("Welcome to Doge");
  lcd.setCursor(0,1);
  lcd.write("Please Connect to PC.");
}

void loop() {
  if (Serial.available()) {
    prevConnected = true;
    lcd.clear();
    delay(100);  //wait some time for the data to fully be read
    lcd.setCursor(0,0);
    lcd.write("Doge Worth/Coin");
    lcd.setCursor(0,1);

    while (Serial.available() > 0) {
      char c = Serial.read();
      lcd.write(c);
    }
  }
}
