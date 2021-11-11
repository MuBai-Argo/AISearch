# 评估函数： evluate(p) = 对角线或者行列中没有MIN的数 - 对角线或者行列中没有MAX的数
# ALPHA-BETA剪枝边生成博弈树边计算各个结点的倒推值，并且根据评估出的倒推值的范围，及时停止拓展那些无需再拓展的子节点。
# ALPHA-BETA的剪枝过程遵循深度优先搜索，

import pandas as pd
import numpy as np

class Node():

    def __init__(self):
        self.border = np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
        self.declare = "MAX"
        self.BETA = 100 # 结点的上确界
        self.ALPHA = -100   # 结点的下确界

    def evaluate(self):
        """
        效用函数
        :return: evluate(p) = 对角线或者行列中没有MIN的数 - 对角线或者行列中没有MAX的数
        """
        alpha = 0
        beta = 0
        # 横纵评估
        for i in range(0, 3):
            if 1 not in self.border[:, i]:
                beta += 1
            if 2 not in self.border[:, i]:
                alpha += 1
            if 1 not in self.border[i, : ]:
                beta += 1
            if 2 not in self.border[i, : ]:
                alpha += 1
        # 对角线评估
        diag1 = [self.border[i] for i in [0, 4, 8]]
        diag2 = [self.border[i] for i in [2, 4, 6]]
        if 1 not in diag1:
            beta += 1
        if 1 not in diag2:
            beta += 1
        if 2 not in diag1:
            alpha += 1
        if 2 not in diag2:
            alpha += 1
        return beta - alpha






class Tree():

    def __init__(self):
        self.root = Node()
