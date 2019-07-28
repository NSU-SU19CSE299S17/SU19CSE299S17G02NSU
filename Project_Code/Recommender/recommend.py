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

# computing cosine similarity matrix using linear_kernal of sklearn
cosine_similarity = linear_kernel(book_description_matrix, book_description_matrix)

indices = pd.Series(book_description['Title'].index)

def customs(name):
    hope = book_description.loc[book_description['Title'] == name]
    m = hope.Book_ID
    m = m-1
    return(m)

# Function to get the most similar books
def recommend(index, cosine_sim=cosine_similarity):
    id = indices[index]
    # Get the pairwsie similarity scores of all books compared to that book,
    # sorting them and getting top 5
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]

    # Get the books index
    books_index = [i[0] for i in similarity_scores]

    # Return the top 5 most similar books using integer-location based indexing (iloc)
    return book_description['Title'].iloc[books_index]