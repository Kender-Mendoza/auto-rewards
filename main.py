# run with source .venv/bin/activate
# You need to add permissions
import pyautogui
import time
from build_sentences import BuildSentences
from datetime import date

NAVIGATOR = "safari"

def main():
    # ? Open app using raycast.
    pyautogui.keyDown("command")
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.keyUp("command")
    pyautogui.typewrite(NAVIGATOR)
    pyautogui.press("enter")

    # ? Open new browser tab.
    pyautogui.keyDown("command")
    pyautogui.press("t")
    time.sleep(2)
    pyautogui.keyUp("command")

    # ? Write in broser bar
    pyautogui.typewrite("https://www.bing.com/")
    pyautogui.press("enter")
    time.sleep(2)

    sentences = BuildSentences().call()

    # ? Write in search engine bark
    for val in sentences:
        pyautogui.typewrite(val)
        pyautogui.press("enter")
        time.sleep(5)

if __name__ == "__main__":
    main()


#
# Get info about conjunto diario and reward profil.
#

# ? Open new browser tab.
# pyautogui.keyDown("command")
# pyautogui.press("t")
# time.sleep(2)
# pyautogui.keyUp("command")

# ? Open Microsoft rewards page.
# pyautogui.typewrite("https://rewards.bing.com")
# pyautogui.press("enter")
# time.sleep(2)

# ? Download html page.
# pyautogui.keyDown("command")
# pyautogui.press("s")
# time.sleep(2)
# pyautogui.keyUp("command")

# ? write file name.
# file_name = "microsoft_rewards_" + date.today().strftime("%Y_%m_%d")
# pyautogui.typewrite(file_name)
# pyautogui.press("enter")
# time.sleep(20) # ? download file time.
