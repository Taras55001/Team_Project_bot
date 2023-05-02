from main import command_parser, NotePad, WITH_NOTES, AddressBook
notebook = NotePad()
book1 = AddressBook()
def test():
    s = "add note test note"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add note test note2"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add note test note4"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add note some text in note"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag te... #bsds"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag te... #csds"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag te... #jsds"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag te... #jsda"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag so... #c"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag so... #a"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "add tag 2... #2"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "search note #a"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "change note te... changing test pass by content"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "change note #a... changing test pass by #"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "change status co..."
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "change status #2"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "change status #a"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "show notes"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "del note #2"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "del note conte..."
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))
    s = "show notes"
    command, args = command_parser(s)
    print(command((notebook if command in WITH_NOTES else book1), *args))