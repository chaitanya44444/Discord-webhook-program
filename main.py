import requests
import time






# Prompt for webhook url 
webhook_url = input("Please enter the Discord webhook URL: ")





method1=int(input("Do you want to send msgs like a CHAT Or 1 msg with a number of tiems to send it write 1 for chat and 2 for second metoh"))
if method1==1:
 
  while True:
      # Prompt  for msg
      message = input("Please enter the message to send: ")

     
      data = {"content": message}
      response = requests.post(webhook_url, json=data)

      
      if response.status_code == 204:
          print("Message sent successfully!")
      else:
          print(f"Failed to send message. Status code: {response.status_code}")

if method1==2:  
 
  num_times = int(input("Please enter the number of times to send the message: "))
  message = input("Please enter the message to send: ")
 


  for i in range((num_times)+1):

      time.sleep(3)

      
      data = {"content": message}
      response = requests.post(webhook_url, json=data)

    
      if response.status_code == 204:
          print("Message sent successfully!")
      else:
          print(f"Failed to send message. Status code: {response.status_code}")
      
         

