import emoji

def main():
    user_input = input("Input: ")
    emojized_output = emoji.emojize(user_input, language='alias')
    print(f"Output: {emojized_output}")

if __name__ == "__main__":
    main()
