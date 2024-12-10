#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from memorization.word_classes import Status

class StatusManager:
    def __init__(self):
        self.correct_first_time = set()
        self.failed_first_time = set()

    def update_status(self, word_pair, result):
        if word_pair.status is None:
            if result == 'correct':
                self.correct_first_time.add(word_pair)
                word_pair.status = Status.CORRECT_FIRST_TIME
            elif result == 'incorrect':
                self.failed_first_time.add(word_pair)
                word_pair.status = Status.FAILED_FIRST_TIME


def view_progress(status_manager):
    print("\nWords correctly answered on the first attempt:")
    if status_manager.correct_first_time:
        for pair in status_manager.correct_first_time:
            print(f"{pair.french} - {pair.english}")
    else:
        print("None")

    print("\nWords failed on the first attempt:")
    if status_manager.failed_first_time:
        for pair in status_manager.failed_first_time:
            print(f"{pair.french} - {pair.english}")
    else:
        print("None")

