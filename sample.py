import random


first_names = ["Boke", "Zilipendwa", "Mauwa", "Ninaweza", "Nasim", "wasaka", "Bymungu"]
last_names = ["luhondo", "Issubi", "Sakama", "tonge", "mwaisa", "tuum", "Yana"]

def generate_funny_name():
    """Generate a funny name by combining a random first name and last name."""
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def character_frequency_analysis(name):
    """
    Analyze the name to find the most repeated character case-insensitive.
    Return the character and its frequency.
    """
    name_lower = name.replace(" ", "").lower()
    frequency = {}
    for char in name_lower:
        frequency[char] = frequency.get(char, 0) + 1
    
    most_frequent_char = max(frequency, key=lambda x: (frequency[x], -name_lower.index(x)))
    return most_frequent_char, frequency[most_frequent_char]

def main():
    while True:
        funny_name = generate_funny_name()
        print(f"\nGenerated Funny Name: {funny_name}")

        char, freq = character_frequency_analysis(funny_name)
        print(f"Most Repeated Character: '{char}' (appears {freq} times)")

        user_input = input("\nPress Enter to generate another name or enter 'n'/'N' to quit: ").strip()
        if user_input.lower() == 'n':
            break

    print("\nThank you for using the Funny Name Generator! Press Enter to exit.")
    input()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}. Please try again.")
