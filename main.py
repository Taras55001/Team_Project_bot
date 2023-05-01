from ab_classes import Name, Phone, Email, Birthday, Record, AddressBook, Address, NotePad
from functools import wraps
import json
from pathlib import Path
from notebook import WITH_NOTES, add_note ,change_note, change_note_stat, show_notes, show_tags, search_note, del_note
import pyttsx3
import re
import sort_folder


PAGE = 10
db_file_name = ""


def input_error(func):
    @wraps(func)
    def wrapper(*args):
        try:
            result = func(*args)
            return result

        except TypeError as err:
            if func.__name__ == "add" or func.__name__ == "change":
                message = "Введіть ім'я та номер телефону будь ласка. мінімальна довжина номеру телефону {} цифр. Максимальна {}. Літери не дозволяються"
                return message.format(Phone.min_len, Phone.max_len)
            if func.__name__ == "add_birthday":
                return "введіть ім'я та день народження"
            if func.__name__ == "add_email":
                return "введіть ім'я та e-mail"
            return err

        except AttributeError:
            return "Введіть ім'я контакту, або такий контакт не існує"

        except ValueError as err:
            return err

        except IndexError as err:
            return err

    return wrapper


@input_error
def greet(*args):
    return "Вітаю, я Ваш персональний бот-помічник MemoMind 1.0.0. Чим можу допомогти?"


@input_error
def add_contact(book: AddressBook, contact: str, phone:Phone, email:Email =None, *address):
    contact_new = Name(contact)
    phone = Phone(phone) if phone else None
    email= Email(email) if email else None
    address= Address(" ".join(address)) if address else None

    rec_new = Record(contact_new, phone, email, address)

    if contact_new.value not in book.keys():
        book.add_record(rec_new)
        return f"Додано контакт '{contact}' з телефоном: {phone}, електронною поштою: {email} та адресою: {address}"
    else:
        rec = book.get(contact)
        if phone:
            rec.add_phone(phone)
        if email:
            rec.add_email(email)
        if address:
            rec.add_adress(address)
        return f"Для існуючого контакту '{contact}' додано номер телефону: {phone}, електронну пошту: {email} та адресу: {address}"
    

@input_error
def add_address(book: AddressBook, contact: str, *adres):
    x = ' '.join(adres)
    address_new = Address(x)
    rec = book.get(contact)
    rec.add_adress(address_new)
    return f'Для існуючого контакту "{contact}" додано адресу: {x}'



@input_error
def add_email(book: AddressBook, contact: str, email: str):
    email_new = Email(email)
    rec = book.get(contact)
    rec.add_email(email_new)
    return f'Для існуючого контакту "{contact}" додано e-mail: {email}'


@input_error
def add_birthday(book: AddressBook, contact: str, birthday: str):
    b_day = Birthday(birthday)
    rec = book.get(contact)
    rec.add_birthday(b_day)
    return f'Для існуючого контакту "{contact}" додано день народження: {b_day}'


@input_error
def congrat(book: AddressBook, days: int):
    if days == "":
        raise ValueError("Введіть число днів")
    output = ""
    for contact in book.values():
        if contact.days_to_birthday() <= int(days):
            output += str(contact)
    text = (
        f"день народження у наступних контактів:\n{output}"
        if output
        else "ні в кого з контактів не має дня народження"
    )
    return f"В період наступних {days} днів {text}"


@input_error
def change(
    book: AddressBook,
    contact: str,
    phone: str = None,
):
    rec = book.get(contact)

    print(rec.show_phones())

    if not rec.phones:
        if not phone:
            phone_new = Phone(
                input("Якщо хочете додати телефон введіть номер:"))
        else:
            phone_new = Phone(phone)
        rec.add_phone(phone_new)
        return f'Змінено номер телефону на {phone_new} для контакту "{contact}"'

    else:
        if len(rec.phones) == 1:
            num = 1
        if len(rec.phones) > 1:
            num = int(input("Який ви хочете змінити (введіть індекс):"))
        if not phone:
            phone_new = Phone(input("Будь ласка введіть новий номер:"))
        else:
            phone_new = Phone(phone)
        old_phone = rec.phones[num - 1]
        rec.edit_phone(phone_new, num)
        return f'Змінено номер телефону {old_phone} на {phone_new} для контакту "{contact}"'


@input_error
def change_email(
    book: AddressBook,
    contact: str,
    email: str = None,
):
    if contact not in book:
        return f'Контакт "{contact}" відсутній в адресній книзі'

    rec = book.get(contact)

    if not email:
        email_new = input("Якщо хочете змінити e-mail введіть нову адресу: ")
    else:
        email_new = email

    rec.change_email(email_new)
    return f'Змінено e-mail контакту "{contact}" на {email_new}'

  
@input_error
def change_birthday(book: AddressBook, contact: str, birthday: str):
    rec = book.get(contact)
    new_birthday = Birthday(birthday)
    rec.change_birthday(new_birthday)
    return f'Змінено дату народження на {new_birthday} для контакту "{contact}"'


@input_error
def change_address(book: AddressBook, contact: str, *address):
    x = " ".join(address)
    address_new = Address(x)
    rec = book.get(contact)

    if not rec.adress:
        if not x:
            address_new = Address(input("Якщо хочете додати адресу, введіть її:"))
        else:
            address_new = Address(x)
        rec.add_address(address_new)
        return f'Додано адресу {address_new} для контакту "{contact}"'
    else:
        if not x:
            address_new = Address(input("Будь ласка, введіть нову адресу:"))
        else:
            address_new = Address(x)
        old_address = rec.adress
        rec.change_address(address_new)
        return f'Змінено адресу {old_address} на {address_new} для контакту "{contact}"'


@ input_error
def del_phone(book: AddressBook, contact: str, phone=None):
    rec = book.get(contact)

    if phone:
        for i, p in enumerate(rec.phones):
            if p == phone:
                num = i + 1
        else:
            raise ValueError("Цей контакт не має такого номеру телефону")
    else:
        print(rec.show_phones())
        if len(rec.phones) == 1:
            num = 1
            ans = None
            while ans != "y":
                ans = input(
                    f"Контакт {rec.name} має тільки 1 телефон {rec.phones[0]}.\
                        Ви впевнені? (Y/N)"
                ).lower()
        else:
            num = int(input("який ви хочете видалити (введіть індекс):"))
    return f"Телефон {rec.del_phone(num)} видалено!"


@ input_error
def del_email(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    rec.email = None
    return f"Контакт {contact}, e-mail видалено"


@ input_error
def del_contact(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    if not rec:
        raise AttributeError
    ans = None
    while ans != "y":
        ans = input(f"Ви впевнені що хочете видалити контакт {contact}? (Y/N)").lower()
    return f"Контакт {book.remove_record(contact)} Видалено!"


@ input_error
def del_birthday(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    rec.birthday = None
    return f"Контакт {contact}, день народження видалений"


@input_error
def del_address(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    rec.adress = None
    return f"Контакт {contact}, адреса видалена"

@ input_error
def phone(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    return f'Контакт "{contact}". {rec.show_phones()}'


@ input_error
def show_all(book: AddressBook, *args):
    if len(book) <= PAGE:
        return book.show_all()
    else:
        gen_obj = book.iterator(PAGE)
        for i in gen_obj:
            print(i)
            print("*" * 50)
            input("Нажміть будь-яку клавішу")
        x = book.lening()
        return f"Всього: {x} контактів."


@ input_error
def search(book: AddressBook, *args):
    pattern = " ".join(args)
    if len(pattern) < 3:
        return "довжина рядка для пошуку >= 3"
    result = book.search(pattern)
    if not result:
        return "не знайдено"
    matches = ""
    for i in result:
        matches += str(i)
    frags = matches.split(pattern)
    highlighted = ""
    for i, fragment in enumerate(frags):
        highlighted += fragment
        if i < len(frags) - 1:
            highlighted += "\033[42m" + pattern + "\033[0m"
    return f"Знайдено {len(result)} збігів:\n" + highlighted


@input_error
def sort_targ_folder(book: AddressBook, *args):
    target_path = " ".join(args)
    return sort_folder.main(target_path)

def voice(content):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # index-> 0 -- Microsoft Irina Desktop - Russian
    # index-> 1 -- Microsoft Zira Desktop - English (United States)
    # index-> 2 -- Microsoft Paulina Desktop - Polish
    # index-> 3 -- Microsoft David Desktop - English (United States)
    engine.say(content)
    engine.runAndWait()
    return content

@input_error
def help(*args):
    with open("README.md", "rb") as help_file:
        output = help_file.read().decode("utf-8")
        return output


@ input_error
def exit(book: AddressBook, notebook: NotePad, *args):
    global is_ended
    is_ended = True
    book.save_to_file(db_file_name)
    notebook.save_to_file(not_file_name,tag_file_name)
    return "До побачення"


@ input_error
def no_command(*args):
    return "Такої команди немає"


COMMANDS = {
    "hello": greet,
    "add email": add_email,
    "add b_day": add_birthday,
    "add address": add_address,
    "add contact": add_contact,
    "add note": add_note,
    "congrat": congrat,
    "change note": change_note,
    "change status": change_note_stat,
    "change address": change_address,
    "change b_day": change_birthday,
    "change email": change_email,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "show notes": show_notes,
    "show tags": show_tags,
    "search note": search_note,
    "search": search,
    "del note": del_note,
    "del address": del_address,
    "del phone": del_phone,
    "del b_day": del_birthday,
    "del email": del_email,
    "del contact": del_contact,
    "sort folder": sort_targ_folder,
    "close": exit,
    "good bye": exit,
    "exit": exit,
    "help": help,
}



@ input_error
def command_parser(line: str):
    line_prep = " ".join(line.split())
    for k, v in COMMANDS.items():
        if line_prep.lower().startswith(k + " ") or line_prep.lower() == k:
            return v, re.sub(k, "", line_prep, flags=re.IGNORECASE).strip().rsplit(" ")
    return no_command, []


is_ended = False


def main():
    book1 = AddressBook()
    notebook=NotePad()
    global db_file_name, not_file_name,tag_file_name
    with open("config.JSON") as cfg:
        cfg_data = json.load(cfg)
        db_file_name = cfg_data["PhoneBookFile"]
        not_file_name=cfg_data["NoteBookFile"]
        tag_file_name=cfg_data["TagBookFile"]

    if Path(db_file_name).exists():
        book1.load_from_file(db_file_name)
        notebook.load_from_file(not_file_name,tag_file_name)
    print("Добрий день!", f"доступні команди: {', '.join(k for k in COMMANDS.keys())}")

    while not is_ended:
        s = input(">>>")
        command, args = command_parser(s)
        if command == exit:
            print(voice(command(book1, notebook),*args))
        else:
            print(voice(command((notebook if command in WITH_NOTES else book1), *args)))

        

if __name__ == "__main__":
    main()
