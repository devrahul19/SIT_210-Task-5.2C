import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(14,GPIO.LOW)
GPIO.setup(15,GPIO.LOW)
GPIO.setup(18,GPIO.LOW)

win =tk.Tk()
win.title("GUI RAHUL-2210994825")
win.geometry('400x400')

def red():
    if GPIO.input(14):
        GPIO.output(14, GPIO.LOW)
        red_button.config(text="Red: OFF")
    else:
        GPIO.output(14, GPIO.HIGH)
        red_button.config(text="Red: ON")
        
def green():
    if GPIO.input(15):
        GPIO.output(15, GPIO.LOW)
        green_button.config(text="Green: OFF")
    else:
        GPIO.output(15, GPIO.HIGH)
        green_button.config(text="Green: ON")
        
def blue():
    if GPIO.input(18):
        GPIO.output(18, GPIO.LOW)
        blue_button.config(text="Blue: OFF")
    else:
        GPIO.output(18, GPIO.HIGH)
        blue_button.config(text="Blue: ON")
   
red_button = tk.Radiobutton(win, text="Red: OFF", command=red)
red_button.pack(pady=10)
green_button = tk.Radiobutton(win, text="Green: OFF", command=green)
green_button.pack(pady=10)
blue_button = tk.Radiobutton(win, text="Blue: OFF", command=blue)
blue_button.pack(pady=10)

def exit_program():
    GPIO.cleanup()
    win.quit()


exit_button = tk.Button(win, text="Exit", command=exit_program)
exit_button.pack(pady=10)


win.mainloop()
