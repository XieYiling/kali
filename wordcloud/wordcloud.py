# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:10:53 2017

@author: yilingx
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('Jane Eyre.txt','r').read()
wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('test.jpg')
