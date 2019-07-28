import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

book_description = pd.read_csv('.../Documentation/Dataset/DATA set.csv', encoding = 'latin-1')
book_description = book_description[['Book_ID','Title','Author','Genre1','Genre2','Plot']]
