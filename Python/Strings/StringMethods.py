
text = ' MY name is David'

print(text.lower()) # my name is david
print(text.upper()) # MY NAME IS DAVID
print(text.capitalize()) # my name is david
print(text.swapcase()) # my NAME IS dAVID
print(text.title()) # My Name Is David

text = text.lower()
print(text.islower())
text = text.upper()
print(text.isupper())
text = '12344565'
print(text.isalnum('2'))