import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

book_description = pd.read_csv('.../Documentation/Dataset/DATA set.csv', encoding = 'latin-1')
book_description = book_description[['Book_ID','Title','Author','Genre1','Genre2','Plot']]

# removing the stop words
books_tfidf = TfidfVectorizer(stop_words='english')
# filling the missing values with empty string
book_description['Plot'] = book_description['Plot'].fillna('')

# computing TF-IDF matrix required for calculating cosine similarity
book_description_matrix = books_tfidf.fit_transform(book_description['Plot'])