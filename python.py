# -*- coding: utf-8 -*-
"""Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tv26SBZCOIIoRZ3o3GX-VkZzXpIqz9WY
"""

n = "hello all"

print(n)

type (n)

n=2

if (n>10):
   print("n is greater than 10")

elif (n<5):
   print("n is smaller than 5")

else:
   print("n is between 5 and 10")

for ele in range(40, 50):
  print(ele)

for ele in range(10, 30, 5):
  print(ele)

def calculator(a, b):
  sum = a+b
  diff = a-b
  prod = a*b
  divide = a/b

  return sum,diff,prod,div

li = [2,4,6,8,10]

print(li)

print(li[0])
print(li[-1])

li[1:5]

!wget https://www.dropbox.com/s/c6lmwqz67kpdsiq/review_dataset.csv

import pandas as pd
import numpy as np

df = pd.read_csv("review_dataset.csv")

df

df.shape

df["label"][0:20]

df['review'][1]

nltk

import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

sw = stopwords.words('english')
sw

len(sw)

def clean_text(sample):
  sample = sample.upper()
  sample = sample.replace("<br /><br /","")
  sample = re.sub("[^a-zA-Z]+", " ", sample)
  sample = sample.split(" ")
  sample = [word for word in sample if word not in sw]
  sample = " ".join(sample)
  return sample

clean_text(df['review'][1])

df['review'] = df['review'].apply(clean_text)

df['review']

