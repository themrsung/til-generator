# TIL Generator

import random
from pyjosa.josa import Josa

prefixes = open("text/prefixes.txt", "r", encoding="UTF-8").readlines()
adjectives = open("text/adjectives.txt", "r", encoding="UTF-8").readlines()
words = open("text/words.txt", "r", encoding="UTF-8").readlines()
adverbs = open("text/adverbs.txt", "r", encoding="UTF-8").readlines()
suffixes = open("text/suffixes.txt", "r", encoding="UTF-8").readlines()

for i in range(len(prefixes)):
    prefixes[i] = prefixes[i].strip()
    
for i in range(len(adjectives)):
    adjectives[i] = adjectives[i].strip()
    
for i in range(len(words)):
    words[i] = words[i].strip()
    
for i in range(len(adverbs)):
    adverbs[i] = adverbs[i].strip()
    
for i in range(len(suffixes)):
    suffixes[i] = suffixes[i].strip()

def generate_til():
    til = ""

    til += prefixes[random.randrange(0, len(prefixes))]
    til += " "
    til += adjectives[random.randrange(0, len(adjectives))]
    til += " "
    word =  words[random.randrange(0, len(words))]
    til += word
    til += Josa.get_josa(word, "을")
    til += " "
    til += adverbs[random.randrange(0, len(adverbs))]
    til += " "
    til += suffixes[random.randrange(0, len(suffixes))]
    til += "."

    return til

number_of_sentences = input("몇 문장을 원하시나요?")

def run(num):
    value = ""
    for i in range(int(num)):
        value += generate_til()
        value += " "
    value = value[:-1]
    return value

print(run(number_of_sentences))