import yaml
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By


# loading connfigs
with open("config.yaml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

DRIVER_LOCATION = config["Survey"]["DRIVER_LOCATION"]
URL = config["Survey"]["URL"]
GROUPS = config["Survey"]["GROUPS"]
OPTIONS = config["Survey"]["OPTIONS"]
BAIS_DICT = config["Survey"]["BAIS_DICT"]
LOOPS = config["Survey"]["LOOPS"]

# open the link and Find all radio buttons
driver = webdriver.Chrome(DRIVER_LOCATION)
driver.get(URL)

time.sleep(2)

# fetch radio button objects
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


def biased_choice(dict_of_options: dict, bais_dict: dict) -> list:
    list_of_choices = []
    for question_no, _ in zip(dict_of_options, bais_dict):
        choice = np.random.choice(dict_of_options[question_no], p=bais_dict[question_no])
        list_of_choices.append(choice)
    return list_of_choices


def fill_survey(dict_of_options: dict, list_of_choices: list,  submit_button) -> None:
    for choice in list_of_choices:
        choice.click()
        time.sleep(1)
    time.sleep(1)
    submit_button.click()


def main(loops):
    for i in range(loops):
        qna_dict = grouping(list_of_all_radio_buttons, GROUPS, OPTIONS)
        choice_list = biased_choice(qna_dict, BAIS_DICT)
        fill_survey(qna_dict, choice_list, submit_button)



if __name__ == "__main__":
    main(LOOPS) # NO of times to run the loop
