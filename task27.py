def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\n1: Kontakt qo'shish, 2: Barcha kontaktlar, 3: Qidirish, 0: Chiqish")
        choice = input("Tanlang: ")
        
        if choice == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            phonebook[name] = phone
        elif choice == "2":
            print(phonebook)
        elif choice == "3":
            name = input("Ismni yozing: ")
            print(phonebook.get(name, "Topilmadi"))
        elif choice == "0":
            break
        
my_contacts = {}
phonebook_menu(my_contacts)