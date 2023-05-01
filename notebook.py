from ab_classes import Note, NotePad, HashTag


def add_note(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    if text.startswith("#"):
        record = HashTag(text)
    else:
        record = Note(text)
    notebook.add_tag(record)
    return f'Запис "{record}" створено'

def change_note(notebook: NotePad, *args):
    text = f'{" ".join(args)}'
    old_note, new_note = text.split("... ")
    if text.startswith("#"):
        record = HashTag(old_note)
        record_new = HashTag(new_note)
    else:
        try:
            record = quick_note(notebook, old_note)
            record_new = Note(new_note)
            record_new.done = record.done
        except AttributeError:
            return "Ви вели невірно запис, спробуйте й ще раз"
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

def quick_note(notebook: NotePad, text: str):
    content = text.replace("...", "")
    for note in notebook.note_list:
        return note if content in str(note) else None
    record = Note(content)
    return record

WITH_NOTES = [
    add_note,
    change_note,
    change_note_stat,
    show_notes,
    show_tags,
    search_note,
    del_note,
    ]