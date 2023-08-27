# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:30:15 2023

@author: Teja Ram Pooniya
@Program: English PAST>PRESENT>FUTURE Tense Checker
"""

import re

# Sample text with tense-related errors
text = "She enjoy playing games. I will goes to the store yesterday."

# Common tense-related errors and their corrections
tense_rules = [
    (r'\b(He|She|It) (.*?)(enjoy|enjoys) (.*?)\b', r'\1 \2enjoys \4'),
    (r'\b(I|You|We|They) (.*?)(go|goes) (.*?) yesterday\b', r'\1 \2went \4 yesterday'),
    (r'\b(I|You|We|They) (.*?)(will) (.*?)\b', r'\1 \2\3 \4'),
]

def apply_tense_rules(text):
    for pattern, replacement in tense_rules:
        text = re.sub(pattern, replacement, text)
    return text

def correct_sentence_fragments(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    corrected_sentences = []
    
    for sentence in sentences:
        if sentence and not sentence.endswith(('.', '!', '?')):
            corrected_sentences.append(sentence + '.')
        else:
            corrected_sentences.append(sentence)
    
    return ' '.join(corrected_sentences)

def correct_tense(text):
    text = apply_tense_rules(text)
    text = correct_sentence_fragments(text)
    return text

corrected_text = correct_tense(text)
print(corrected_text)
