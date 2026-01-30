import time
import random
import matplotlib.pyplot as plt

from match import matcher
from verify import verify

def random_preferences(n: int):
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
    n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    match_times = []
    verify_times = []
    
    for n in n_values:
        hospital_preferences, student_preferences = random_preferences(n)
        
        match_start_time = time.time()
        matched_pairs, proposals = matcher(n, hospital_preferences, student_preferences) # index: hospital, value: student
        match_end_time = time.time()
        match_duration = match_end_time - match_start_time
        
        verify_start_time = time.time()
        valid = verify(matched_pairs, hospital_preferences, student_preferences)
        verify_end_time = time.time()
        verify_duration = verify_end_time - verify_start_time
        
        match_times.append(match_duration)
        verify_times.append(verify_duration)
        
    plt.scatter(n_values, match_times, label='Matching Time', color='blue')
    plt.xlabel("Number of Hospitals/Students")
    plt.ylabel("Running Time (seconds)")
    plt.title("Matching: Number of Hospitals/Students vs. Elapsed Time")
    plt.savefig("matching_time_plot.png")
    plt.clf()
    
    plt.scatter(n_values, verify_times, label='Verification Time', color='orange')
    plt.xlabel("Number of Hospitals/Students")
    plt.ylabel("Running Time (seconds)")
    plt.title("Verification: Number of Hospitals/Students vs. Elapsed Time")
    plt.savefig("verification_time_plot.png")
    
scalability()