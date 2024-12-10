#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def display_word_pairs(word_pairs):
    print("\nPlease memorize the following French-English word pairs:\n")
    for pair in word_pairs:
        print(f"{pair.french} - {pair.english}")
    print("\nWhen you are done memorizing, type 'start' to begin the quiz, or 'exit' to finish and see your results.\n")
    while True:
        user_input = input("Type 'start' to begin the quiz: ").strip().lower()
        if user_input == 'start':
            return True
        elif user_input == 'exit':
            return False
        else:
            print("Please type 'start' or 'exit'.")


def clear_screen():
    print("\n" * 50)  # Simulate clearing the screen


def quiz_user(word_pairs, status_manager):
    clear_screen()
    print("Quiz Time! Please provide the English meaning for the following French words:")
    print("Type 'exit' to finish and see your results, or 'hint' for a hint.\n")
    wrong_pairs = []
    for pair in word_pairs:
        while True:
            answer = input(f"{pair.french}: ").strip().lower()
            if answer == 'exit':
                return None
            elif answer == 'hint':
                print(f"Hint: The word starts with '{pair.english[0]}'.")
                continue
            if answer == pair.english.lower():
                print("Correct!\n")
                status_manager.update_status(pair, 'correct')
                break
            else:
                print(f"Incorrect. The correct answer is '{pair.english}'.\n")
                status_manager.update_status(pair, 'incorrect')
                wrong_pairs.append(pair)
                break
    return wrong_pairs

