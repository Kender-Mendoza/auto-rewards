# run with source .venv/bin/activate
# You need to add permissions
import pyautogui
import time

def open_app(app_name):
    pyautogui.keyDown("command")
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.keyUp("command")
    pyautogui.typewrite(app_name)
    pyautogui.press("enter")

def click_in_ui(positions):
    time.sleep(2)
    pyautogui.moveTo(positions)
    pyautogui.click()

def main():
    # TODO: You can open the app in specifict position and size.
    open_app('safari')

    # Click in rewards icon in safari favorites
    # TODO: you can change to write in url bar. and put the url.
    click_in_ui((2531,400))

    # Click in Status option in reward page.
    click_in_ui((2600,400))

    time.sleep(1)
    pyautogui.scroll(-60)

    # Click in See points breakdown option in reward page.
    click_in_ui((2440,435))

    # Click in PC search
    click_in_ui((2455,575))

    # click in search option
    click_in_ui((1950,190))

    # click in search engine
    click_in_ui((1950,130))

    sentences = [
        "Bing officially replaced Live Search on June 3",
        "Unslashing Tiger new back-end search infrastructure delivering faster and slightly more relevant search results"
    ]

    for val in sentences:
        time.sleep(5)
        pyautogui.typewrite(val)
        pyautogui.keyDown("enter")

        # Clear search engine
        click_in_ui((2435,130))

if __name__ == "__main__":
    main()