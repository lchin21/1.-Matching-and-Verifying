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
    # call validator
    
if __name__ == "__main__":
    main()