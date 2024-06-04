import requests
from bs4 import BeautifulSoup


def getnewdecrypt():
    base_url1="https://decrypt.co"
    url1 = ['https://decrypt.co/news']
    titles = []
    for url in url1:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        mydiv = soup.find_all('h3', {'class': 'font-normal gg-dark:text-neutral-100 gg-dark:font-poppins font-akzidenz-grotesk text-base leading-4.5 text-black xl:text-xl xl:leading-6 gg-dark:xl:text-2xl gg-dark:xl:leading-8 scene:font-itc-avant-garde-gothic-pro degen-alley-dark:text-neutral-100 bitcoin:inline bitcoin:hover:bg-orange-400'})
        for new in mydiv[:3]:
            a_tag = new.find('a')
            title = a_tag.get_text()
            href = a_tag.get('href')
            titles.append((title, base_url1+href))
        return titles

def getnew():
    base_url2 = "https://www.the-blockchain.com"
    url2 = ['https://www.the-blockchain.com/blockchain-news/']
    titles = []
    for url in url2:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        mydiv = soup.find_all('h3', {'class': 'entry-title td-module-title'})
        for new in mydiv[:3]:
            a_tag = new.find('a')
            title = a_tag.get_text()
            href = a_tag.get('href')
            titles.append((title, href))
        return titles
def getnew3():
    url3 = ['https://www.cryptoninjas.net/']
    titles = []
    for url in url3:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        mydiv = soup.find_all('h3', {'class': 'jeg_post_title'})
        for new in mydiv[:3]:
            a_tag = new.find('a')
            title = a_tag.get_text()
            href = a_tag.get('href')
            titles.append((title, href))
        return titles
# Test function (Optional)
if __name__ == "__main__":
    news = getnew()
    for title, link in news:
        print(f'Title: {title}\nLink: {link}')
if __name__ == "__main__":
    news = getnewdecrypt()
    for title, link in news:
            print(f'Title: {title}\nLink: {link}')
if __name__ == "__main__":
    news = getnew3()
    for title, link in news:
            print(f'Title: {title}\nLink: {link}')
