# # Email drafting:

# import speech_recognition as sr
# import smtplib

# # Email configuration
# EMAIL_CONFIG = {
#     'smtp_server': 'smtp.gmail.com',
#     'smtp_port': 587,
#     'smtp_username': 'niva.ai002@gmail.com',
#     'smtp_password': 'JarviS#1999',
# }

# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio)
#         print("You said:", command)
#         return command
#     except sr.UnknownValueError:
#         print("Sorry, could not understand the audio.")
#         return None

# def send_email(subject, body, to_email):
#     # Create an SMTP connection
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login("niva.ai002@gmail.com","JarviS#1999")
#     # server.sendmail("YOUR_MAIL_ID",to,content)
#     # server.close()
#     # server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
#     # server.starttls()
#     # server.login(EMAIL_CONFIG['smtp_username'], EMAIL_CONFIG['smtp_password'])

#     # Compose the email
#     message = f"Subject: {subject}\n\n{body}"

#     # Send the email
#     # server.sendmail(EMAIL_CONFIG['smtp_username'], to_email, message)
#     server.sendmail("niva.ai002@gmail.com", to_email, message)
#     # Close the connection
#     server.quit()

# def main():
#     print("Hello, I'm Jarvis. How can I assist you with your email?")
    
#     print("What is the subject of the email?")
#     subject = recognize_speech()

#     print("What should be the body of the email?")
#     body = recognize_speech()

#     print("To whom should I send the email?")
#     to_email = "mnlohar18@gmail.com"

#     send_email(subject, body, to_email)
#     print("Email sent successfully.")

# if __name__ == "__main__":
#     main()


# #niva.ai002@gmail.com
# #JarviS#1999


# import smtplib
# from email.mime.text import MIMEText

# def send_email():
#     # Email configuration
#     sender_email = 'niva.ai002@gmail.com'
#     recipient_email = 'mnlohar18@gmail.com'
#     subject = 'Test Email'
#     body = 'This is a test email sent from Python.'

#     # SMTP server configuration (for Gmail)
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#     smtp_username = 'niva.ai002@gmail.com'
#     smtp_password = 'JarviS#1999'

#     # Create the email message
#     message = MIMEText(body)
#     message['Subject'] = subject
#     message['From'] = sender_email
#     message['To'] = recipient_email

#     try:
#         # Establish a connection to the SMTP server
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()

#         # Login to the SMTP server
#         server.login(smtp_username, smtp_password)

#         # Send the email
#         server.sendmail(sender_email, recipient_email, message.as_string())

#         print("Email sent successfully!")

#     except Exception as e:
#         print(f"Error sending email: {e}")

#     finally:
#         # Close the connection to the SMTP server
#         server.quit()

# # Call the function to send the email
# send_email()


# import pywhatkit as kt
# import datetime

# def send_whatsapp_message(recipient_number, message_content, hours, minutes):
#     try:
#         # Send the WhatsApp message
#         kt.sendwhatmsg(recipient_number, message_content, hours, minutes)

#         print(f"WhatsApp message scheduled to be sent at {hours}:{minutes}")
#     except Exception as e:
#         print(f"Error: {e}")

# # Replace these values with your recipient's number and the message content
# recipient_number = '+919325066278'  # Replace with the recipient's WhatsApp number
# message_content = "Hello, this is Jarvis. How can I assist you today?"

# # Set the time to send the message (adjust as needed)
# now = datetime.datetime.now()
# hours = now.hour
# minutes = now.minute + 2  # Send the message 1 minute from now

# # Call the function to send the WhatsApp message
# send_whatsapp_message(recipient_number, message_content, hours, minutes)

import pywhatkit as kt
import datetime

def send_whatsapp_message():
    try:
        # Ask the user for the recipient's name or number
        choice = input("Enter '1' to send by name or '2' to send by number: ")

        if choice == '1':
            # Send by name
            recipient_name = input("Enter the recipient's name: ")  # Replace with actual contact name
            recipient_number = get_contact_number(recipient_name)
        elif choice == '2':
            # Send by number
            recipient_number = input("Enter the recipient's WhatsApp number: ")
        else:
            print("Invalid choice. Please enter '1' or '2'.")
            return

        # Get the message content
        message_content = input("Enter the message: ")

        # Set the time to send the message (adjust as needed)
        now = datetime.datetime.now()
        hours = now.hour
        minutes = now.minute + 2 # Send the message 1 minute from now

        # Send the WhatsApp message
        kt.sendwhatmsg(recipient_number, message_content, hours, minutes)

        print(f"WhatsApp message scheduled to be sent at {hours}:{minutes}")
    except Exception as e:
        print(f"Error: {e}")

def get_contact_number(contact_name):
    # Replace this function with your logic to retrieve the contact number by name
    # You may use a contacts API or a local contacts database
    # For simplicity, let's assume a static mapping in this example
    contacts = {'mahendra': '+918623047067', 'Jane Doe': '+9876543210'}
    return contacts.get(contact_name, None)

# Call the function to send the WhatsApp message
send_whatsapp_message()
