from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/view/2304048283/?eBP=JOB_SEARCH_ORGANIC&recommendedFlavor=JOB_SEEKER_QUALIFIED&refId=0af0d738-73d4-44a3-bd1f-bbdfe72353ba&trackingId=bsU8CUy8wJ2ZH%2F5DFpNSpQ%3D%3D&trk=flagship3_search_srp_jobs")

element1= driver.find_element_by_class_name("jobs-unified-top-card__subtitle-primary-grouping mr2 t-black")