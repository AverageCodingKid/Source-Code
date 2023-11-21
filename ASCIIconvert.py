import time
import pyfiglet
import pyperclip

print("Welcome to PYConverter 🚀\n")

while True:
    userin = input("Enter text to convert to ASCII: ")
    if userin != "end":
        print("Hold on while we generate ASCII ⌛")
        text = pyfiglet.figlet_format(userin)
    if userin.lower() == "end":
        break
        

    time.sleep(1.5)
    print("Generated Text Successfully ✔")
    pyperclip.copy(text)
    print(text)
    print("Powered By Pyfiglet 🐍\n")