import requests
import time






# Prompt the user to input the webhook URL and message to send
webhook_url = input("Please enter the Discord webhook URL: ")





method1=int(input("Do you want to send msgs like a CHAT Or 1 msg with a number of tiems to send it write 1 for chat and 2 for second metoh"))
if method==1:
    # Define an infinite loop to continuously prompt the user for input and send messages
  while True:
      # Prompt the user to input a message to send
      message = input("Please enter the message to send: ")

      # Send the message to the channel using the webhook
      data = {"content": message}
      response = requests.post(webhook_url, json=data)

      # Display a success or failure message depending on the response status code
      if response.status_code == 204:
          print("Message sent successfully!")
      else:
          print(f"Failed to send message. Status code: {response.status_code}")'''

if method1==2:  
  # Prompt the user to input the number of times to send the message
  num_times = int(input("Please enter the number of times to send the message: "))
  message = input("Please enter the message to send: ")
  # Loop through the messages and send them using the webhook
  for i in range (2):

    for i in range(num_times):
        data = {"content": message}
        time.sleep(3)
        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print(f"Message {i+1} sent successfully!")
        else:
            print(f"Failed to send message {i+1}. Status code: {response.status_code}")
      
         

