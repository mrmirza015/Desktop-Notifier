from plyer import notification
import time
import random

if __name__=="__main__":

        quotes = {
        1: "Stay hydrated and conquer the day!",
        2: "Water is the fuel for your body; keep it topped up.",
        3: "Don't forget to drink water and get sunshine. It's the fountain of youth.",
        4: "Water: Your natural energy booster.",
        5: "Every sip of water you take is supporting your health.",
        6: "Stay thirsty for success and hydrated for life.",
        7: "Water is the key to unlocking your full potential.",
        8: "H2O: The elixir of life and wellness.",
        9: "Drink water, stay focused, and never give up!",
        10: "Sip by sip, you're getting closer to your goals. Keep drinking!"
    }
    
        while True:
            random_number = random.randint(1, 10)
            random_quote = quotes[random_number]
            notification.notify(title="Drink Some Water", message=random_quote,app_icon="D:/Python/ForGit/Desktop Notifier/favicon.ico", timeout=5)
            time.sleep(10)
