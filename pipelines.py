import json
import requests
import datetime
import os
import RPi.GPIO as GPIO

from dotenv import load_dotenv
from dateutil.parser import *
from time import sleep

load_dotenv()

PIN_LED_FAILED = 8
GITLAB_API_URL = os.getenv('GITLAB_API_URL')
GITLAB_PROJECT_ID = os.getenv('GITLAB_PROJECT_ID')
GITLAB_PROJECT_NAME = os.getenv('GITLAB_PROJECT_NAME')
GITLAB_PRIVATE_TOKEN = os.getenv('GITLAB_PRIVATE_TOKEN')


# Functions
def printo(message):
    print('[{0}] {1}'.format(str(datetime.datetime.now()), message))


def gitlab_api(path):
    response = requests.get(GITLAB_API_URL + path, headers={'PRIVATE-TOKEN': GITLAB_PRIVATE_TOKEN})

    return json.loads(response.text)


def blink_pipeline(id, status, url, pin_led):
    printo('Pipeline #{0} with status: {1}'.format(str(id), status))
    print(url)
    printo('Blinking led pin: {0}'.format(pin_led))
    for i in range(20):
        GPIO.output(pin_led, (i % 2) == 0)
        sleep(0.5)


# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED_FAILED, GPIO.OUT, initial=GPIO.LOW)

last_failed = datetime.datetime.now()

print('# {0} Pipeline Monitor'.format(GITLAB_PROJECT_NAME))
print('# Started at {0}'.format(str(datetime.datetime.now())))

while True:
    pipelines = gitlab_api('projects/{0}/pipelines?status=failed&per_page=3'.format(GITLAB_PROJECT_ID))
    printo('Total pipelines: {0}'.format(str(len(pipelines))))

    for pipe in pipelines:
        pipeline = gitlab_api('projects/{0}/pipelines/{1}'.format(GITLAB_PROJECT_ID, str(pipe['id'])))
        created_at = parse(pipeline['created_at'], ignoretz=True)

        if created_at > last_failed:
            blink_pipeline(pipe['id'], pipe['status'], pipe['web_url'], PIN_LED_FAILED)
            last_failed = datetime.datetime.now()

    sleep(60)
