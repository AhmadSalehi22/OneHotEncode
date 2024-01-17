from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
  
ps = PorterStemmer()

data = open("text.txt","r")
data = data.read()

for word in data: # stemming the words in data
	word = ps.stem(word)

# allowed dictionary words
alphabet = 'abcdefghijklmnopqrstuvwxyz '

# characters to number
charToNum = dict((c, i) for i, c in enumerate(alphabet))

# one-hoting for the whole text
num_encoded = [charToNum[char] for char in data]
print("Text One-Hot:")
print(num_encoded)
print("\n")

# one hot encode for each letter in text
output = list()
for value in num_encoded:
	letter = [0 for _ in range(len(alphabet))]
	letter[value] = 1
	output.append(letter)
print("Each Letter One-Hot:")
print(output)