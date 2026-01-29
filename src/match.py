"""Gale-shapley"""

#potential optimization with quicker lookup of preference within algorithm? - rank table
def preference(student_prefs, student, new_hospital, current_hospital):
    for h in student_prefs[student]:
        if h == new_hospital:
            return True
        if h == current_hospital:
            return False
    return False

def matcher(n, hospital_prefs, student_prefs):

    hospital_prefer_list = [[x - 1 for x in row] for row in hospital_prefs]
    student_prefer_list = [[x - 1 for x in row] for row in student_prefs]

    hospital_match = [-1] * n
    student_match = [-1] * n
    next_proposal_index = [0] * n

    #free hospitals FIFO
    free_hospitals = [h for h in range(n)]
    next_hos = 0

    proposals = 0

    while next_hos < len(free_hospitals):
        h = free_hospitals[next_hos]
        next_hos += 1

        if next_proposal_index[h] >= n:
            continue

        s = hospital_prefer_list[h][next_proposal_index[h]]
        next_proposal_index[h] += 1
        proposals += 1

        if student_match[s] == -1:
            student_match[s] = h
            hospital_match[h] = s

        else:
            current = student_match[s]
            # if it is preferred over the other hospital
            if preference(student_prefer_list, s, h, current):
                student_match[s] = h
                hospital_match[h] = s
                hospital_match[current] = -1
                free_hospitals.append(current)
            else:
                #rejection
                if next_proposal_index[h] < n:
                    free_hospitals.append(h)

    return hospital_match, proposals