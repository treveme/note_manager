username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

headings = []
for i in range(3):
    heading = input(f"Введите заголовок {i + 1}: ")
    headings.append(heading)

note = [
    username,
    title,
    content,
    status,
    created_date,
    issue_date,
    headings 
]


temp_created_date = created_date[0:5]  
temp_issue_date = issue_date[0:5]      


print("\n--- Информация о заметке ---")
print("Имя пользователя:", note[0])
print("Заголовок заметки:", note[1])
print("Описание заметки:", note[2])
print("Статус заметки:", note[3])
print("Дата создания заметки (без года):", temp_created_date)
print("Дата истечения заметки (без года):", temp_issue_date)
print("Заголовки заметки:")
for h in note[6]:  
    print("-", h)
