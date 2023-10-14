disk_size = 1.44  # Объем дискеты с мегабайтах
pages = 100  # Количество страниц в книге
lines = 50  # Количество страниц в книге
characters = 25  # Количество символов в строке
bytes_for_one_char = 4  # Объем памяти для одного символа

disk_size_in_kb = disk_size * 1024 * 1024  # Объем дискеты в байтах
total_char = characters * lines * pages  # Кол-во символов в книге
book_size = bytes_for_one_char * total_char  # Размер одной книги
number_of_books = int(disk_size_in_kb // book_size)

print("Количество книг, помещающихся на дискету:", number_of_books)
