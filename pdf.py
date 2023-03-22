import PyPDF2
from nltk.tokenize import word_tokenize

# creating a pdf reader object
reader = PyPDF2.PdfReader('notes.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())
# from nltk.tokenize import sent_tokenize
#
# text = "Hello everyone. Welcome to GeeksforGeeks. You are studying NLP article"
# sent_tokenize(text)


print(word_tokenize(reader))