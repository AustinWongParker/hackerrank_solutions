if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        python_students = []
        python_students.append([name, score])
        
        for i in range(len(python_students)-1):
            if python_students[i][1] > python_students[i+1][1]:
                temp = python_students[i]
                python_students[i] = python_students[i+1]
                python_students[i+1] = temp
                print(python_students[i][1])
            else:
                pass
                
                
        ## ran out of time -- was stuck on it for 30mins doing 
        ## the logic