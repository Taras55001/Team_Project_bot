from main import add_note, change_note, change_note_stat, del_note, search_note, NotePad

notebook = NotePad()
print(add_note(notebook, "test"))
print(add_note(notebook, "test1"))
print(add_note(notebook, "#test"))
print(change_note(notebook, "#test", "#test1"))
print(change_note_stat(notebook, "test"))
print(del_note(notebook, "test"))
print(search_note(notebook, "te"))
print(search_note(notebook, "#te"))
