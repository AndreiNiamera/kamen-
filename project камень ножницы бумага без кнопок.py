import random

while True:
    user = input("Выбери - камень, ножницы или бумага:")
    possible = ["камень", "бумага", "ножницы"]
    computer = random.choice (possible)
    print(f"Вы выбрали {user}, компьютер выбрал {computer}.")
    
    if user == computer:
        print(f"Одинаково {user}. Ничья!")
    elif user == 'камень':
        if computer == 'ножницы':
            print("Камень бьет нождницы! Ты победил!")
        else:
            print("Бумага оборачивает камень! Ты выйграл!")
    elif user == 'бумага':
        if computer == 'камень':
            print("Бумага оборачивает камень! Ты выйграл!") 
        else:
            print("Ножницы режут бумагу! Ты проиграл!")
    elif user == 'ножницы':
        if computer == 'бумага':
            print("Ножницы режут бумагу! Ты выйграл!")
        else:
            print("Камень бьет ножницы! Ты выйграл!") 
    
   
    again = input ("Сыграем еще? (д/н): ") 
    if again.lower() != "д":
        break                                    