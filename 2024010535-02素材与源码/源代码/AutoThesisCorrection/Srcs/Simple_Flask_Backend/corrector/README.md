# MuCGEC集成
python版本严格要求为3.8 
1. 克隆代码https://github.com/hillzhang1999/mucgec。将整个项目放到`Simple Flask Backend`目录下。
2. 在github页面下载seq2seq_lang8+hsk\[[Link](https://drive.google.com/file/d/180CXiW7pDz0wcbeTgszVoBrvzRmXzeZ9/view?usp=sharing)\]模型，然后放入`./models/seq2seq-based-CGEC/exps`目录
3. 将根目录重命名为`MuCGEC`以及将`./models/seq2seq-based-CGEC`目录重命名为`seq2seq_based_CGEC`来解决python无法导入名称含有特殊字符的路径。
4. 根据自己情况修改`./models/seq2seq_based_CGEC`目录下`main.py`和`predict.py`内的模型路径。
5. 根据`requirements_seq2seq`以及`'Simple Flask Backend'\MuCGEC\the_correction\requirements.txt`下载依赖。