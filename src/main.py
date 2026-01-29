from match import matcher
from verify import verify

def main():
    n: int = int(input())
    hospital_preferences: list[list[int]] = []
    student_preferences: list[list[int]] = []
    
    for i in range(n):
        preferences: list[int] = [int(n) for n in input().strip().split(" ")]
        hospital_preferences.append(preferences)
        
    for i in range(n):
        preferences: list[int] = [int(n) for n in input().strip().split(" ")]
        student_preferences.append(preferences)
    
    # call matcher
    match, _ = matcher(n, hospital_preferences, student_preferences)
    # output match, 0 indexed so +1
    for h in range(n):
        print(h + 1, match[h] + 1)

    print("----------------------------------------")
    # call validator
    valid = verify(match, hospital_preferences, student_preferences)
    if valid: print ("Valid Matching")
    
    
if __name__ == "__main__":
    main()