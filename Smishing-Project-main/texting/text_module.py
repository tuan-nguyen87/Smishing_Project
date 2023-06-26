import requests
import config
from PIL import Image, ImageTk
import tkinter as tk
#Function to send the an actual text
def smish(phoneNumber, msg):
    
    resp = requests.post('https://textbelt.com/text', {
    'phone': phoneNumber,
    'message': msg,
    'key': config.api_key,
    })
    return(resp.json()["success"])

# phone = 1234
# message = "default"

#inialize root
root = tk.Tk()
root.title("SMShy")
root.geometry('450x200')

#set background image
background_image=tk.PhotoImage(file = 'C:/Users/Johnn/Documents/GitHub/Smishing-Project/texting/matrix.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# the label for user_name
phone_label = tk.Label(root, text = "Phone Number").place(x = 40,y = 60) 

# the label for user_password 
bait_label = tk.Label(root, text = "Bait URL").place(x = 50, y = 100) 

#Entry field for phone number
phone_field = tk.Entry(root,width = 30)
phone_field.place(x = 150, y = 60) 

#Entry field for bait
bait_field = tk.Entry(root, width = 30)
bait_field.place(x = 150,y = 100) 

#handles submit button functionality
#calls smish command which will send out text and displays status message of the text
def submit():
    a = phone_field.get() #gets the text inside the entry objects
    b = bait_field.get()
    global params, text_status #params=entry field text, status=status of message
    params = [a, b]
    text_status = smish(a, b)
    # print(text_status)
    if(text_status):
        success_message = tk.StringVar(root, "Successfully Sent")
    else:
        success_message = tk.StringVar(root, "Failed to Send")
    messageStatus = tk.Message(root, textvariable=success_message, width=400).place(x= 150, y = 130)
    #uncomment if you want the application to close upon sending the text
    # root.destroy()

#smish button
submit_button = tk.Button(root,text = "Smish", command = submit).place(x =100, y = 130)


root.mainloop()

# print(params)


# amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
# print(amnt_of_texts.json())

# request for phone number
# phoneNumber = input("Please input a phone number: ")
#request for message
# msg = input("Please your message: ")

# smish(phoneNumber, msg)