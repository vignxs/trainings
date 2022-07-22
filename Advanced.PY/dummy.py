# importing the module
import pywhatkit
import os

os.environ['DISPLAY'] = ':0'
# using Exception Handling to avoid
# unprecedented errors
try:

# sending message to receiver
# using pywhatkit
    pywhatkit.sendwhatmsg("+919080450116","Hello from GeeksforGeeks",1, 58)
    print("Successfully Sent!")

except:

# handling exception
# and printing error message
    print("An Unexpected Error!")
