import sys
from turtle import backward, forward
import keyboard
import tty,termios
def move_forward(self, distance):
        result = self._distance_trans_steps(distance)
        self.thread_l = threading.Thread(target=self._motor_left.Step_CCW, args=(result, SPEED))
        self.thread_l.setDaemon(False)
        self.thread_r = threading.Thread(target=self._motor_right.Step_CW, args=(result, SPEED))
        self.thread_r.setDaemon(False)
        self.thread_l.start()
        self.thread_r.start()

def move_backward(self, distance):
        result = self._distance_trans_steps(distance)
        thread_l = threading.Thread(target=self._motor_left.Step_CW, args=(result, SPEED))
        thread_l.setDaemon(False)
        thread_r = threading.Thread(target=self._motor_right.Step_CCW, args=(result, SPEED))
        thread_r.setDaemon(False)
        thread_r.start()
        thread_l.start()

def turn_left(self, theta):
        result = self._angle_trans_steps(theta)
        thread_l = threading.Thread(target=self._motor_left.Step_CW, args=(result, SPEED))
        thread_l.setDaemon(False)
        thread_r = threading.Thread(target=self._motor_right.Step_CW, args=(result, SPEED))
        thread_r.setDaemon(False)
        thread_l.start()
        thread_r.start()
    
def turn_right(self, theta):
        result = self._angle_trans_steps(theta)
        thread_l = threading.Thread(target=self._motor_left.Step_CCW, args=(result, SPEED))
        thread_l.setDaemon(False)
        thread_r = threading.Thread(target=self._motor_right.Step_CCW, args=(result, SPEED))
        thread_r.setDaemon(False)
        thread_l.start()
        thread_r.start()
def stop(self):
        result = 0
        self.thread_l = threading.Thread(target=self._motor_left.Step_CCW, args=(result, SPEED))
        self.thread_l.setDaemon(False)
        self.thread_r = threading.Thread(target=self._motor_right.Step_CW, args=(result, SPEED))
        self.thread_r.setDaemon(False)
        self.thread_l.start()
        self.thread_r.start()        
if __name__=='__main__':
    while(True):
        fd=sys.stdin.fileno()
        old_settings=termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch=sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN,old_settings)
        if ch=="w":
            move_forward()
            print("w")
        if ch=="s":
            move_backward()
            print("s")
        if ch=="a":
            turn_right()
            print("a")
        if ch=="d":
            turn_left()
            print(d) 
        if ch=="k":
            stop()
            print("stop") 
        if ch=="b":
            print("Shut down!")
            break          
    #GPIO.cleanup()
    sys.exit()        

