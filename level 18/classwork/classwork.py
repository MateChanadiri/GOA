# .upper() - დიდ ასოებს ხდის
i = "hello".upper()
print(i)
# .lower() - პატარა ასოებს ხდის
i = "hello".lower()
print(i)
# .capitalize() - პირველ ასოს დიდს ხდის
i = "hello".capitalize()
print(i)
# .swapcase() - პატარა ასოებს დიდს ხდის და დიდ ასოებს პატარას
i = "HelLo".swapcase()
print(i)
# .find() - პოულობს რიცხვს ან ასოს
i = "hello"
i = i.find("h")
print(i)
# len() - პოულობს რამდენი რაღაცაა შეტანილი
i = "hello"
i = len(i)
print(i)
# .index()
i = ["cat", "dog", "tiger"]
position = i.index("dog")
print(position)
# .append() - ბოლოში უმატებს შიგნით ჩაწერილ მნიშვნელობას
i = ["Hello"]
i = i.append("Hi")
print(i)
# .insert() - უმატებს მის შიგნით ჩაწერილ მნიშვნელობას აქვს ორი არგუმენტი სად უნდა ჩაჯდეს და რა უნდა ჩაჯდეს
i = ["Hello"]
i = i.insert(0, "Hi")
print(i)
# .pop() - უშლის ერთ რაღაცას
i = ["Hello"]
i = i.pop("Hello")
print(i)
# .remove() - უშლის არჩეულ მნიშვნელობას
i = ["Hello"]
i = i.remove("H")
print(i)