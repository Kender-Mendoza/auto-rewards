# run with source .venv/bin/activate
# You need to add permissions
import pyautogui
import time

# ? Create program for this resolutions and positions.
ORIGINAL_SCREEN_WIDTH = 3440
ORIGINAL_SCREEN_HEIGHT = 1440

def open_app(app_name):
    pyautogui.keyDown("command")
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.keyUp("command")
    pyautogui.typewrite(app_name)
    pyautogui.press("enter")

def click_in_ui(positions):
    original_x, original_y = positions
    screenWidth, screenHeight = pyautogui.size()
    position_x = int(original_x * (screenWidth / ORIGINAL_SCREEN_WIDTH))
    position_y = int(original_y * (screenHeight / ORIGINAL_SCREEN_HEIGHT))

    pyautogui.moveTo((position_x, position_y))
    pyautogui.click()
    time.sleep(2)


def main():
    # open_app('safari')

    # Position windows with Rycast
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("option")
    # pyautogui.press("right")
    # time.sleep(2)
    # pyautogui.keyUp("ctrl")
    # pyautogui.keyUp("option")

    # Search reward page
    # pyautogui.typewrite('google.com')
    # pyautogui.press("enter")

    # # Click in rewards icon in safari favorites
    # # TODO: you can change to write in url bar. and put the url.
    click_in_ui((2531, 400))

    # Click in Status option in reward page.
    click_in_ui((2605,375))

    time.sleep(1)
    pyautogui.scroll(-60)

    # Click in See points breakdown option in reward page.
    click_in_ui((2600, 445))

    # # Click in PC search
    click_in_ui((2455,575))

    # click in search option
    click_in_ui((1950,190))

    # click in search engine
    click_in_ui((1950,130))

    sentences = [
        "The murmuring brook lulled the traveler into a deep slumber.",
        "An emerald mantis perched silently on the windowsill, observing the room.",
        "Beneath the canopy of stars, the desert whispered ancient secrets.",
        "Her laughter rippled like wind through a field of wildflowers.",
        "The mechanical hum of the old clock was oddly comforting.",
        "A stray pebble triggered an avalanche of cascading thoughts.",
        "He carved the wooden figurine with a precision born of decades.",
        "The library's forgotten corner held volumes untouched for centuries.",
        "A single wisp of fog lingered in the valley like a lost dream.",
        "The kaleidoscope shattered, scattering its pieces of light and color.",
        "As the ink dried on the parchment, history was quietly rewritten.",
        "The aroma of fresh pine mingled with the scent of old leather.",
        "Each wave that touched the shore felt like a whispered apology.",
        "The chessboard lay untouched, mid-game, as though frozen in time.",
        "A crimson leaf drifted slowly to the ground, its journey unnoticed.",
        "The wind chimes sang a melody only the mountains could echo.",
        "Shadows danced on the cobblestones under the flickering lamplight.",
        "The forgotten lighthouse stood sentinel over an empty harbor.",
        "A lone violinist played, his music mingling with the autumn breeze.",
        "The forest floor was a mosaic of moss, twigs, and dappled sunlight.",
        "She penned letters to the moon, never expecting a reply.",
        "The sound of a distant train evoked memories of journeys never taken.",
        "The rain painted streaks across the dusty windowpane.",
        "In the silence of the cathedral, her thoughts found a sanctuary.",
        "The abandoned carousel creaked as if longing for laughter.",
        "His voice had the cadence of waves meeting the shore.",
        "The tea cooled as their conversation warmed.",
        "A single candle flickered against the darkness, defiant yet fragile.",
        "The recipe was a secret, passed down like a precious heirloom.",
        "A forgotten melody surfaced, carried by the breeze from the attic.",
        "The butterfly’s wings bore patterns that mimicked ancient maps.",
        "A silver fox darted across the snow, blending into the moonlit landscape.",
        "Her handwriting curled and swirled, resembling vines on a trellis.",
        "The old bookstore smelled of paper, ink, and quiet nostalgia.",
        "The city skyline looked like a jagged heartbeat against the dusk.",
        "He planted a garden of wildflowers that no one but he would see.",
        "The first snowflake landed on her palm, melting into a tiny drop.",
        "An unfinished puzzle lay abandoned on the coffee table.",
        "The old sailor spoke of stars as if they were lifelong companions.",
        "A single raven watched from the barren tree, silent and still.",
        "She danced barefoot on the dewy grass under a lavender sky.",
        "The distant mountains seemed to hum with a song only they could hear.",
        "The clock tower struck thirteen, unsettling the quiet village.",
        "A letter arrived, addressed to a name no one remembered.",
        "The artist’s brush trembled, caught between inspiration and hesitation.",
        "The scent of freshly baked bread filled the small cottage.",
        "The compass pointed true, but his heart pulled him elsewhere.",
        "A thread of sunlight broke through the stormy clouds.",
        "The tree’s gnarled roots told stories of time and resilience.",
        "Her footsteps echoed through the cavern, a lone symphony in the void."
    ]

    acc = 0
    for val in sentences:
        time.sleep(5)
        pyautogui.typewrite(val)
        pyautogui.keyDown("enter")

        # Clear search engine
        click_in_ui((2435,130))
        acc += 2
        print(acc)



    # print("Presiona Ctrl+C para salir.")
    # try:
    #     while True:
    #         # Obtiene la posición actual del mouse
    #         x, y = pyautogui.position()
    #         print(f"Posición: X={x}, Y={y}", end="\r", flush=True)
    #         time.sleep(0.1)  # Actualiza cada 0.1 segundos
    # except KeyboardInterrupt:
    #     print("\nMedición terminada.")


# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)
# pyautogui.hotkey('command', 'space')

if __name__ == "__main__":
    main()