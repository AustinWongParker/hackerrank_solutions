if _name_ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    
    second_lowest = sorted(list(set([x[1] for x in students])))[1]
    for name in sorted([x[0] for x in students if x[1] == second_lowest]):
        print(name)