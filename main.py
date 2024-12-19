# run with source .venv/bin/activate
# You need to add permissions
import pyautogui
import time
from request_sentences import request_sentences

NAVIGATOR = "brave"
SEARCH_ENGINE_URL = "https://www.bing.com/search?q=hi"

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
    pyautogui.typewrite(SEARCH_ENGINE_URL)
    pyautogui.press("enter")
    time.sleep(2)

    sentences = request_sentences()

    # ? Write in search engine bar
    for val in sentences:
        pyautogui.typewrite(val)
        pyautogui.press("enter")
        time.sleep(5)

if __name__ == "__main__":
    main()