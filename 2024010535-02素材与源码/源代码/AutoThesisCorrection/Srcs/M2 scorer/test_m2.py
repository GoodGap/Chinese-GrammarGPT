from scripts import levenshtein
from scripts.m2scorer import M2Score, load_annotation
from scripts.util import smart_open

# 设置超参数，这里取默认
max_unchanged_words = 2
beta = 0.5
ignore_whitespace_casing = False
verbose = False
very_verbose = False
# 使用的句子的地址
system_file = "example\\nlpcc_19_gpt(v3_5)_system"
gold_file = "example\\nlpcc_gold_19"
# load source sentences and gold edits
source_sentences, gold_edits = load_annotation(gold_file)
# load system hypotheses
fin = open(system_file, 'r', encoding='utf-8')
system_sentences = [line.strip() for line in fin.readlines()]
fin.close()
# 这里运行主函数
p, r, f1 = M2Score(system_sentences, source_sentences, gold_edits)
print("Precision   : %.4f" % p)
print("Recall      : %.4f" % r)
print("F_%.1f       : %.4f" % (beta, f1))
