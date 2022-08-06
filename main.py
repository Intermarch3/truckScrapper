####################################
#                                  #
#   software: truckScrapper        #
#   author: Intermarch3            #
#   date of start: 05/08/2022      #
#                                  #
####################################

#####- import space -#####
import bs4
import urllib.request
from pathlib import Path

#####- global var -#####
SITE_URL = ["https://fierdetreroutier.fr/piwigo/index.php?/category/150"]

#####- function space -#####
def main():
    # main function
    # param: none
    # return: none
    nb_page = 1
    nb_img = 0
    page = int(input("How many page do you want to download (1 page = 250 images) ? \n>>> "))
    pageCounter(page)
    print("Scrap the website ...")
    for url in SITE_URL:
        links = scrapper(url)
        print("Download ans save images in page " + str(nb_page) + " ...")
        nb_page += 1
        for link in links:
            nb_img += 1
            downloadImg(link)
    print("You have downloaded " + str(nb_img) + " images of trucks !!!")
    print("Enjoy your trucks :)")


def pageCounter(nb):
    # give pages urls
    # param: nb: number of page wanted (int)
    # return: none
    nb -= 1
    i = 0
    if nb != 0:
        while i != nb:
            i += 1
            SITE_URL.append(SITE_URL[0] + "/start-" + str(250 * i))


def scrapper(url):
    # get images urls
    # param: url: url of the website (str)
    # return: none
    with urllib.request.urlopen(url) as r:
        soup = bs4.BeautifulSoup(r, 'html.parser')
    liste = soup.find("ul", "thumbnails")
    links = []
    for img in liste.find_all("img", "thumbnail", src=True):
        link = img['src']
        link = link.lstrip("_data/i")
        link = link.replace("-th", "")
        links.append("https://fierdetreroutier.fr/piwigo/" + link)
    return links


def downloadImg(url):
    # download image
    # param: url: url of the images (str)
    # return: none
    filename = url.split('/')[-1]
    path = str(Path().absolute()) + "\image\\" + filename
    urllib.request.urlretrieve(url, path)


if __name__ == '__main__':
    main()