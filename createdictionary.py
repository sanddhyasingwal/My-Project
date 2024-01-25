def create_dictionary():
    hindi_dict = {}
    num_entries = int(input("Enter the number of dictionary entries: "))

    for _ in range(num_entries):
        hindi_word = input("Enter Hindi word: ")
        english_translation = input("Enter English translation: ")
        hindi_dict[hindi_word] = english_translation

    return hindi_dict


def lookup_translation(dictionary):
    hindi_word = input("Enter the Hindi word to look up: ")

    if hindi_word in dictionary:
        translation = dictionary[hindi_word]
        print(f"The English translation of '{hindi_word}' is '{translation}'.")
    else:
        print(f"'{hindi_word}' not found in the dictionary.")


# Create the dictionary
my_dictionary = create_dictionary()

# Provide an option to look up translations
while True:
    option = input("Enter '1' to look up translations, '0' to exit: ")

    if option == '1':
        lookup_translation(my_dictionary)
    elif option == '0':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please enter '1' or '0'.")
