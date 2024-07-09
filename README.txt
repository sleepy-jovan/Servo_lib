This is a servo lib for micro python on raspberry pi pico, pico w. This "framework" is used for 
converting degrees in to milliseconds, You can find the class Servo in the servo.py folder.
It works whit a specific formula:

int(((((deg/90)+0.5)/20) * 65535))

This is the formula for converthing degrees in to miliseconds and then to a specific number between 1638 and 8191, these numbers then are put in to a line of code, more specifically in the file example.py in line 8.

servo.duty_u16(sv.Deg(180,0))

Hire were calling calling the method Deg in the class Servo. The first argument that is given is the degrees that then are converted using the formula in the servo.py file.
The seccond argument is not importent you can set it to any number you want.

If you are curious on how the forumal works, well it works by fist defining the deg variable and then devide it by 90. Now we divide it by 90 because we need to convert the degreec in to miliseconds for example if we divide 180 whit 90 we get 2 and as the formula goes we add + 0.5 because to comand the servo to go to 0 degreec we need to give it 0.5 milisecond but for it to go to 180 degreec we need to give it 2.5 milisecond. So in the first step of the formula wich is to divide 180 (or and given number betwine 0 and 180) by 90 because that gives the formula by how many miliseconds to move from 0.5 to 2.5. Then we divide it by 20 to get a % and we the 
multiply it by 16 bits (that is how many bits micropython has to proces the value) and we get a number betwine 1638 and 8191. If you so happen to have any quetions about how this works feal free to ask me over at twiter @Skeepy_Jovan. 