def main():
    list_students()
    grade_student()


def list_students():
    print('Students: ', end = '')
    for student in students:
        print(student, end = ', ')


def grade_student():
    input_student = input('\nSelect a student from this list: ')
    while True:
        if input_student in students:
            print(f'\nGrade {input_student} - {students[input_student]}')
            main()
        else:
            print('\nDidnt find this student ')
            main()


students = {
    'Maxim': 'A',
    'Denchik': 'A',
    'Vlados': 'C',
    'Semen': 'F',
    'Kirill': 'B'
}

if __name__ == '__main__':
    main()