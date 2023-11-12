strange_message = "432H3525el523l52o5 523C532F52"

decrypt_message = ""

for char in strange_message:
    if not char.isnumeric():
        decrypt_message += char

print(decrypt_message)