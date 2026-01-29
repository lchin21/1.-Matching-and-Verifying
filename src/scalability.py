import time
import random

from match import matcher

def random_pairs(n: int):
    l = list(range(1, n + 1))
    hospital_prefs = []
    student_prefs = []

    for _ in range(n):
        row = l[:]
        random.shuffle(row)
        hospital_prefs.append(row)

    for _ in range(n):
        row = l[:]
        random.shuffle(row)
        student_prefs.append(row)

    return hospital_prefs, student_prefs

def scalability():
