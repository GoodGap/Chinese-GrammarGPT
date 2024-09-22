#!/usr/bin/python

import sys
import levenshtein
from getopt import getopt
from util import paragraphs
from util import smart_open
from levenshtein import equals_ignore_whitespace_casing
from levenshtein import levenshtein_matrix, edit_graph, merge_graph, transitive_arcs
import levenshtein
import jieba

def resp2edit(source,target,max_unchanged_words = 0):
    """
    :param source:  用来对比的原始句子，一个中文字符串
    :param target:  跑模型得到的句子，一个中文字符串
    :param max_unchanged_words: 在最后结果中反映出的每个编辑序列中，允许出现最大相同词语的个数
    :return:一个列表，里面是形如(pos1,pos2,word1,word2)的元组。
    这里需要特殊说明一下：pos1是发生修改部分的起始词偏移量，pos2是终止的词偏移量；word1是该处发生修改的原始词，word2是该处修改后的词。
    由于是词偏移量，所以要求后端跟模型端的分词手段得一致，否则可能找不到标注的位置。这里暂时采用的是jieba分词器。
    但是jieba现在可能不如spacy好，jieba是单纯基于词表的分词，而spacy不仅有更大的词表，同时还有经过预训练的分词模型。
    目前的jieba偶尔出现分词粒度过小的问题，所以之后可能还要调整。
    在两种情况下，返回是[(-1,-1,'','')]：修改前后完全相等；修改前后差异巨大。遇见这种返回值，可以通过识别pos1来略过。
    """
      # -  Maximum unchanged words when extraction edit. Default 0.
    beta = 0.5
    ignore_whitespace_casing = False  # -  Ignore edits that only affect whitespace and caseing. Default no.
    verbose = False  # -  print verbose output"
    very_verbose = False  # -  print lots of verbose output
    if(source==target):
        return [(-1,-1,'','')]
    target = target.strip()
    source = source.strip()
    target_tok = ' '.join(jieba.cut(target, cut_all=False)).split()
    source_tok = ' '.join(jieba.cut(source, cut_all=False)).split()
    lmatrix1, backpointers1 = levenshtein_matrix(source_tok, target_tok, 1, 1, 1)
    lmatrix2, backpointers2 = levenshtein_matrix(source_tok, target_tok, 1, 1, 2)
    V1, E1, dist1, edits1 = edit_graph(lmatrix1, backpointers1)
    V2, E2, dist2, edits2 = edit_graph(lmatrix2, backpointers2)
    V, E, dist, edits = merge_graph(V1, V2, E1, E2, dist1, dist2, edits1, edits2)
    V, E, dist, edits = transitive_arcs(V, E, dist, edits, max_unchanged_words, very_verbose)
    # Find the shortest path with an empty gold set
    gold = []
    localdist = levenshtein.set_weights(E, dist, edits, gold, verbose, very_verbose)
    editSeq = levenshtein.best_edit_seq_bf(V, E, localdist, edits, very_verbose)
    if ignore_whitespace_casing:
        editSeq = filter(lambda x: not equals_ignore_whitespace_casing(x[2], x[3]), editSeq)
    if editSeq[0][1] - editSeq[0][0] >= 10:
        return [(-1,-1,'','')]
    return list(reversed(editSeq))

