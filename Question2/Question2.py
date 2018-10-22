'''Implement a basic encryptor (hint: use ord() and chr() built-in functions; ASCII table)
The encryption algorithm being used here is that we will shift the letter forward 2 places (i.e. a -> c, e -> g, z -> b)
	Example:
	Input: encrypt me
    Output: gpetarv og'''

# Generate string for translation.
initial = ""
for i in range(97, 97 + 26):
    initial += chr(i)

# Add +2 to Ordinal and retranslate.
translated = ""
for i in range(97, 97 + 26):
    translated += chr(i + 2)

print("INITIAL   ", initial)
print("TRANSLATED", translated)

# Maketrans table.
table = str.maketrans(initial, translated)

# String to Translate.
value = "encrypt me"
result = value.translate(table)

print("BEFORE", value)
print("AFTER ", result)
