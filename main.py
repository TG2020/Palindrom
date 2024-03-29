word = input("Podaj słowo: ")
def is_palindrome(value):
    value = "".join([x for x in value.lower() if x.isalnum()])
    return value == value[::-1]

print("To jest palindrom." if is_palindrome(word) else "To nie jest palindrom.")
