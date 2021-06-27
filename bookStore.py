#practice of data types with a book store
print('Provide the following book details.\n')
bookName = input('name: ')
bookId = input('id: ')
bookPrice = input('price: ')
shipInfo = input('free shipping (True/False): ')

if shipInfo == 'True':
    shipInfo = True
elif shipInfo == 'False':
    shipInfo = False
else: 
    print('Please insert the correct input for shipinfo.')


#print(f'\n\nname: {bookName}\nid: {bookId}\nprice: {bookPrice}\nfree shipping: {shipInfo}')
print(f'''
    name: {bookName}
    id: {bookId}
    price: {bookPrice}
    free shipping: {shipInfo}
''')