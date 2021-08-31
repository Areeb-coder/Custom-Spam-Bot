#This is the bot for Telegram
import pyautogui
import time
msg = input("Enter the message: ")
n = input("How many times ? : ")
lap= input("Enter the Time between two messages (secounds):")
print("t minus")
count = 5
while(count != 0):
  print(count)
  time.sleep(1)
  count -= 1
print("Fire in the hole!!!")
for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')
  lapse = float(lap)
  time.sleep(lapse)


