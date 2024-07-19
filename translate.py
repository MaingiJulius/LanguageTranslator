habafrom googletrans import Translator


def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text


def main():
    print("Welcome to the Python Translation App!")
    text = input("What do you want to translate: ")
    dest_language = input("Enter the destination language (e.g., 'es' for Spanish, 'fr' for French): ")

    try:
        translated_text = translate_text(text, dest_language)
        print(f"Translated text: {translated_text}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
