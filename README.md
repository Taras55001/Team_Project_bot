Бот "Персональний Помічник".
Цей бот використовується для зберігання важливої інформації такої як телефонна книга, а також список нотаток/завдань з хештегами, і ще даяких інших корисних функцій. Основні команди (всі команди сase-insensitive):

- HELLO: вітається з користувачем
- ADD CONTACT: додає контакт в телефонну книгу. Формат: add contact ім'я (обов'язковий параметр) телефон пошта адреса (необов'язковий праметр) Імена користувачів не можуть складатись тільки з цифр і бути коротше 3-х символів
- ADD_NOTE: додає нотатку(з поточною датою та статусом "не виконано") або хештег до списку нотаток або хештегів відповідно
- CHANGE: змінює телефон(и) контакту. Формат: change ім'я телефон (необов'язковий праметр). Якщо в контакту не було телефона, можно одразу додати. Якщо 1 номер він замінюється на новий. В разі якщо в контакта у книзі більше одного номера телефону можна вибрати який з них змінити
- CHANGE EMAIL: змінює єлектронну почту контакту. Формат: change email ім'я (обов'язковий параметр) електронна поштаю.
- CHANGE BIRTHDAY: змінює дату народження. Формат: change b_day ім'я дата.
- CHANGE ADDRESS: змінює адресу. Формат: change address ім'я адерса.
- CHANGE*NOTE: змінює зміст нотатки або хештегу. Формат: change note старий*зміст новий_зміст(символи "..." в кінці старої нотатки, не обовязково вводити повністю стару нотатку)
- CHANGE_NOTE_STATUS: змінює статус нотатки на "виконано" зі збереженням дати
- PHONE: виводить телефон(и) контакту на екран. Формат: phone ім'я
- DEL PHONE: видаляе телефон контакту. Формат: del phone ім'я телефон (необов'язковий праметр). Якщо номер введено то видаляється саме він, якщо ні то вибираєте який номер видалити
- DEL CONTACT: Видаляє контакт з телефонної книги. Формат: del contact ім'я
- DEL_NOTE: видаляє нотатку або хештег
- ADD ADRESS: Добавляє адрес контакта. Формат: add adres ім'я адрес
- DEL ADRESS: видалити адрес контакта. Формат: del adres ім'я
- ADD EMAIL: додає e-mail контакта. Формат: add email ім'я e-mail
- DEL EMAIL: видаляє e-mail контакта. Формат: del email ім'я
- ADD B_DAY: додає дату народження контакта. Формат: add b_day ім'я дата.
- CONGRAT: виводить список контактів у яких буде день народження в зазначений період. Формат: congrat число_днів
- DEL B_DAY: видаляє дату народження контакта. Формат: del b_day ім'я.
- SHOW ALL: виводить на екран телефонну книгу Формат: show all
- SHOW NOTES: виводить всі нотатки, дату сворення та статус виконання
- SHOW TAGS: виводить всі таги
- SEARCH: виконує пошук по книзі контактів. знаходить всі співпадіння в номерах, іменах або імейлах. рядок пошуку не меньше 3-х символів. Формат: search рядок
- SEARCH_NOTE: знаходить співпадіння в нотатках або хешегах від 1 символу
- SORT FOLDER: розсортовує файли по типах в теці по вказаному щляху. Розпаковує архіви, видаляє порожні теки. Переводить імена файлів і тек транслітом з кирилиці. Формат: sort folder шлях_до_теки. типи файлів можна задавати в конігураційному файлі config.JSON. Назва теки "archives" незмінна!
- CLOSE, GOOD BYE, EXIT: виходить в операційну систему
- HELP: виводить цей мануал на екран Імена файлв з телефонною книгою і з книгою нотаток також прописані в файлі config.JSON
