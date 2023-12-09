with open ('quotes.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
while True:
    author = f'\n({input("Введіть автора")})'
    quote = input('Бажаєте додати цитату')
    if quote=='так':
        quote = input()
        author = input("Введіть автора:")
        with open('quoter.txt', 'a' ,encoding='utf-8')as file:
    else:
        break
with open('quotes.txt','a' ,encoding='utf-8')as file:
    deta = file.white(author)

with open('quoter.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)    