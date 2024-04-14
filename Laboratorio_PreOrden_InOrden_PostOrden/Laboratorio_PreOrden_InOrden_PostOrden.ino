const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int buttonPin3 = 4;
const int ledPin4 = 5;
const int ledPin5 = 6;
const int ledPin6 = 7;

bool leerPotenciometro = true;

void setup() {
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);
  pinMode(ledPin4, OUTPUT);
  pinMode(ledPin5, OUTPUT);
  pinMode(ledPin6, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (leerPotenciometro) {
    int pot = analogRead(A3);
    Serial.println(pot);
    delay(10);
  }
  int buttonState1 = digitalRead(buttonPin1);
  int buttonState2 = digitalRead(buttonPin2);
  int buttonState3 = digitalRead(buttonPin3);
  
  if (buttonState1 == LOW) {
    Serial.println("InOrden ejecutado");
    digitalWrite(ledPin6, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin6, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin4, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin4, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin5, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin5, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println("InOrden terminado");
    delay(2000);
  }
  if(buttonState2 == LOW){
    Serial.println("PostOrden ejecutado");
    digitalWrite(ledPin4, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin4, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin6, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin6, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin5, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin5, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println("PostOrden terminado");
    delay(2000);
  }
  if(buttonState3 == LOW){
    Serial.println("PreOrden ejecutado");
    digitalWrite(ledPin5, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin5, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin4, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin4, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin6, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin6, LOW);
    Serial.println(0);
    Serial.println("PreOrden terminado");
    delay(2000);
  }

}