def main():
    n: int = int(input())
    hospital_preferences: list[list[int]] = []
    student_preferences: list[list[int]] = []
    
    for i in range(n):
        preferences: list[int] = input().strip().split(" ")
        hospital_preferences.append(preferences)
        
    for i in range(n):
        preferences: list[int] = input().strip().split(" ")
        student_preferences.append(preferences)
    
    # call matcher
    # call validator
    
main()