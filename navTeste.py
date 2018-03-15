from bs4 import BeautifulSoup
import requests
class scrapAnimePage(object):
    @staticmethod
    def epLoader(url):
        players = [];
        page = requests.get(url)
        if page.status_code != 200:
            raise Exception('Não foi possivel entrar no site base de dados \nError HTTP code:'+page.status_code )
        soup = BeautifulSoup(page.content, 'html.parser')
        itens=list(soup.find_all('div',class_='GTTabs_divs'))
        if len(itens) == 0:
             raise Exception("Não existem videos nessa pagina")
        for item in itens:
                video = item.find('video')
                if video != None:
                    if video.has_attr('src'):
                     players.append(video.attrs['src'])
                    elif video.find('source'):
                     players.append(video.find('source').attrs['src']);
                    else:
                     raise Exception("Não existem palyers nessa pagina")
        return players;




    @staticmethod
    def listLoader(url):
        episodes = [];
        page = requests.get(url)
        if page.status_code != 200:
            raise Exception('Não foi possivel entrar no site base de dados \nError HTTP code:'+page.status_code )
        soup = BeautifulSoup(page.content, 'html.parser')
        itens = soup.find_all('ul',class_='lcp_catlist')
        if len(list(itens)) == 0:
            raise Exception("Não existem episodios nessa pagina")
        itens = itens[0].children
        for item in itens:
            episodes.append((item.find('a').text, item.find('a').attrs['href']))
        return episodes

    @staticmethod
    def animeSearch(str):
        page = requests.get('http://www.animalog.biz/animes-legendados/')
        animesWith = None
        if page.status_code != 200:
            raise Exception('Não foi possivel entrar no site base de dados \nError HTTP code:'+page.status_code )
        soup = BeautifulSoup(page.content, 'html.parser')
        animesWith = soup.find('a',class_='list-group-item',text=str)
        if animesWith == None:
            raise Exception('Não existem animes com esse nome certifique-se de letras maiuscula/minusculas e sinais')
        return(animesWith.attrs['href'])

try:
    print(scrapAnimePage.animeSearch("Borutz"))
except Exception as e:
    print(e)
