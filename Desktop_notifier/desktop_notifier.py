from plyer import notification

import time

if __name__== "__main__":
    while True:
        notification.notify(
            title="Hello",
            message="This is a test notification",
            app_icon="F:/Praveen_Repository/python_advanced_projects/Desktop_notifier/try.ico",
            timeout=5
        )
    time.sleep(10)
