# AutoBot_Game-cheater




The code posted above is an implementation of a bot that plays a game involving clicking on a cookie to earn in-game currency and using that currency to buy upgrades from a store. The bot is built using the selenium library for Python, which allows it to interact with the game through a web browser.


![Untitled video - Made with Clipchamp (4)](https://user-images.githubusercontent.com/39882035/227760109-f8448789-8fcb-472f-a9bd-b06d47fc1d96.gif)


![auto_3](https://user-images.githubusercontent.com/39882035/227760081-93f4e0e6-1c28-44c0-9ae4-0dfa40d24f0d.gif)


The TheGameBot class defines methods for connecting to the game, finding the cookie element, clicking on the cookie, and buying upgrades from the store. The bot uses webdriver.Chrome to launch a Chrome browser and navigate to the game URL.

The click method finds the money and cookie elements on the page and clicks on the cookie.

The buy_options method finds the store elements on the page and checks if the bot has enough money to buy any of the available upgrades. If it does, the bot clicks on the most expensive upgrade it can afford.

The bot runs in an infinite loop until the game ends, clicking on the cookie and buying upgrades as needed.


