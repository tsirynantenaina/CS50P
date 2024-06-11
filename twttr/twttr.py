# twttr.py

def omit_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def main():
    text = input("Entrez un texte : ")
    modified_text = omit_vowels(text)
    print(modified_text)

if __name__ == "__main__":
    main()
