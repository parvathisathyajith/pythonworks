text="The quick brown fox jumps over the lazy dog".casefold()\

seq=("abcdefghijklmnopqrstuvwxyz")

for ch in seq:

    if ch not  in text:

        is_pangram=False
        break

    else:

        is_pangram=True

print(is_pangram)