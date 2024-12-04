text="this is a simple python program that print most recursive word.this is simple"

def most_frequent(text):
    words=text.split(" ")
    words=max(words,key=lambda w:words.count(w))

    freq_word=most_frequent(text)
print(freq_word)

