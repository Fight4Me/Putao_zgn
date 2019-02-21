# 统计每句话上下文中(5句内)频率高的句
该代码分为两个部分，第一个部分是preprocess.py用于预处理，第二个部分是CountFiveNearest.py用于处理预处理文件生成json文件。每部分代码均包含流程图，请使用draw.io打开对应文件。
处理数据放在：https://github.com/Fight4Me/putao_zgn/blob/master/%E5%85%A8%E9%83%A8%E5%AF%B9%E8%AF%9D%E6%95%B0%E6%8D%AE.rar

# stanfordNLP的NER接口使用方法

官方网址：https://nlp.stanford.edu/software/CRF-NER.shtml

pyner: https://github.com/dat/pyner

运行前需要下载官方网站上提供的stanford-ner-2018-10-16.rar里面包含了训练好的模型，同时可以使用Git Bash在windows系统中搭建服务，我将解压的文件夹放入pyner的文件夹中，然后使用bash文件在git中搭建服务，具体参考ner.sh文件。使用时请下载pyner与stanford-ner-2018-10-16.rar以及其他必须组件。
