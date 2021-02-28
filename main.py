from bs4 import BeautifulSoup as soup
import requests
import re, argparse, sys

index_url = 'https://4anime.to/'
show_suffix = "/anime/"
secondary_url = "https://Gogo"
def page_getter(index_url):
    page = requests.get(index_url)
    #html parsing
    page_soup = soup(page.content,"html.parser")

    if page_soup.find("div", {"class": "right floated sixteen wide mobile ten wide tablet twelve wide computer column"}) is None:
        print("Show not found")
        Start()
    return page_soup

def info_printer(info):
    print(f"Title: \t\t {info['title'].replace('-', ' ').capitalize()}")
    print(f"Episodes: \t {info['num_eps']}")
    print(f"Genres: \t {info['genres']}")
    print(f"Type: \t\t {info['details'][0]}")
    print(f"Studio: \t {info['details'][1]}")
    print(f"Release Date: \t {info['details'][2]}")
    print(f"Status: \t {info['details'][3]}")
    print(f"Language: \t {info['details'][4]}")
    print(f"Description: \t {info['description']}")

def info_getter(show):

    specified = show.lower()
    search_url = index_url + show_suffix + '' + specified + '/'
    info_soup = page_getter(search_url)

    genres_string = ""
    for genres in info_soup.find("div", {"class": "ui tag horizontal list"}).findAll('a'):
        for genre in genres.contents:
            genres_string += f"{genre} "


    details = []
    for detail_div in info_soup.find("div", {"class": ["details", "flat-panel"]}).findAll("div", {"class", "detail"}):
        d = ""
        for detail in detail_div.findAll("a"):
            d += f"{detail.contents[0]} "
        details.append(d)

    eps = info_soup.find("ul", {"class": ["episodes", "range", "active"]}).findAll("a")
    num_of_episodes = eps[len(eps) - 1].contents[0]

    dList = []
    for data in info_soup.find("div", {"class": "ui grid"}).findAll("p"):
            dList.append(f"{data.get_text()}")
    decription_list = dList[2:]
    description_string = ""
    for i in decription_list:
        description_string += i
    info_printer({"title": show, "num_eps": num_of_episodes, "genres": genres_string, "details": details, "description":description_string})
    again = input("Would you like to research another show?")
    if "yes" or "y " == again.lower():
        Start()
    else:
        exit()




def Start():
    info = input("Enter show")

    if info is not None:
        for i in info:
            if i == " ":
                info = info.replace(" ","-")
        info_getter(info)


Start()