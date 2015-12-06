# -*- coding: utf-8 -*-

import feedparser
import re

#RSSフィードのタイトルと、単語頻度のディクショナリを返す
def getwordcounts(url):
    #フィードをパースする
    d = feedparser.parse(url)
    wc={}

    #すべてのエントリーをループする
    for e in d.entries:
        if  'summary' in e: summary = e.summary
        else: summary=e.summary

        #単語のリストを取り出す
        words=getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1
        return d.feed.title,wc


def getwords(html):
    #すべてのHTMLタグを取り除く
    txt=re.compile(r'<[^>]+>').sub('',html)

    #すべての非アルファベット文字で分割する
    words=re.compile(r'[^A-Z^a-z]+').split(txt)

    #小文字に変換する
    return[word.lower() for word in words if word!='']
