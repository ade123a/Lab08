import requests
import re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
def get_headings(soup):
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print("Number of headings: ", len(headings))
    return headings

def get_links(soup):
    links = soup.find_all('a')
    print("Number of links: ", len(links))
    return links

def get_paragraphs(soup):
    paragraphs = soup.find_all('p')
    print("Number of paragraphs: ", len(paragraphs))
    return paragraphs

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = get_headings(soup)
    links = get_links(soup)
    paragraphs = get_paragraphs(soup)
    
    
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

text = soup.get_text()
words = re.findall(r'\b\w+\b', text.lower())
count = 0

value = input("Enter the word you want to search: ")
#4
for word in words:
    if value.lower() == word:
        count += 1

print("The word", value, "is found", count, "times")

#5
word_dict = {}
for word in words: 
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
        
word_counts = [(word, count) for word, count in word_dict.items()]
word_counts.sort(key=lambda x: x[1], reverse=True)

for word, freq in word_counts[:5]:
    print(f"Word: {word}, Frequency: {freq}")

#6
largest_paragraph = max(paragraphs, key=lambda p: len(p.get_text().split()), default=None)
print("Largest paragraph:", largest_paragraph.get_text())
print("Largest paragraph length:", len(largest_paragraph.get_text().split()))


import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [len(headings), len(links), len(paragraphs)]
colors = ['red', 'green', 'blue']
plt.bar(labels, values, color=colors)
plt.title('Group 8 - Web Analyzer')
plt.ylabel('Count')
plt.show()


