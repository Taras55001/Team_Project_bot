Бот "Персональний Помічник".
Цей бот використовується для зберігання важливої інформації такої як телефонна книга, а також список нотаток/завдань з хештегами, і ще даяких інших корисних функцій.
Основні команди (всі команди сase-insensitive):
- HELLO: вітається з користувачем
- ADD: додає контакт в телефонну книгу. Формат: add ім'я телефон (необов'язковий праметр)
Імена користувачів не можуть складатись тільки з цифр і бути коротше  3-х символів
- CHANGE: змінює телефон(и) контакту. Формат: change ім'я телефон (необов'язковий праметр). Якщо в контакту не було телефона, можно одразу додати. Якщо 1 номер він замінюється на новий. В разі якщо в контакта у книзі більше одного номера телефону можна вибрати який з них змінити
- PHONE: виводить телефон(и) контакту на екран. Формат: phone ім'я
- DEL PHONE: видаляе телефон контакту. Формат: del phone ім'я телефон (необов'язковий праметр). Якщо номер введено то видаляється саме він, якщо ні то вибираєте який номер видалити
- DEL CONTACT: Видаляє контакт з телефонної книги. Формат: del contact ім'я
- ADD ADRES: Добавляє адрес контакта. Формат: add adres ім'я адрес
- DEL ADRES: видалити адрес контакта. Формат: del adres ім'я
- ADD EMAIL: додає e-mail контакта. Формат: add email ім'я e-mail
- DEL EMAIL: видаляє e-mail контакта. Формат: del email ім'я
- ADD B_DAY: додає дату народження контакта. Формат: add b_day ім'я дата.
- CONGRAT: рахує кількість днів до дня народження контакта.  Формат: congrat ім'я дата
- DEL B_DAY: видаляє дату народження контакта. Формат: del b_day ім'я.
- SHOW ALL: виводить на екран телефонну книгу Формат: show all
- SEARCH: виконує пошук по книзі контактів. знаходить всі співпадіння в номерах, іменах або імейлах. рядок пошуку не меньше 3-х символів. Формат: search рядок
- SORT FOLDER: розсортовує файли по типах в теці по вказаному щляху. Розпаковує архіви, видаляє порожні теки. Переводить імена файлів і тек транслітом з кирилиці. Формат: sort folder шлях_до_теки. типи файлів можна задавати в конігураційному файлі config.JSON. Назва теки "archives" незмінна!
- CLOSE, GOOD BYE, EXIT: виходить в операційну систему
- HELP: виводить цей мануал на екран