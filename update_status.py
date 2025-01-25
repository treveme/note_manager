def collect_note_titles():
    notes = {}  
    while True:
        title = input("Введите заголовок заметки (или 'стоп' для завершения): ")
        if title.lower() == 'стоп' or title == '':
            break
        if title.strip():
            if title not in notes:
                notes[title] = "Не выполнено"
            else:
                print("Этот заголовок уже добавлен. Пожалуйста, введите другой.")
    return notes

def change_note_status(notes):
    while True:
        title = input("Введите заголовок заметки для изменения статуса (или 'стоп' для завершения): ")
        if title.lower() == 'стоп' or title == '':
            break
        if title in notes:
            new_status = input("Введите новый статус (например, 'Выполнено' или 'Не выполнено'): ")
            notes[title] = new_status
        else:
            print("Такой заголовок не найден.")

note_titles = collect_note_titles()
print("\nДобавленные заголовки заметок и их статусы:")
for title, status in note_titles.items():
    print(f"{title}: {status}")

change_note_status(note_titles)

print("\nОбновленные заголовки заметок и их статусы:")
for title, status in note_titles.items():
    print(f"{title}: {status}")