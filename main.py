with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
word_count = 0

for word in words:
    word_count += 1

letter_count = {}
lower_words = []

for word in words:
    lower_words.append(word.lower())

for word in lower_words:
    for i in word:
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1

used_letters = list(letter_count)
used_letters.sort()


print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document\n")

for letter in used_letters:
    if letter.isalpha():
        print(f"The {letter} character was found {letter_count[letter]} times")

print("--- End report ---")