import os
from gtts import gTTS
import webbrowser
import schedule
import time
import requests
from bs4 import BeautifulSoup

# Global variables

views = None
print("Source Code: \n")

def update_view_count():
    try:
        
        global title, views

        link = input("Enter video link:")

        time.sleep(3)
        print("Updating view count...")

        # Get the HTML content of the YouTube Shorts page
        response = requests.get(link)
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the title tag
        title_tag = soup.find('meta', attrs={'property': 'og:title'})

        # Extract the title text
        title = title_tag['content']

        # Find the views tag
        views_tag = soup.find('meta', attrs={'itemprop': 'interactionCount'})

        # Extract the views count
        views = int(views_tag['content'])

        
        time.sleep(1)
        # Print the extracted views count
        print("Current view count:", views)
    
    except ValueError:
        print("Enter a valid url")

# Schedule the update_view_count function to run every 30 seconds
schedule.every(30).seconds.do(update_view_count)

while True:
    data = input("<<< ")

    # Check if input is empty
    if not data:
        continue


    elif data == "dtation":
        print("Collecting Search...")
        time.sleep(3)
        webbrowser.open("python.org")
        continue

    # Handle clear command
    elif data == "clear":
        os.system('cls')  # or clear() for Linux/macOS
        continue

    elif data == "delete":
        try:
            file = input("Enter file to delete: ")
            confirm = input("Are you sure you want to delete the application? (yes/no): ")
            if confirm.lower() == "yes":
                os.remove(file)
                print("Application deleted.")

            else:
                print("Deletion canceled.")

        except FileNotFoundError:
            print("File not found")


    # Handle speech-to-text or text-to-speech commands
    elif data == "speechtext" or data == "texttospeech" or data == "gtts":
        try:
            language = 'en'
            text = input("Enter text:")
            audio = tts = gTTS(text=text, lang=language)

            # Save the speech as an MP3 file
            audio.save('ai_audio.mp3')
            print("File saved as mp3")
        except AssertionError:
            print("Error: perhaps you did not input any text, try again soon.")
            continue

    elif data == "yview":
        update_view_count()
        
        continue

    # Handle exit command
    elif data == "end":
        break

    elif "search" in data:
        web = input("Enter website: ")
        webbrowser.open(web)
        continue

    elif data == "update":
        print("Updating 10%")
        time.sleep(1)
        print("Updating 30%")
        time.sleep(1)
        print("Updating 50%")
        time.sleep(1)
        print("Updating 100%")
        time.sleep(3)
        print("Restart Initiated")
        os.system("shutdown -r -t 0")
        

    else:
        print("Command Not Found, if you would like to exit, type:end")

# Run the scheduler
schedule.run_pending()