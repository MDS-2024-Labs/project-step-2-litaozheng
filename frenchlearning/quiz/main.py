#!/usr/bin/env python
# coding: utf-8

# In[2]:


from memorization.word_initializer import initialize_word_pairs
from quiz.manager import StatusManager, view_progress
from quiz.quizzing import display_word_pairs, quiz_user

def main():
    word_pairs = initialize_word_pairs()
    status_manager = StatusManager()

    print("Welcome to the French Learning Program!\n")

    while True:
        print("Select Difficulty Level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("Type 'end' to finish and see your results.\n")

        difficulty_choice = input("Enter the number corresponding to your choice: ").strip()
        if difficulty_choice.lower() == 'end':
            break
        elif difficulty_choice not in ['1', '2', '3']:
            print("Invalid input. Please enter 1, 2, 3, or 'end' to finish.")
            continue

        difficulty_levels = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}
        selected_difficulty = difficulty_levels[difficulty_choice]

        session_word_pairs = [wp for wp in word_pairs if wp.difficulty == selected_difficulty]

        while True:
            num_words_input = input("How many words would you like to learn this session? ").strip()
            if num_words_input.isdigit():
                num_words = int(num_words_input)
                break
            elif num_words_input.lower() == 'end':
                break
            else:
                print("Please enter a valid number or type 'end' to finish.")

        if num_words_input.lower() == 'end':
            break

        if len(session_word_pairs) >= num_words:
            session_word_pairs = random.sample(session_word_pairs, num_words)
        else:
            print(f"Only {len(session_word_pairs)} words available in this difficulty level.")
            session_word_pairs = session_word_pairs

        # Display words for memorization
        proceed = display_word_pairs(session_word_pairs)
        if not proceed:
            break

        # Start the quiz
        wrong_pairs = quiz_user(session_word_pairs, status_manager)
        if wrong_pairs is None:
            # User chose to exit during the quiz
            break
        elif wrong_pairs == 'end':
            break

        # If there are wrong answers, allow the user to retry them
        while wrong_pairs:
            print("Review the words you got wrong:\n")
            for pair in wrong_pairs:
                print(f"{pair.french} - {pair.english}")
            proceed = display_word_pairs(wrong_pairs)
            if not proceed:
                break
            wrong_pairs = quiz_user(wrong_pairs, status_manager)
            if wrong_pairs is None or wrong_pairs == 'end':
                break

    # After user chooses to end the test
    print("\nTest completed. Here's your progress:")
    total_first_attempts = len(status_manager.correct_first_time) + len(status_manager.failed_first_time)
    if total_first_attempts > 0:
        correctness_percentage = (len(status_manager.correct_first_time) / total_first_attempts) * 100
        print(f"Correctness Percentage (based on first-time answers): {correctness_percentage:.2f}%\n")
    else:
        print("No words were attempted.\n")

    view_progress(status_manager)
    print("Thank you for using the French Learning Program!")


# In[ ]:




