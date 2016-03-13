# -*- coding:utf-8 -*-

import time
from structures import Corpus

__author__ = 'Gree-gorey'

t1 = time.time()

newCorpus = Corpus(u'/home/gree-gorey/Corpus/')

for text in newCorpus.texts(u'json'):
    text.sentence_splitter()
    # print len(text.sentences)
    for sentence in text.sentences:

        # for token in sentence.tokens:
        #     print token.pos, token.content
        # print u'***************'

        # sentence.find_pp()

        # sentence.find_coordination()

        sentence.find_complimentizers()

        sentence.find_names()

        sentence.eliminate_pair_comma()

        # for token in sentence.tokens:
        #     print token.pos, token.content

        sentence.span_splitter()

        sentence.get_shared_tokens()  # loop through all the spans 1

        sentence.split_double_complimentizers()  # loop through all the spans 2

        for span in sentence.spans:  # loop through all the spans 3

            # decide whether span is inserted or embedded or neither
            span.type()
            # print span.tokens[0].content, span.semicolon

        # split embedded span if it contains > 1 predicate
        sentence.split_embedded()

        # for span in sentence.spans:
        #     print span.shared_tokens[0].content, span.tokens[0].content

        # walk through spans and join whenever possible
        sentence.restore_embedded()

        sentence.split_base()

        # for span in sentence.spans:
        #     print span.shared_tokens[0].content, span.tokens[0].content

        sentence.restore_base()

        for span in sentence.spans:
            span.get_boundaries()
            # print span.basic, span.tokens[0].content

    text.write_clause_ann()

    text.copy_into_brat()

t2 = time.time()

print t2 - t1
