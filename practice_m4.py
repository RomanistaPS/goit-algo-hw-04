fh = open('test.txt', 'w', encoding='utf-8')
symbols_written = fh.write('Serhii')
print(symbols_written)
fh.close()

fh = open('test.txt', 'r')
all_read = fh.read()
print(all_read)
fh.close
fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)
fh.close

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел

# Python може працювати з дуже великою кількістю різних кодувань.
s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

print(b'Hello World!'.decode('utf-16'))  #Виведення якщо кодування UTF-8 ми намагаємось декодувати в UTF-16:

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)
byte_array.append(ord("!"))  #Окрім зміни наявних елементів, bytearray дозволяє додавати та видаляти елементи
print(byte_array)

# Порівняння рядків
string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")
