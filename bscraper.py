from bs4 import BeautifulSoup
import requests
import urllib
import lxml


webpage = urllib.request.urlopen('https://www.linkedin.com/jobs/view/2304048283/?eBP=JOB_SEARCH_ORGANIC&recommendedFlavor=JOB_SEEKER_QUALIFIED&refId=0af0d738-73d4-44a3-bd1f-bbdfe72353ba&trackingId=bsU8CUy8wJ2ZH%2F5DFpNSpQ%3D%3D&trk=flagship3_search_srp_jobs')
webContent = webpage.read()

soup = BeautifulSoup(webContent, 'lxml')
css_soup = BeautifulSoup(webContent, 'html.parser')
position_name = str(soup.h1.contents)
company_name = soup.find_all("span", class_="topcard__flavor")

print(position_name[2:-2])
print(company_name)
