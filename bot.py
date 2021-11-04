import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# configs
chromedriver_location = "./resources/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)


###################################  SURVEY CONFIGURATION  ###################################
# survey link
url = 'https://www.surveymonkey.com/r/WJKVKPB'
# no of questions:
groups = 10
# No. of options for each question sequentially:
options = [2, 6, 3, 3, 3, 5, 3, 3, 3, 3]
#############################################################################################

# open the link and Find all radio buttons
driver.get(url)
time.sleep(2)
list_of_all_radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
submit_xpath = '//*[@id = "patas"]/main/article/section/form/div[2]/button'
submit_button = driver.find_element(By.XPATH, submit_xpath)

def grouping(list_of_options: list, groups: int, options: list) -> dict:

    # dictionary of questions and their options
    qna_dict = {i:[] for i in range(1, groups+1)}
    
    for i, option in zip(range(1, groups+1), options):
        for j in range(option):
            element = list_of_options.pop(0)
            qna_dict[i].append(element)
    
    return qna_dict


def fill_survey(dict_of_options: dict, submit_button) -> None:
    for question_no in dict_of_options:
        choice = random.choice(dict_of_options[question_no])
        choice.click()
        time.sleep(1)
    time.sleep(1)
    submit_button.click()



qna_dict = grouping(list_of_all_radio_buttons, groups, options)
fill_survey(qna_dict, submit_button)
