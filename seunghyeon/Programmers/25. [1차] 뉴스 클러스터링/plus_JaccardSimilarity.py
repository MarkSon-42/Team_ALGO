# -------------------- < Jaccard Similarity > --------------------


# 1. 자카드 유사도란?
    # 2개의 집합A, B가 있을 때 두 집합의 합집합 중 교집합의 비율
    # 두 집합이 완전히 같을 때 : 자카드 유사도는 1
    # 두 지합에 교집합이 없을 때 : 자카드 유사도는 0


# 2. 자카드 유사도의 활용
    # 자연어처리 분야에서의 활용
    # 집합이 하나의 문서에 해당
    # 자카드 유사도는 문서 간 얼마나 많은 종류의 단어가 중복되었는지에 집중
    # 단어마다 중복 횟수는 고려하지 X
    # 즉, 자카드 유사도는 특정 단어가 여러 번 겹쳐도 얼마나 다른 종류의 단어가 겹치는지에 따라 문서 유사도를 계산


# .
# .
# .


# 3. 연습해보기

# step 1) 문서 샘플
doc1 = "The fat cat sat on the mat"
doc2 = "The lovely dog slept on the table"


# step 2) 문서 토큰화
doc1_tokenized = doc1.split()
    ## ['The', 'fat', 'cat', 'sat', 'on', 'the', 'mat']
doc2_tokenized = doc2.split()
    ## ['The', 'lovely', 'dog', 'slept', 'on', 'the', 'table']


# step 3) 합집합 계산
doc_union = set(doc1_tokenized).union(set(doc2_tokenized))
    ## {'sat', 'fat', 'on', 'the', 'slept', 'lovely', 'cat', 'dog', 'The', 'table', 'mat'}


# step 4) 교집합 계산
doc_intersection = set(doc1_tokenized).intersection(set(doc2_tokenized))
    ## {'the', 'The', 'on'}


# step 5) 합집합 대 교집합 비율 계산
jaccard_similarity = len(doc_intersection) / len(doc_union)
print(jaccard_similarity)
    ## 0.2727272727272727
print(f"jaccard similarity: {jaccard_similarity:.2f}")
    ## jaccard similarity: 0.27
