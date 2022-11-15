int data;

void setup() {
    Serial.begin(9600);
    pinMode(13, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    digitalWrite(13, LOW);
}

void loop() {  
  while (Serial.available()){
    data = Serial.read();
  }

  if (data == '1'){
    digitalWrite(13, HIGH);
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
  }
  
  else if (data == '2'){
    digitalWrite(13, LOW);
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
  }
  
  else if (data == '3'){
    digitalWrite(13, LOW);
    digitalWrite(8, LOW);
    digitalWrite(9, HIGH);
  }
}
