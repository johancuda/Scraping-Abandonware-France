# Abandonware France Scraper

A scraping project of the website [Abandonware France](https://abandonware-france.org/) to retrieve the games with a Swiss flag on their page.

## Results

There exists only one game with this special Swiss flag: [Cashtown](https://abandonware-france.org/ltf_abandon/ltf_jeu.php?id=3860).

You can find the two text files created by the scripts in the `results` folder.

## Requirements

You'll need the following libraries to execute these scripts:
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## Scripts

This repo contains two Python scripts.

- `links_scraper.py` : Used to retrieve a list of all the links to the games' pages. They are then stored in a file named "game_links.txt". This script should be executed first.
- `check_links.py`: Used to verify there are no duplicates in the "game_links.txt" file.
- `flags_scraper.py` : Used to scrape each game's page and then parses the HTML to find the flags present on the page. If the game's page has a Swiss flag, the page's link is then stored in a file named "swiss_games.txt"

## License

Distributed under the MIT License. See LICENSE.txt for more information.

## Credits

Made by Johan Cuda (johan.cuda@unil.ch), student assistant in the [CH Ludens](https://chludens.ch/) Sinergia project.