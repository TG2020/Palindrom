def palindrom(word):
    word = word.lower()
    backword="".join(reversed(word))

    if word.isalnum():
        print("Czy to słowo jest palindromem?")
        print(word==backword)

palindrom("kajak")

#dokumentacja w pliku README
