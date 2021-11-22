# Survey Bot
This is python bot made with selenium to auto submit responses. The responses can be configured in the `config.yaml` file. This bot in its current stage of development requires all questions to be multiple choice radio boxes.

## Requirements:
1. Chrome web browser: Chrome or a chromium based browser should be used.
2. Selenium driver: Go to this [link](https://chromedriver.chromium.org/downloads) and install the driver for your version of chrome. Check your version [here](chrome://settings/help)
3. Install the required packages:
   1. Create a virtual environment (optional)
   2. Run `pip install -r requirements.txt`

## Configuring the bot:
There are a few variables you can customize in the config
1. `DRIVER_LOCATION`: Path to the selenium driver downloaded in step 2
2. `URL` : Pretty obvious, its the link for the survey
3. `GROUPS`:  No. of questions for the survey
4. `Options`: How many options does each question have sequentially arranged in a list.
5. `Bias_dict`: Must be a python dictionary where the keys are question numbers and values must be a list of probabilities for each option. Note the questions must be arranged in numeric order starting from 1 and ending at the total number of questions. The sum of all the probablities must be equal to 1. The order of the options is decided by the layout of the webpage.
6. `Loops`: The number of responses to submit using the bot