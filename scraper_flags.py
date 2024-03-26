import requests
from bs4 import BeautifulSoup

# fonction qui effectue requête avec header pour contourner erreur 403
def get_page_HTML(page):
    # Code from this stackoverflow post: https://stackoverflow.com/questions/70931027/http-403-forbidden-is-showing-while-scraping-a-data-from-a-website-using-python
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}
    HOST = 'https://abandonware-france.org'
    PAGE = f"/ltf_abandon/{page}"
    with requests.Session() as session:
        (r := session.get(HOST, headers=headers)).raise_for_status()
        (r := session.get(f'{HOST}/{PAGE}', headers=headers)).raise_for_status()
        return r

print("Process started...")    
with open("game_links.txt", "r") as file:
    links = file.readlines()
    count = 1
    nbr_games = len(links)

    for link in links:
        print(f"Game {count}/{nbr_games}")
        page_HTML_jeu = get_page_HTML(link)

        soup = BeautifulSoup(page_HTML_jeu.text)

        flag = soup.find("img", title="Suisse")

        if flag:

            with open("swiss_games.txt", "a+") as output:
                output.write(link + "\n")
            print("Swiss game found!")
        count += 1
    print("Process finished.")