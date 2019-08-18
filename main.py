from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

from datetime import datetime

browser = webdriver.Chrome()

def generateBib(inputStr):
    browser.get(inputStr)

    author = getAuthor(browser)
    title = browser.title
    url = browser.current_url
    year = getYear(browser)

    return author + " " + year + " " + title + " " + url 

def getAuthor(browser):
    element = browser.find_element_by_xpath("//meta[@name='author']")
    return element.get_attribute("content")

def getYear(browser):
    element = browser.find_element_by_xpath("//meta[@property='article:published_time']")
    date = element.get_attribute("content")
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return str(date_obj.year)

def main():
    bib = []
    inputFile = open("input.txt", "r")
    for line in inputFile.readlines():
        bib.append(generateBib(line))
        bib.append('\n')

    browser.close()

    outputFile = open("output.txt", 'w+')

    for i in bib:
        outputFile.write(i)

if __name__ == "__main__":
    main()