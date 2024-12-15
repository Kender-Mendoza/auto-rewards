# run with source .venv/bin/activate
# You need to add permissions
import pyautogui
import time

def main():
    # ? Open app using raycast.
    pyautogui.keyDown("command")
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.keyUp("command")
    pyautogui.typewrite('brave')
    pyautogui.press("enter")

    # ? Open new browser tab.
    pyautogui.keyDown("command")
    pyautogui.press("t")
    time.sleep(2)
    pyautogui.keyUp("command")

    # ? Write in broser bar
    pyautogui.typewrite('https://www.bing.com/search?q=hi')
    pyautogui.press("enter")
    time.sleep(2)

    sentences = [
        'primera prueba',
        'segunda prueba'
    ]

    # ? Write in search engine bar
    for val in sentences:
        pyautogui.typewrite(val)
        pyautogui.press("enter")
        time.sleep(2)

if __name__ == "__main__":
    main()