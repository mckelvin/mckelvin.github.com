#!/usr/bin/env python2
# coding: UTF-8
# 图片OCR工具 http://www.onlineocr.net/
# 大猫咪F - 最招人讨厌的星座～读图时代有爱统计 http://www.douban.com/group/topic/38559331/
# ◆.财小姐姐 :) - 中国星座人口比例（更新篇） http://www.douban.com/note/58744715/

import numpy as np
labels = ["魔羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手"]
labels = map(lambda x: '%s座'%x, labels)
X = [13563, 1487, 7264, 4472, 7457, 5299, 6793, 3734, 20179, 6162, 22393, 2968]
X = np.array(X)
base = [587719, 700267, 653845, 884644, 950893, 1000711, 946605, 684568, 574803, 644527, 1580495, 1007767]
base = np.array(base).astype(np.float)
base = base / base.mean()

print '''['星座', '考虑人口基数', '不考虑人口基数' ], '''
for l, c, c2 in zip(labels, X / base, X):
    print '''['{0}', {1}, {2} ], '''.format(l, c, c2)
