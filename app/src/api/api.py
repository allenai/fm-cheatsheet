from random import randint
from time import sleep
import logging

# Takes a list of strings and filters out any empty strings
def clean_str_list(input):
    # get rid of empty spaces ' ' => ''
    stripped = [s.strip() for s in input]
    # filter out empty elements eg. ''
    return list(filter(None, stripped))

"""
Sample function to show you can
utilize whatever python code you'd like
directly from the Streamlit app
"""
def solve(question, choices=[]):
    if question is None or len(question.strip()) == 0:
        raise ValueError('Please enter a question.')

    cleaned_choices = clean_str_list(choices)
    if len(cleaned_choices) == 0:
        raise ValueError('Please enter at least one choice value.')

    # We use a randomly generated index to choose our answer
    rand_index = randint(0, len(cleaned_choices)-1)
    selected = cleaned_choices[rand_index]

    # We use a randomly generated value between 0 and 100 to make a fake score
    random_value = randint(0, 100)
    # We produce a score with no actual meaning, it's just for demonstration
    # purposes
    score = random_value - 50 if random_value > 50 else random_value - 0

    answer = {
        'answer': selected,
        'score': score
    }
    logging.info(answer)

    # Create simulated latency. You should definitely remove this. It's
    # just so that the API actually behaves like one we'd expect you to
    # build
    sleep(randint(1,3))

    return answer