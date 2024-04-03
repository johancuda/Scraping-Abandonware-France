import requests
from bs4 import BeautifulSoup

def get_page_HTML(page):
    """ Return the content on a game page on Abandonware, used to couter 403 message from the server"""
    
    # Code from this stackoverflow post: https://stackoverflow.com/questions/70931027/http-403-forbidden-is-showing-while-scraping-a-data-from-a-website-using-python
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}
    HOST = 'https://abandonware-france.org'
    PAGE = f"/ltf_abandon/{page}"
    with requests.Session() as session:
        (r := session.get(HOST, headers=headers)).raise_for_status()
        (r := session.get(f'{HOST}/{PAGE}', headers=headers)).raise_for_status()
        return r

def main():

    # Starting scraping
    print("Process started...")
    # Read all game links scraped using links_scraper.py
    with open("game_links.txt", "r") as file:
        links = file.readlines()
        # Initializes count to display in terminal
        count = 1
        nbr_games = len(links)

        for link in links:
            print(f"Game {count}/{nbr_games}")
            # Get HTML
            page_HTML_jeu = get_page_HTML(link)
            # Parsing HTML
            soup = BeautifulSoup(page_HTML_jeu.text)
            # Find flags
            flag = soup.find("img", title="Suisse")

            if flag:
                # If a Swiss flag is present on the page, adds the page's link to the text file
                with open("swiss_games.txt", "a+") as output:
                    output.write(link + "\n")
                print("Swiss game found!")
            count += 1
        print("Process finished.")

if __name__ == "__main__":
    main()