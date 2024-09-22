# This file is part of the NUS M2 scorer.
# The NUS M2 scorer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# The NUS M2 scorer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# file: m2scorer.py
# 
# score a system's output against a gold reference 
#
# Usage: m2scorer.py [OPTIONS] proposed_sentences source_gold
# where
#  proposed_sentences   -   system output, sentence per line
#  source_gold          -   source sentences with gold token edits
# OPTIONS
#   -v    --verbose             -  print verbose output
#   --very_verbose              -  print lots of verbose output
#   --max_unchanged_words N     -  Maximum unchanged words when extracting edits. Default 2."
#   --beta B                    -  Beta value for F-measure. Default 0.5."
#   --ignore_whitespace_casing  -  Ignore edits that only affect whitespace and caseing. Default no."
#

import sys
# import levenshtein
from scripts import levenshtein
from getopt import getopt
from scripts.util import paragraphs
from scripts.util import smart_open



def load_annotation(gold_file):
    source_sentences = []
    gold_edits = []
    fgold = open(gold_file, 'r', encoding='utf-8')
    puffer = fgold.read()
    fgold.close()
    # puffer = puffer.decode('utf8')
    for item in paragraphs(puffer.splitlines(True)):
        item = item.splitlines(False)
        sentence = [line[2:].strip() for line in item if line.startswith('S ')]
        assert sentence != []
        annotations = {}
        for line in item[1:]:
            if line.startswith('I ') or line.startswith('S '):
                continue
            assert line.startswith('A ')
            line = line[2:]
            fields = line.split('|||')
            start_offset = int(fields[0].split()[0])
            end_offset = int(fields[0].split()[1])
            etype = fields[1]
            if etype == 'noop':
                start_offset = -1
                end_offset = -1
            corrections =  [c.strip() if c != '-NONE-' else '' for c in fields[2].split('||')]
            # NOTE: start and end are *token* offsets
            original = ' '.join(' '.join(sentence).split()[start_offset:end_offset])
            annotator = int(fields[5])
            if annotator not in annotations.keys():
                annotations[annotator] = []
            annotations[annotator].append((start_offset, end_offset, original, corrections))
        tok_offset = 0
        for this_sentence in sentence:
            tok_offset += len(this_sentence.split())
            source_sentences.append(this_sentence)
            this_edits = {}
            # for annotator, annotation in annotations.iteritems():
            for annotator, annotation in annotations.items():
                this_edits[annotator] = [edit for edit in annotation if edit[0] <= tok_offset and edit[1] <= tok_offset and edit[0] >= 0 and edit[1] >= 0]
            if len(this_edits) == 0:
                this_edits[0] = []
            gold_edits.append(this_edits)
    return (source_sentences, gold_edits)

  
def print_usage():  
    print("Usage: m2scorer.py [OPTIONS]proposed_sentences gold_source", file=sys.stderr)  
    print("where", file=sys.stderr)  
    print("  proposed_sentences   -   system output, sentence per line", file=sys.stderr)  
    print("  source_gold          -   source sentences with gold token edits", file=sys.stderr)  
    print("OPTIONS", file=sys.stderr)  
    print("  -v    --verbose                   -  print verbose output", file=sys.stderr)  
    print("        --very_verbose              -  print lots of verbose output", file=sys.stderr)  
    print("        --max_unchanged_words N     -  Maximum unchanged words when extraction edit. Default 2.", file=sys.stderr)  
    print("        --beta B                    -  Beta value for F-measure. Default 0.5.", file=sys.stderr)  
    print("        --ignore_whitespace_casing  -  Ignore edits that only affect whitespace and caseing. Default no.", file=sys.stderr)


def M2Score(system_sentences, source_sentences, gold_edits, max_unchanged_words=2, beta=0.5, ignore_whitespace_casing= False, verbose= False, very_verbose= False, is_print_usage = True):
    """
    计算 M2Score 的主函数
    :params system_sentences:str,用户自己生成的改句
    :params source_sentences:str,提供的原始病句
    :params gold_edits:str,对source_sentences的标准编辑操作集合
    :params max_unchanged_words:int,一次编辑操作序列中允许不变的最大单词数量,默认为2
    :params beta:用来选择评测标准，默认为0.5，代表输出F0.5，这个应该不可更改
    :params ignore_whitespace_casing:选择是否忽略那些只涉及空格等的编辑操作，默认为false
    :params verbose:输出详细信息，包含病句的基本信息和修改信息等
    :params very_verbose:输出更加详细的信息，包含晶格图内部路径的计算情况
    :params is_print_usage: 是否打印帮助文本，默认 True
    :returns tuple: 返回准确率、查全率和 F1 分数
    """
    if is_print_usage:
        print_usage()
    return levenshtein.batch_multi_pre_rec_f1(system_sentences, source_sentences, gold_edits, max_unchanged_words, beta, ignore_whitespace_casing, verbose, very_verbose)

if __name__ == "__main__":

    # 设置超参数，这里取默认
    max_unchanged_words=2
    beta = 0.5
    ignore_whitespace_casing= False
    verbose = False
    very_verbose = False

    # 使用的句子的地址
    system_file = "example\system"
    gold_file = "example\source_gold"

    # load source sentences and gold edits
    source_sentences, gold_edits = load_annotation(gold_file)

    # load system hypotheses
    fin = smart_open(system_file, 'r')
    # system_sentences = [line.decode("utf8").strip() for line in fin.readlines()]
    system_sentences = [line.strip() for line in fin.readlines()]
    fin.close()

    # 这里运行主函数
    p, r, f1 = M2Score(system_sentences, source_sentences, gold_edits)

    print("Precision   : %.4f" % p)
    print("Recall      : %.4f" % r)
    print("F_%.1f       : %.4f" % (beta, f1))

