import requests
from bs4 import BeautifulSoup

def main():
    # Code from this stackoverflow post: https://stackoverflow.com/questions/70931027/http-403-forbidden-is-showing-while-scraping-a-data-from-a-website-using-python
    # Used to counter the "403 Forbidden" message from the server
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}
    HOST = 'https://abandonware-france.org'
    PAGE = "/ltf_abandon/ltf_listes_jeux.php?lettre=tous"
    with requests.Session() as session:
        (r := session.get(HOST, headers=headers)).raise_for_status()
        (r := session.get(f'{HOST}/{PAGE}', headers=headers)).raise_for_status()

    # Parsing HTML
    soup = BeautifulSoup(r.text)

    # Find all links to the game pages 
    links = soup.find_all("a", class_="go_j")
    # Add links to a text file
    with open("game_links.txt", "a+") as f:
        for link in links:
            link_url = link['href']
            f.write(link_url + "\n")

if __name__ == "__main__":
    main()