#include <RedBot.h>

// 'Start' button
#define BUTTON_PIN 12

// user LED
#define LED_PIN 13

// the left and right wheel encoders
#define L_ENCODER_PIN A2
#define R_ENCODER_PIN 10

// the left, center and right line sensors
#define L_LINE_SENSOR_PIN A3
#define C_LINE_SENSOR_PIN A6
#define R_LINE_SENSOR_PIN A7

// the front Sensor
#define TRIG_PIN A1
#define ECHO_PIN A0

// Motor
#define MAX_SPEED 255           // Fastest speed
#define MIN_SPEED 1             // Slowest speed

// Define the motors, encoders and sensor objects
RedBotMotors motors;
RedBotEncoder encoder = RedBotEncoder(L_ENCODER_PIN, R_ENCODER_PIN);
RedBotSensor left = RedBotSensor(L_LINE_SENSOR_PIN);
RedBotSensor center = RedBotSensor(C_LINE_SENSOR_PIN);
RedBotSensor right = RedBotSensor(R_LINE_SENSOR_PIN);

// variables for testing line sensors
int          prevlValue = 0; // previous left line sensor value
int          prevcValue = 0; // previous center line sensor value
int          prevrValue = 0; // previous right line sensor value

// variables for testing ultra sonic sensor
unsigned long prevValue = 0; // previous ultra sonic reading

void setup() 
{ 
  Serial.begin(19200); //for serial IO to screen
  Serial.println("Welcome to my sensor tester!");

  // make sure the motors are stopped
  stopMotors();

  // now that wheels are stopped, clear the encoder count
  encoder.clearEnc(BOTH);

  pinMode(BUTTON_PIN, INPUT_PULLUP); // setup 'start' button so it is LOW when pressed
  pinMode(LED_PIN, OUTPUT); // setup user LED to be an output

  // setup front sensor's trigger pin adn set to LOW (so it is not on yet)
  pinMode(TRIG_PIN, OUTPUT);
  digitalWrite(TRIG_PIN, LOW);
}

// Function:    waitEncoderLeft
// Description: waits for left wheel encoder to change the desried amount
// Inputs:      counts - number of encoder counts to wait for
// Returns:     none
void waitEncoderLeft(int counts)
{
  long    lCount = 0;     // left motor encoder counts

  while (true)
  {
    // get current value
    lCount = abs(encoder.getTicks(LEFT));

    // print new counter value
    Serial.print("wait left:  ");
    Serial.print(lCount, DEC);
    Serial.print("\twant: ");
    Serial.print(counts, DEC);
    Serial.println("");

    if (lCount >= counts)
    {
        return;
    }
  }
}

// Function:    waitEncoderRight
// Description: waits for right wheel encoder to change the desried amount
// Inputs:      counts - number of encoder counts to wait for
// Returns:     none
void waitEncoderRight(int counts)
{
  long    rCount = 0;     // right motor encoder counts

  while (true)
  {
    // get current value
    rCount = abs(encoder.getTicks(LEFT));

    // print new counter value
    Serial.print("wait right: ");
    Serial.print(rCount, DEC);
    Serial.print("\twant: ");
    Serial.print(counts, DEC);
    Serial.println("");

    if (rCount >= counts)
    {
        return;
    }
  }
}



// Function:    clearEncoders
// Description: clears encoder counts (this stops the motors)
// Inputs:      none
// Returns:     none
void clearEncoders()
{
  stopMotors(); // stop the motors so coutns do not hcange on us
  wait(250);    // give wheels a chance to actually stop

  // clear the encoder counts
  encoder.clearEnc(LEFT);
  encoder.clearEnc(RIGHT);
}

// Function:    pressToStart
// Description: wait for the 'Start' button to be pressed
// Inputs:      none
// Returns:     none
// 
void pressToStart()
{
  unsigned long startTime;
  bool pressed = false;

  Serial.println(""); // print blank line
  Serial.println("Waiting for 'Start' button to be pressed...");

  // keep blinking LED until button is pressed
  while (!pressed)
  {
    // keep LED off for 1 sec, or until button is pressed
    digitalWrite(LED_PIN, LOW);  // turn LED off
    startTime = millis();        // get current time NOTE: the micros() counter will overflow after ~50 days
    while (!pressed && ((millis() - startTime) < 500))
    {
      // see if button is pressed (i.e. LOW)
      if (digitalRead(BUTTON_PIN) == LOW)
      {
        pressed = true;
      }
    }

    // keep LED on for 1 sec, or until button is pressed
    digitalWrite(LED_PIN, HIGH); // turn LED on
    startTime = millis();        // get current time NOTE: the millis() counter will overflow after ~50 days
    while (!pressed && ((millis() - startTime) < 500))
    {
      // see if button is pressed (i.e. LOW)
      if (digitalRead(BUTTON_PIN) == LOW)
      {
        pressed = true;
      }
    }
  }

  // make sure LED is off
  digitalWrite(LED_PIN, LOW);

  // give user a chance to remove their finger
  wait(1000);

  Serial.println(""); // print blank line
}

// Function:    stopMotors
// Description: stops the wheel motors
// Inputs:      none
// Returns:     none
void stopMotors()
{
  motors.brake(); // use .stop() for a coasting stop
  // to control each motor separately
  //motors.leftDrive(0);
  //motors.rightDrive(0);

  Serial.println("stopped");
}



// Function:    fwd
// Description: set motor speed so robot drives forward
// Inputs:      speed - the speed the robot will move, 1=slow, 255=fast
// Returns:     none
void fwd(int speed)
{ 
  // validate the speed value
  if (speed < MIN_SPEED) speed = MIN_SPEED;
  if (speed > MAX_SPEED) speed = MAX_SPEED;
  
  // display the function we are in and its values
  Serial.print("forward:    ");
  Serial.println(speed, DEC);  
  
  // start robot moving forward
  //motors.drive(speed);
  // to control each motor separately
  motors.leftDrive(speed+5);
  motors.rightDrive(speed);
}



// Function:    rev
// Description: set motor speed so robot drives backwards
// Inputs:      speed - the speed the robot will move, 1=slow, 255=fast
// Returns:     none
void rev(int speed)
{
  // validate the speed value
  if (speed < MIN_SPEED) speed = MIN_SPEED;
  if (speed > MAX_SPEED) speed = MAX_SPEED;
  
  // display the function we are in and its values
  Serial.print("backwards:  ");
  Serial.println(speed, DEC);
  
  // start robot moving backward
  motors.drive(-speed);
  // to control each motor separately
  //motors.leftDrive(-speed);
  //motors.rightDrive(-speed);
}



// Function:    turnLeft
// Description: set motor speed so robot turns to the left
// Inputs:      speed - the speed the robot will turn, 1=slow, 255=fast
// Returns:     none
void turnLeft(int speed)
{
  // validate the speed value
  if (speed < MIN_SPEED) speed = MIN_SPEED;
  if (speed > MAX_SPEED) speed = MAX_SPEED;

  // display the function we are in and its values
  Serial.print("turn left:  ");
  Serial.println(speed, DEC);  
  
  // start turning robot to the left
  // to control each motor separately
  motors.pivot(-speed);
  //motors.leftDrive(-speed);
  //motors.rightDrive(speed);
}



// Function:    turnRight
// Description: set motor speed so robot turns to the right
// Inputs:      speed - the speed the robot will turn, 1=slow, 255=fast
// Returns:     none
void turnRight(int speed)
{
  // validate the speed value
  if (speed < MIN_SPEED) speed = MIN_SPEED;
  if (speed > MAX_SPEED) speed = MAX_SPEED;

  // display the function we are in and its values
  Serial.print("turn right: ");
  Serial.println(speed, DEC);
  
  // start turning robot to the right
  motors.pivot(speed);
  // to control each motor separately
  //motors.leftDrive(speed);
  //motors.rightDrive(-speed);
}



// Function:    wait
// Description: wait for the desired length of time, before this function returns
// Inputs:      duration - number of milliseconds before this function returns
// Returns:     none
void wait(int duration)
{ 
  // display the function we are in and its values
  Serial.print("wait:       ");
  Serial.print(duration, DEC);
  Serial.println("ms");

  // wait for the desired time
  delay(duration);
}

// Function:    testUltra
// Description: prints the reading from the ultra sonic sensor, if it has changed
// Inputs:      none
// Returns:     none
void testUltra()
{
  unsigned long ultraValue;

  // read the sensor
  ultraValue = readUltraSonic();

  // see if anything changed
  if (ultraValue != prevValue)
  {
    // remember new value
    prevValue = ultraValue;

    // print new counter values
    Serial.print("ultra:      ");
    Serial.print(ultraValue, DEC);
    Serial.println("");
  }

  delay(100);             // give the sensor a chance to change
}



// Function:    readUltraSonic
// Description: The reads one value from the ultra sonic sensor
// Inputs:      none
// Returns:     the time in microseconds the reading took
unsigned long readUltraSonic()
{
  unsigned long startTime;

  // tell sensor to start reading by holding
  // the trigger pin high for at least 10 us
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // wait for 'sound' to be sent out
  while (digitalRead(ECHO_PIN) == 0);

  // get current time
  // NOTE: the micros() counter will overflow after ~70 min
  startTime = micros();

  // wait for 'sound' to come back
  while (digitalRead(ECHO_PIN) == 1);

  // return how long it took
  return (micros() - startTime);
}


    
// Function:    checkUltraTooClose
// Description: see if we are closer than the given value
// Inputs:      value - ultrasonic microsecond value to check againt
// Returns:     true if close than the given value
unsigned long lastUltraCheck = 0;
bool checkUltraTooClose(unsigned long value) 
{
  unsigned long ultraValue;

  // we want to give the sensor a chance, so we cannot call it too fast.
  // so if it hasn't been 100ms since the last time we used the sensor, then
  // we will wait the remaining time. so if 5ms have gone by, then wait the
  // rest of the 95ms before we check again
  if ((millis() - lastUltraCheck) < 100)
  {
    delay(100 - (millis() - lastUltraCheck));
  }

  // read the sensor
  ultraValue = readUltraSonic();
  lastUltraCheck = millis(); // remember we last finished checking

  // see if we are there
  if (ultraValue < value)
  {
    // print new counter values
    Serial.print("ultraClose: YES ");
    Serial.print(ultraValue, DEC);
    Serial.println("");
    return (true);
  }

  Serial.print("ultraClose: no ");
  Serial.print(ultraValue, DEC);
  Serial.println("");
  return (false);
}


// Function:    testLine
// Description: prints the readings from all line sensors, if any have changed.
//              the sensor labels are upper-case if the value is above LINETHRESHOLD
// Inputs:      threshold - 1 (very light) to 1024 (very dark)
// Returns:     none
int testLine(unsigned long threshold)
{
  int     lLineValue = 0; // left line sensor value
  int     cLineValue = 0; // center line sensor value
  int     rLineValue = 0; // right line sensor value

  // read all the current values
  lLineValue = left.read();
  cLineValue = center.read();
  rLineValue = right.read();

  // see if anything changed
  if ((lLineValue != prevlValue) || (cLineValue != prevcValue) || (rLineValue != prevrValue))
  {
    // remember new counters
    prevlValue = lLineValue;
    prevcValue = cLineValue;
    prevrValue = rLineValue;

    // print new counter values
    Serial.print("line:       ");
    if (lLineValue > threshold)
    {
       Serial.print("LEFT: ");
    }
    else
    {
       Serial.print("left: ");
    }
    Serial.print(lLineValue, DEC);
    if (cLineValue > threshold)
    {
      return false;
    }
    else
    {
      return true;
    }
    
  }

   delay(100);           // give sensors a chance to change
}

void driveToBox(int speed, int stopDist)
{
    while (checkUltraTooClose(stopDist) == false)
  {
    fwd( speed );
  }
}

void turnRight90(int speed,int count)
{
  clearEncoders();
  turnRight(speed);
  waitEncoderLeft(count);
}

void turnLeft90(int speed, int count)
{
  clearEncoders();
  turnLeft(speed);
  waitEncoderRight(count);
}

void lineFollow(int speed,int threshold,int stopDist)
{
  lineFollowToBox(speed, threshold, stopDist);
  checkUltraTooClose(stopDist);
  lineFollowToBox(speed, threshold, stopDist);
}

void lineFollowToBox(int speed,int threshold,int stopDist)
{ int count = 0;
  while ( count < 2)
  {
    while (checkUltraTooClose(stopDist) == false)
    {
      trackLine(speed, threshold);
    }
  count++;
  }
}

void trackLine(int speed,int threshold)
{
  int     lLineValue = 0; // left line sensor value
  int     cLineValue = 0; // center line sensor value
  int     rLineValue = 0; // right line sensor value

  // read all the current values
  lLineValue = left.read();
  cLineValue = center.read();
  rLineValue = right.read();

  // see if anything changed
  if ((lLineValue != prevlValue) || (cLineValue != prevcValue) || (rLineValue != prevrValue))
  {
    // remember new counters
    prevlValue = lLineValue;
    prevcValue = cLineValue;
    prevrValue = rLineValue;

    // print new counter values
    Serial.print("line:       ");
    if (lLineValue > threshold+50)
    {
       clearEncoders();
       turnRight(60);
       waitEncoderRight(20);
       clearEncoders();
       fwd(50);
       waitEncoderRight(20);
       clearEncoders();
    }
   
    if (rLineValue > threshold)
    {
       clearEncoders();
       turnLeft(60);
       waitEncoderLeft(20);
       clearEncoders();
       fwd(50);
       waitEncoderLeft(20);
       clearEncoders();
    }

    if (rLineValue<threshold && cLineValue<threshold && lLineValue<threshold+50)
    {
      clearEncoders();
      fwd(50);
      waitEncoderRight(20);
      clearEncoders();
    }
  }
}

void loop(){ 
  pressToStart();
  driveToBox(100, 620);
  turnRight90(120, 50);
  driveToBox(100, 620);
  turnLeft90(120, 100);
  while( testLine(750) == false)
  {
  driveToBox(100, 620);
  }
  turnLeft90(120, 100);
  lineFollow(50,750, 620);
  turnLeft90(120, 100);
  while (testLine(750) == false)
  {
    fwd(100);
  }
  stopMotors();
  
}

