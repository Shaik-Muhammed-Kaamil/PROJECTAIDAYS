import pandas as pd
from googletrans import Translator

# Load the dataset
def load_data(file_path):
    """
    Load the CSV dataset containing world important dates.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        if 'Date' not in data.columns or 'Event' not in data.columns:
            raise ValueError("Dataset must contain 'Date' and 'Event' columns.")
        return data
    except Exception as e:
        print(f"Error loading the dataset: {e}")
        return None

def find_event(date, data):
    """
    Find an event corresponding to a given date in the dataset.

    Args:
        date (str): The date entered by the user (format: "DD-MM" or "MM-DD").
        data (pandas.DataFrame): The dataset containing important dates.

    Returns:
        str: The event description or a message if the date is not found.
    """
    event = data[data['Date'] == date]
    if not event.empty:
        return event.iloc[0]['Event']  # Return the event description
    else:
        return "Sorry, no event found for the given date."

def translate_text(text, language):
    """
    Translate the text into a specified language using Google Translate.

    Args:
        text (str): The text to translate.
        language (str): Target language code (e.g., 'ur' for Urdu, 'te' for Telugu).

    Returns:
        str: Translated text.
    """
    translator = Translator()
    try:
        translated = translator.translate(text, dest=language)
        return translated.text
    except Exception as e:
        return f"Error during translation: {e}"

def chatbot(data):
    """
    A chatbot that answers user queries about important dates and translates explanations.

    Args:
        data (pandas.DataFrame): The dataset containing important dates.
    """
    print("📜 Welcome to the Historical Dates Chatbot!")
    print("Enter a date in the format 'DD-MM-YYYY' to learn about its historical importance.")
    print("Type 'exit' to quit the chatbot.")

    while True:
        user_input = input("\nEnter a date or 'exit': ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye! Keep exploring history! 🌟")
            break

        event = find_event(user_input, data)
        print(f"🗓 Event: {event}")
        
        # Ask if the user wants a translation
        translate_option = input("Would you like a translation of this explanation? (yes/no): ").strip().lower()
        if translate_option == "yes":
            print("Choose a language for translation:")
            print("1. Urdu (ur)")
            print("2. Telugu (te)")
            language_choice = input("Enter your choice (1 or 2): ").strip()
            
            if language_choice == "1":
                translated_event = translate_text(event, "ur")
                print(f"📖 Translation in Urdu: {translated_event}")
            elif language_choice == "2":
                translated_event = translate_text(event, "te")
                print(f"📖 Translation in Telugu: {translated_event}")
            else:
                print("Invalid choice. Translation skipped.")

if __name__ == "__main__":
    # Load the dataset
    file_path = "C:\\Users\\USER\\Documents\\Project aihackathon\\.venv\\simple-chatbot-main\\World_Important_Dates.csv"  # Path to the uploaded dataset
    data = load_data(file_path)
    
    if data is not None:
        print("Dataset loaded successfully!")
        chatbot(data)
    else:
        print("Failed to load the dataset. Exiting.")
