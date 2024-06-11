def main():
    word = input("Input: ")
    print("Output:", shorten(word))

def shorten(word):
    vowels = "aeiouAEIOU"
    shortened = ""
    for char in word:
        if char not in vowels:
            shortened += char
    return shortened

if __name__ == "__main__":
    main()
