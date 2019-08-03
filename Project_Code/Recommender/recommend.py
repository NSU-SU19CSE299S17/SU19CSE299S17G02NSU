import pandas as pd
import  csv
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


book_description = pd.read_csv('E:/DATA set.csv', encoding = 'latin-1')
for line in book_description:
   books_tfidf = TfidfVectorizer(stop_words='english')
   book_description['Plot'] = book_description['Plot'].fillna('')
   book_description_matrix = books_tfidf.fit_transform(book_description['Plot'])
   cosine_similarity = linear_kernel(book_description_matrix, book_description_matrix)
   indices = pd.Series(book_description['Title'].index)

def customs(name):
    hope = book_description.loc[book_description['Title'] == name]
    m = int(hope.Book_ID)
    m = m-1
    return(m)

# Function to get the most similar books
def recommend(index, cosine_sim=cosine_similarity):
    id = indices[index]
    # Get the pairwsie similarity scores of all books compared to that book,
    # sorting them and getting top 5
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:4]

    # Get the books index
    books_index = [i[0] for i in similarity_scores]

    # Return the top 5 most similar books using integer-location based indexing (iloc)
    #return list(book_description['Title'].iloc[books_index])

    meep = list(book_description['Title'].iloc[books_index])
    fin = meep
    #fin = {"B1": meep[0], "B2": meep[1], "B3": meep[2]}
    return fin