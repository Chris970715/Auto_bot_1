# AutoBot_Game-cheater




The code posted above is an implementation of a bot that plays a game involving clicking on a cookie to earn in-game currency and using that currency to buy upgrades from a store. The bot is built using the selenium library for Python, which allows it to interact with the game through a web browser.

![Untitled video - Made with Clipchamp (3)](https://user-images.githubusercontent.com/39882035/227759798-b230365f-f807-4d6e-9b7f-89e2a23ac25b.gif)

The TheGameBot class defines methods for connecting to the game, finding the cookie element, clicking on the cookie, and buying upgrades from the store. The bot uses webdriver.Chrome to launch a Chrome browser and navigate to the game URL.

The click method finds the money and cookie elements on the page and clicks on the cookie.

The buy_options method finds the store elements on the page and checks if the bot has enough money to buy any of the available upgrades. If it does, the bot clicks on the most expensive upgrade it can afford.

The bot runs in an infinite loop until the game ends, clicking on the cookie and buying upgrades as needed.

Overall, the code is a basic implementation of a game-playing bot and could be improved with additional features and error handling.
