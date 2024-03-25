def graded_system(file_path):
    with open(file_path,'r') as file:
        total_grade = 0
        student_count=0
        failed_student=[]

        for line in file:
            name,file_grade = line.split(',')
            grade = int(file_grade)

            total_grade += grade
            student_count+=1
            if grade<60:
                failed_student.append(name)
        

    average_grade = total_grade / student_count

    print(f"Average Grade: {average_grade}")
    print("Failed Students:", ", ".join(failed_student))



file_path = 'C:/Users/mohamed/Desktop/data.txt'
graded_system(file_path)