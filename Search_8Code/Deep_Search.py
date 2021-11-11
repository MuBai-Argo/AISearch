class Border():
    """
    九宫格棋盘，包含控制0位置移动的方法
    """
    def __init__(self):
        # step 表示行进的方向变化
        self.step = []
        # path 表示经过的路径和方向，元素由列表[位置, 方向]
        # 方向 0, 1, 2, 3 表示右、下、左、上
        self.path = []
        # paths 存储不同深度经过的路径，不存储当前层
        self.paths = []
        # 表盘
        self.border = [1, 2, 3, 7, 4, 0, 6, 8, 5]
        # self.border = [2,8,3,1,6,4,7,0,5]
        # 最终表盘
        self.final_boder = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        # 初始化path: path[0]为[最初0所在的位置, 0]
        self.path.append([self.border.index(0), 0])
        # self.paths.append([self.border.index(0)])

    def canbeSolved(self):
        """
        当前八数码问题是否能够被解决
        :return:
        """
        odd = 0
        for i in range(len(self.border)):
            if self.border[i] != 0:
                for j in self.border[:i]:
                    if j > self.border[i]:
                        odd += 1
        if odd % 2 == 1:
            print(odd)
            print("可解")
            return True
        else:
            print(odd)
            print("不可解")
            return False

    def show_border(self):
        print(self.border[:3])
        print(self.border[3:6])
        print(self.border[6:9])

    def if_complete(self):
        if self.border == self.final_boder:
            print("找到路径")
            print(self.path[:-1])
            print(f"一共需要走{len(self.path[:-1]) - 1}步")
            return True
        else:
            return False

    def turn_right(self):
        """
        0与右边的数字进行交换
        :return:
        """
        # 首先检测是否处于右边缘，若处于右边缘则直接返回
        if (self.border.index(0) in [2, 5, 8]):
            print("处于右边缘 准备向下转")
            self.path[-1][1] += 1
            # 转向失败，当前结点转向   若转向后为4说明不可已经进入死路，直接回退
            return False
        # 假如不处于右边缘，则可以右转
        print("向右转")
        zero_position = self.border.index(0)
        right = self.border[zero_position + 1]
        temp = right
        self.border[zero_position + 1] = self.border[zero_position]
        self.border[zero_position] = temp
        # 将当前前进操作加入step
        self.step.append("turn right")
        # 将当前层的path加入到历史paths
        self.paths.append([i[0] for i in self.path.copy()])
        # 将当前位置加入路径队列path
        self.path.append([self.border.index(0), 0])
        # 前进成功，进入下一层
        return True

    def turn_down(self):
        """
        0与下边的数字进行交换
        :return:
        """
        # 首先检测是否处于下边缘，若处于下边缘则直接返回
        if (self.border.index(0) in [6, 7, 8]):
            print("处于下边缘 准备向左转")
            self.path[-1][1] += 1
            # 转向失败，当前结点转向   若转向后为4说明不可已经进入死路，直接回退
            return False
        # 假如不处于下边缘，则可以下转
        print("向下转")
        zero_position = self.border.index(0)
        down = self.border[zero_position + 3]
        temp = down
        self.border[zero_position + 3] = self.border[zero_position]
        self.border[zero_position] = temp
        # 将当前前进操作加入step
        self.step.append("turn down")
        # 将当前层的path加入到历史paths
        self.paths.append([i[0] for i in self.path.copy()])
        # 将当前位置加入路径队列path
        self.path.append([self.border.index(0), 0])
        # 前进成功，进入下一层
        return True

    def turn_left(self):
        """
        0与左边的数字进行交换
        :return:
        """
        # 首先检测是否处于左边缘，若处于左边缘则转向直接返回
        if (self.border.index(0) in [0, 3, 6]):
            print("处于左边缘 准备向上转")
            self.path[-1][1] += 1
            # 转向失败，当前结点转向   若转向后为4说明不可已经进入死路，直接回退
            return False
        # 假如不处于左边缘，则可以左转
        print("向左转")
        zero_position = self.border.index(0)
        left = self.border[zero_position - 1]
        temp = left
        self.border[zero_position - 1] = self.border[zero_position]
        self.border[zero_position] = temp
        # 将当前前进操作加入step
        self.step.append("turn left")
        # 将当前层的path加入到历史paths
        self.paths.append([i[0] for i in self.path.copy()])
        # 将当前位置加入路径队列path
        self.path.append([self.border.index(0), 0])
        # 前进成功，进入下一层
        return True

    def turn_up(self):
        """
        0与上边的数字进行交换
        :return:
        """
        # 首先检测是否处于上边缘，若处于上边缘则转向直接返回
        if (self.border.index(0) in [0, 1, 2]):
            print("处于上边缘 陷入死路，需要回退")
            self.path[-1][1] += 1
            # 转向失败，当前结点转向   若转向后为4说明不可已经进入死路，直接回退
            return False
        # 假如不处于上边缘，则可以上转
        print("向上转")
        zero_position = self.border.index(0)
        up = self.border[zero_position - 3]
        temp = up
        self.border[zero_position - 3] = self.border[zero_position]
        self.border[zero_position] = temp
        # 将当前前进操作加入step
        self.step.append("turn up")
        # 将当前层的path加入到历史paths
        self.paths.append([i[0] for i in self.path.copy()])
        # 将当前位置加入路径队列path
        self.path.append([self.border.index(0), 0])
        # 前进成功，进入下一层
        return True

    # 撤回函数
    def turn_right_for_shift(self):
        """
        0与右边的数字进行交换
        :return:
        """
        print("向右撤回")
        zero_position = self.border.index(0)
        right = self.border[zero_position + 1]
        temp = right
        self.border[zero_position + 1] = self.border[zero_position]
        self.border[zero_position] = temp

    def turn_down_for_shift(self):
        """
        0与下边的数字进行交换
        :return:
        """
        print("向下撤回")
        zero_position = self.border.index(0)
        down = self.border[zero_position + 3]
        temp = down
        self.border[zero_position + 3] = self.border[zero_position]
        self.border[zero_position] = temp

    def turn_left_for_shift(self):
        """
        0与左边的数字进行交换
        :return:
        """
        print("向左撤回")
        zero_position = self.border.index(0)
        left = self.border[zero_position - 1]
        temp = left
        self.border[zero_position - 1] = self.border[zero_position]
        self.border[zero_position] = temp

    def turn_up_for_shift(self):
        """
        0与上边的数字进行交换
        :return:
        """
        print("向上撤回")
        zero_position = self.border.index(0)
        up = self.border[zero_position - 3]
        temp = up
        self.border[zero_position - 3] = self.border[zero_position]
        self.border[zero_position] = temp

    def shift(self):
        """
        当没有方向可用或者达到最大深度时，回撤
        回撤之前先将当前深度的路径存入到paths中，并在回撤后的结点的path[-1][1] += 1
        :return:
        """
        print("执行撤回操作")
        # 先存入当前路径
        self.paths.append([i[0] for i in self.path.copy()])
        # 检查上一步操作，向反方向撤回
        step = self.step[-1]
        if step == "turn right":
            self.turn_left_for_shift()
        elif step == "turn down":
            self.turn_up_for_shift()
        elif step == "turn left":
            self.turn_right_for_shift()
        elif step == "turn up":
            self.turn_down_for_shift()
        # 从step中撤回上一步操作
        self.step.pop()
        # 从路径中撤回上一步走向，并使上一步操作转向
        self.path.pop()
        self.path[-1][1] += 1

if __name__ == "__main__":
    border = Border()
    if border.canbeSolved():
        while (True):
            # 检测是否达到最终结果
            print(border.border[:3])
            print(border.border[3:6])
            print(border.border[6:9])
            if border.if_complete():
                print("搜索已完成")
                break
            # 进入深度优先搜索 len(border.path[-1]) + 1代表当前深度
            deep = len(border.path)
            way = border.path[-1][1]  # way表示当前方向
            if deep <= 5:
                if way == 0:
                    border.turn_right()
                elif way == 1:
                    border.turn_down()
                elif way == 2:
                    border.turn_left()
                elif way == 3:
                    border.turn_up()
                elif way == 4:
                    # 记住当前路径，并撤回一步
                    border.shift()
            else:
                # 到达最大深度5， 进行撤回操作
                border.shift()


