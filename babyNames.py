import requests
from random import randint

url = 'https://www.usna.edu/Users/cs/roche/courses/s15si335/proj1/files.php%3Ff=names.txt&downloadcode=yes'

r = requests.get(url)
text = r.text
# print(text)

individual_words = text.split()
# print(individual_words)
random_number = randint(0, len(individual_words))

print(individual_words[random_number])
