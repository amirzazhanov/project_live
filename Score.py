import os
from Utils import SCORES_FILE_NAME

def add_score(level):
    points = (level * 3 ) + 5

    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as f:
            score = int(f.read().strip())
            f.close()
    else:
            score = 0

    with open(SCORES_FILE_NAME, "w") as f:
        f.write(str(score + points))
        f.close()

def read_score():
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            score = int(file.read().strip())
            file.close()
    else:
        score = 0

    return score