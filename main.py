from ab_classes import Name, Phone, Email, Birthday, Record, AddressBook, Adres, Note, NotePad, HashTag
from functools import wraps
from pathlib import Path
import re


PAGE = 10
DB_FILE_NAME = "phonebook.bin"


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
    return "Вітаню, чим можу допомогти?"


@input_error
def add(book: AddressBook, contact: str, phone: str = None):
    contact_new = Name(contact)
    phone_new = Phone(phone) if phone else None
    rec_new = Record(contact_new, phone_new)

    if contact not in book.keys():
        book.add_record(rec_new)
        return f'Добавлено контакт "{contact}" з телефоном: {phone}'
    else:
        book.get(contact).add_phone(phone_new)
        return f'Для існуючого контакту "{contact}" додано номер телефону: {phone}'


@input_error
def add_adres(book: AddressBook, contact: str, *adres):
    x = ' '.join(adres)
    adres_new = Adres(x)
    rec = book.get(contact)
    rec.add_adres(adres_new)
    return f'Updated existing contact "{contact}" with new adres: {x}'


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


def add_note(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    if text.startswith("#"):
        record = HashTag(text)
    else:
        record = Note(text)
    notebook.add_tag(record)
    return f'Запис "{record}" створено'


@ input_error
def congrat(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    return rec.days_to_birthday()


@ input_error
def change(book: AddressBook, contact: str, phone: str = None,):
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


def change_note(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    old_note, new_note = text.split("... ")
    if text.startswith("#"):
        record = HashTag(old_note)
        record_new = HashTag(new_note)
    else:
        record = quick_note(notebook, old_note)
        record_new = Note(new_note)
        record_new.done = record.done
    if record in notebook.note_list or record in notebook.tag_list:
        notebook.change_tag(record, record_new)
        return f'"{record}" змінено на "{record_new}"'
    return f'Запис "{record}" не знайдений'


def change_note_stat(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    record = quick_note(notebook, text)
    if record in notebook.note_list:
        notebook.change_status(record)
        return f'Статус нотатки змінено на "виконано"'
    return f'Запис "{record}" не знайдений'


def del_note(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    if text.startswith("#"):
        record = HashTag(text)
    else:
        record = quick_note(notebook, text)
    if record in notebook.note_list or record in notebook.tag_list:
        notebook.delete(record)
        return f'"{record}" видалений успішно'
    return f'Запис "{record}" не знайдений'


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
        ans = input(f"Are you sure to delete contact {contact}? (Y/N)").lower()
    return f"Контакт {book.remove_record(contact)} Видалено!"


@ input_error
def del_birthday(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    rec.birthday = None
    return f"Контакт {contact}, день народження видалений"


@ input_error
def del_adres(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    rec.adres = None
    return f"Contact {contact}, adres deleted"


@ input_error
def phone(book: AddressBook, *args):
    contact = " ".join(args)
    rec = book.get(contact)
    return f'Контакт "{contact}". {rec.show_phones()}'


@ input_error
def show_all(book: AddressBook, *args):
    if len(book) < PAGE:
        return book.show_all()
    else:
        gen_obj = book.iterator(PAGE)
        for i in gen_obj:
            print(i)
            print("*" * 50)
            input("Нажміть будь-яку клавішу")


@ input_error
def search(book: AddressBook, *args):
    pattern = " ".join(args)
    if len(pattern) < 3:
        return "search string length >= 3"
    result = book.search(pattern)
    if not result:
        return "not found!"
    matches = ""
    for i in result:
        matches += str(i)
    frags = matches.split(pattern)
    highlighted = ""
    for i, fragment in enumerate(frags):
        highlighted += fragment
        if i < len(frags) - 1:
            highlighted += "\033[42m" + pattern + "\033[0m"
    return f"Found {len(result)} match(es):\n" + highlighted


def search_note(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    error = f'Запис не знайдений'
    if text.startswith("#"):
        for tag in notebook.tag_list:
            return f'{tag}' if text in str(tag) else error
    else:
        for note in notebook.note_list:
            return f'{note}' if text in str(note) else error


def show_notes(notebook: NotePad, *args):
    line = ''
    for note in notebook.note_list:
        line += f'дата створення: {note.day.strftime("%d-%m-%Y")}.Зміст: {str(note)}.Статус {note.done}'+'\n'
    return ("список нотатків\n"+line+"кінець списку нотаток")


def show_tags(notebook: NotePad, *args):
    line = ''
    for tag in notebook.tag_list:
        line += f'{str(tag)}'+'\n'
    return ("список тег\n"+line+"кінець списку тег")


@ input_error
def help(*args):
    with open("README.md", "rb") as help_file:
        output = help_file.read().decode("utf-8")
        return output


@ input_error
def exit(book: AddressBook, *args):
    global is_ended
    is_ended = True
    book.save_to_file(DB_FILE_NAME)
    return "До побачення"


def quick_note(notebook: NotePad, text: str):
    content = text.replace("...", "")
    for note in notebook.note_list:
        return note if content in str(note) else None
    record = Note(content)
    return record


@ input_error
def no_command(*args):
    return "Такої команди немає"


COMMANDS = {
    "hello": greet,
    "add email": add_email,
    "add b_day": add_birthday,
    "add address": add_adres,
    "add note": add_note,
    "add": add,
    "congrat": congrat,
    "change note": change_note,
    "change status": change_note_stat,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "show notes": show_notes,
    "show tags": show_tags,
    "search note": search_note,
    "search": search,
    "del note": del_note,
    "del address": del_adres,
    "del phone": del_phone,
    "del b_day": del_birthday,
    "del email": del_email,
    "del contact": del_contact,
    "close": exit,
    "good bye": exit,
    "exit": exit,
    "help": help,
}
WITH_NOTES = [
    add_note,
    change_note,
    change_note_stat,
    show_notes,
    show_tags,
    search_note,
    del_note
]


@ input_error
def command_parser(line: str):
    line_prep = " ".join(line.split())
    for k, v in COMMANDS.items():
        if line_prep.lower().startswith(k + " ") or line_prep.lower() == k:
            return v, re.sub(k, "", line_prep, flags=re.IGNORECASE).strip().rsplit(
                " ")
    return no_command, []


is_ended = False


def main():
    book1 = AddressBook()
    notebook = NotePad()
    if Path(DB_FILE_NAME).exists():
        book1.load_from_file(DB_FILE_NAME)

    while not is_ended:
        s = input(">>>")
        command, args = command_parser(s)
        print(command((notebook if command in WITH_NOTES else book1), *args))


if __name__ == "__main__":
    main()
