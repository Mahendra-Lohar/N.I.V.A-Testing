# Email drafting:

import speech_recognition as sr
import smtplib

# Email configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'smtp_username': 'your email',
    'smtp_password': 'your password',
}

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None

def send_email(subject, body, to_email):
    # Create an SMTP connection
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("your email","your password")
    # server.sendmail("YOUR_MAIL_ID",to,content)
    # server.close()
    # server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
    # server.starttls()
    # server.login(EMAIL_CONFIG['smtp_username'], EMAIL_CONFIG['smtp_password'])

    # Compose the email
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    # server.sendmail(EMAIL_CONFIG['smtp_username'], to_email, message)
    server.sendmail("your email", to_email, message)
    # Close the connection
    server.quit()

def main():
    print("Hello, I'm Jarvis. How can I assist you with your email?")
    
    print("What is the subject of the email?")
    subject = recognize_speech()

    print("What should be the body of the email?")
    body = recognize_speech()

    print("To whom should I send the email?")
    to_email = "recipient mail"

    send_email(subject, body, to_email)
    print("Email sent successfully.")

if __name__ == "__main__":
    main()





# import smtplib
# # from email.mime.text import MIMEText

# def send_email():
#     # Email configuration
#     sender_email = 'niva.ai002@gmail.com'
#     recipient_email = 'mnlohar18@gmail.com'
#     subject = 'Test Email'
#     body = 'This is a test email sent from Python.'

#     # SMTP server configuration (for Gmail)
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587


#     # Create the email message
#     # message = MIMEText(body)
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
