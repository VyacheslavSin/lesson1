from cmath import phase


phones=['iPhone 12', 'Samsung Galaxy S21', 'Xiaomi Mi11']
print(phones)
count=len(phones)
print(count)
phones.append('iPhone 13')
print(phones)
count=len(phones)
print(count)
print (phones.count('iPhone 12'))
print(phones.count('Xiaomi Mi11'))
print(phones[1])
print(phones[0])
phones=['iPhone 12', 'Samsung Galaxy S21', 'Xiaomi Mi11']
print(phones[1:2])
print(phones[:2])
print(phones[-1])
print(phones.index('Xiaomi Mi11'))
phones.sort()
print(phones)
print(phones.index("Xiaomi Mi11"))
print("iPhone 12" in phones)
