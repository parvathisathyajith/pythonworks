#return a new list numbers
text=["apple","iphone","orange","potato"]

#words strting with vowels

vowel_words=[w for w in text if w[0] in ['a','e','i','o','u']]

print(vowel_words)

consonant_words=[w for w in text if w[0] not in ['a','e','i','o','u']]

print(consonant_words)

#longest word

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)




