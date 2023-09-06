# -------------------- < Text 유사도를 측정하는 방법들> --------------------

# < 1. python 내장 모듈 difflib 이용 >

# ///code/// ratio() 메서드를 이용하여 두 문자열(단어)의 유사도를 검사하는 함수
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

a = 'banana'
b = 'manana'
c = 'strawberry'

print(b, similar(a, b))
print(c, similar(a, c))
    ## manana 0.8333333333333334
    ## strawberry 0.125


# .
# .
# .


# < 2. 코사인 유사도 (Cosine Similarity) >

# ///code/// 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = ("Hi, my name is Tommy.", 
"Hi, my name is Tom.")

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
cos_similar = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print(cos_similar[0][0])
    ## 0.6694188517266485
    

# .
# .
# .


# < 3. 자카드 유사도 (Jaccard Similarity) >
    # plus_JaccardSimilarity.py 파일 참고
