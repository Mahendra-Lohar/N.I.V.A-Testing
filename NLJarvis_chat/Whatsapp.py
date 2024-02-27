
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
    contacts = {'xyz': '+91857847067', 'Jane Doe': '+9876543210'}
    return contacts.get(contact_name, None)

# Call the function to send the WhatsApp message
send_whatsapp_message()
