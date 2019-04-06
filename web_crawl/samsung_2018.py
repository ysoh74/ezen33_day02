from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
import nltk
nltk.download()

ctx = 'C:/Users/Ysoh/PycharmProjects/day02/data/'
filename = ctx + "kr-Report_2018.txt"

with open(filename, 'r', encoding='UTF-8') as f:
    texts = f.read()
# print(texts[:300])

texts = texts.replace('\n', '')
tokenizer = re.compile('[^ ㄱ-힣]+')
texts = tokenizer.sub('', texts)
# print(texts[:300])

tokens = word_tokenize(texts)
tokens[:7]
