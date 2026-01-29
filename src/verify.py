def verify(hospital_to_student_pairs: list[int], hospital_preferences: list[list[int]], student_preferences: list[list[int]]) -> bool:
    # hospital_to_student_pairs = [p - 1 for p in hospital_to_student_pairs]
    hospital_preferences = [[p - 1 for p in prefs] for prefs in hospital_preferences]
    student_preferences = [[p - 1 for p in prefs] for prefs in student_preferences]

    n: int = len(hospital_preferences)
    
    if n != len(student_preferences):
        print("Number of hospitals and students do not match.")
        return False
    
    if len(hospital_to_student_pairs) != len(set(hospital_to_student_pairs)):
        print("Duplicate students in pairs.")
        return False
    
    student_to_hospital = {student: hospital for hospital, student in enumerate(hospital_to_student_pairs)}
        
    if len(student_to_hospital) != n:
        print("Not all hospitals are matched.")
        return False
    
    for current_hospital, current_student in enumerate(hospital_to_student_pairs):
        student_preference_list = student_preferences[current_student]
        current_hospital_rank = student_preference_list.index(current_hospital)
        
        for hospital_rank, preferred_hospital in enumerate(student_preference_list):
            if hospital_rank < current_hospital_rank:
                hospital_preference_list = hospital_preferences[preferred_hospital]
                current_student_rank = hospital_preference_list.index(hospital_to_student_pairs[preferred_hospital])
                preferred_student_rank = hospital_preference_list.index(current_student)
                
                if preferred_student_rank < current_student_rank:
                    print(f"Unstable pair: Hospital {preferred_hospital + 1} and Student {current_student + 1} prefer each other over their current matches.")
                    return False
                    
    return True