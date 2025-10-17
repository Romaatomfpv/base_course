text_template = "Шляпка гриба, покрытая {} кожиц{}й, держится на {} ножк{}. Снизу шляпка затянута {} плёнкой. Когда её уберёшь, откроется нижняя {} сторона шляпк{}. "

answers = []

print("Задание: Вставьте недостающие слова и буквы в текст.")
print(text_template.format("...", ".", "...", ".", "...", "...", "."))

answer_1 = input("Введите первое пропущенное слово: ")
answers.append(answer_1)

answer_2 = input("Введите первую пропущенную букву: ")
answers.append(answer_2)

answer_3 = input("Введите второе пропущенное слово: ")
answers.append(answer_3)

answer_4 = input("Введите вторую пропущенную букву: ")
answers.append(answer_4)

answer_5 = input("Введите третье пропущенное слово: ")
answers.append(answer_5)

answer_6 = input("Введите четвертое пропущенное слово: ")
answers.append(answer_6)

answer_7 = input("Введите третью пропущенную букву: ")
answers.append(answer_7)

filled_text = text_template.format(*answers)
print("\nВаш заполненный текст:")
print(filled_text)