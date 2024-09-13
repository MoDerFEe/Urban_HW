'''
На вход даны следующие данные:
    Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
    Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
    Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
    Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
а значением - его средний балл.
'''



grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_stu=sorted(students)
ave_grades=[]

for i in grades:
    ave=sum(i)/len(i)
    ave_grades.append(ave)

j=0
book={}

for i in sort_stu:
    book[i] = ave_grades[j]
    j+=1

print(book)