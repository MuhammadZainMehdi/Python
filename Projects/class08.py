def result():
    for student in students_data:
        total = student["marks"]["Math"] + student["marks"]["English"] + student["marks"]["Science"]
        percent = total * 100 // 300

        if percent >= 90:
            grade = "A+"

        elif percent >= 80 and percent < 90:
            grade = "A"
    
        elif percent >= 70 and percent < 80:
            grade = "B"
    
        elif percent >= 60 and percent < 70:
            grade = "C"
    
        elif percent >= 50 and percent < 60:
            grade = "D"
    
        else:
            grade = "F"

        print("----------Grade Report----------")
        print(f"Students Name: {student["name"]}")
        print("Subject\t\t Marks Obtained")
        print(f"Math\t\t {student["marks"]["Math"]}/100")
        print(f"Math\t\t {student["marks"]["English"]}/100")
        print(f"Math\t\t {student["marks"]["Science"]}/100")
        print(f"Percentage: {percent}%\t\t Grade: {grade}")
        print()

students_data = [
    {
        'name': 'John Doe',
        'marks': {
            'Math': 85,
            'English': 90,
            'Science': 78
        }
    },
    {
        'name': 'Jane Smith',
        'marks': {
            'Math': 75,
            'English': 82,
            'Science': 89
        }   
    },
    {
        'name': 'Emily Davis',
        'marks': {
            'Math': 93,
            'English': 87,
            'Science': 85
        }
    },
    {
        'name': 'Michael Brown',
        'marks': {
            'Math': 65,
            'English': 70,
            'Science': 60
        }
    },
    {
        'name': 'Chris Johnson',
        'marks': {
            'Math': 88,
            'English': 85,
            'Science': 90
        }
    }
]

result()