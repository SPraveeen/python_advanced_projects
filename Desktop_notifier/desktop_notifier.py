from plyer import notification

import time

if __name__== "__main__":
    while True:
        notification.notify(
            title="Hello",
            message="Namagiri il malai tea udan maja",
            app_icon="F:\\Praveen_Repository\\python_advanced_projects\\Desktop_notifier\\try.ico",
            timeout=5
        )
        print("Notification sent!")
        time.sleep(10)
