import webbrowser

from selenium import webdriver
import urllib3
from db_notes import Note, Session, engine

note_Session = Session(bind=engine)

path = './chromedriver'


def get_data(link):
    global path
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)
    definition = '/html/body/div[3]/div[3]/div[5]/div[1]/p[2]'
    value = ""
    try :
        value = driver.find_element_by_xpath(definition)
    except Exception as e:
        print("Topic too vague")
        webbrowser.open(link)
        exit()
    return value.text
    driver.close()
    return value.text


def scrape_the_web(keyword: str):
    baseurl = 'https://en.wikipedia.org/wiki/'
    keyword = keyword.replace(" ", "_")
    finalurl = baseurl + keyword
    content = ""
    try:
        print(finalurl)
        content = get_data(finalurl)
    except urllib3.exceptions.MaxRetryError as e:
        print(e)
        exit()
    add_to_database(keyword, content)


def add_to_database(title, content):
    new_data = Note(note_title=title, note_content=content)
    note_Session.add(new_data)
    note_Session.commit()


def see_notes(keyword):
    datas = note_Session.query(Note).filter(Note.note_title.contains(keyword)).all()
    for data in datas:
        print(data.note_content, data.note_title)


# see_notes("Barcelona")
# get_data("https://en.wikipedia.org/wiki/Kinetic_energy")
#

# scrape_the_web(str(input("What would you like to get definition about ::")))
