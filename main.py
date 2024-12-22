# run with source .venv/bin/activate
# You need to add permissions
import pyautogui
import time
from build_sentences import BuildSentences

NAVIGATOR = "brave"

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
    pyautogui.typewrite("https://www.bing.com")
    pyautogui.press("enter")
    time.sleep(2)

    sentences = BuildSentences().call()

    # ? Write in search engine bar
    for val in sentences:
        pyautogui.typewrite(val)
        pyautogui.press("enter")
        time.sleep(5)

if __name__ == "__main__":
    main()