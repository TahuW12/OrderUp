from twilio.rest import Client
from twilio_credentials import twilio_account, twilio_token, twilio_number
from datetime import datetime




#Program Code
while True:
    
    #get phone number
    user_input = input("Enter Phone Number: ")

    #check if number is formatted correct, if not format it
    if(user_input[0] == "0"):
        user_input = user_input[1:]
    
    #add area code (+61)
    cellphone = ("+61" + user_input)
    
    #Twilio credential definitions
    account= twilio_account
    token = twilio_token
    client = Client(account, token)

    #grab quote from text file:
    with open("Quote.txt", "r") as quote_file:
        quote = quote_file.read()
        quote_file.close()
    
    
    #Send request to twilio
    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote)
                           
                           
    
    #Get current date and time
    currtime = datetime.now()
    dt_string = currtime.strftime("%d/%m/%Y %H:%M:%S")
       
    #log info of text to txt file
    log = str(cellphone + " " + dt_string)
    with open("Log.txt", "a") as text_file:
        text_file.write("Text Sent to " + log + "\n")
        text_file.close()
    
    #return to user that text has been sent
    print("Text has been sent to " + log)
