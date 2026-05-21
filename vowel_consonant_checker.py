# Vowel or Consonant
# Input a character → check vowel or consonant.

# Prompt the user for a character
character = input("Enter an alphabetic character: ").lower()

# 1. Check length
if len(character) != 1:
    print("Please enter only a single character!")
# 2. Check if it's a valid letter
elif not character.isalpha():
    print(f"'{character}' is not an alphabetic letter!")
# 3. Process the letter
else:
    # A sleek way to check all vowels at once
    if character in "aeiou":
        print(f"'{character}' is a vowel.")
    else:
        print(f"'{character}' is a consonant.")