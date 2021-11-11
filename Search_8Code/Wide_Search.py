class Border():
    """
    九宫格棋盘，包含控制0位置移动的方法
    """

    def __init__(self):
        # 初始表盘
        # self.border = [1, 2, 3, 7, 4, 0, 6, 8, 5]
        # self.border = [2, 8, 3, 1, 6, 4, 7, 0, 5]
        self.border = [0, 2, 3,
                       1, 8, 4,
                       7, 6, 5]
        # 最终表盘
        self.final_border = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        # path 当前路径 + 当前格局 初始path: [[7], [2, 8, 3, 1, 6, 4, 7, 0, 5]]
        self.path = [[self.border.index(0)], self.border.copy()]
        # paths 存储已遍历过路径并且存储在这一步时的border格局 初始paths [[[7], [2, 8, 3, 1, 6, 4, 7, 0, 5]]]
        self.paths = [[[self.border.index(0)], self.border.copy()]]
        self.temp_paths = []    # 暂时存储paths信息，在每次深度结算时更新，用于存储某一层的路径

    def if__complete(self):
        """
        用于检测是否查找成功
        :return:
        """
        border = self.path[1].copy()
        if border == self.final_border:
            print("查找成功")
            print()
            show_border(border)
            print()
            print(f"搜索路径为{self.path[0].copy()}, 一共{len(self.path[0].copy()) - 1}个步骤")
            return True
        else:
            print()
            show_border(border)
            print()
            return False

    def turn_right(self):
        """
        0与右边换位
        :return:
        """
        # 首先判断是否处于边缘
        # 获取当前的路径和格局
        path = self.path[0].copy()
        border = self.path[1].copy()
        if path[-1] in [2, 5, 8]:
            print("处于右边缘")
            return False
        # 若不处于边缘，则向右移动
        zero_Position = border.index(0)
        right = border[zero_Position + 1]
        border[zero_Position + 1] = border[zero_Position]
        border[zero_Position] = right
        # 交换后记录该路径存入paths中，将self.path依然保持当前循环的值
        path.append(border.index(0))
        if [path, border] not in self.paths:
            self.temp_paths.append([path, border])
        # print(self.path)
        print(f"path = {self.path}")
        print(f"paths = {self.temp_paths}")

    def turn_down(self):
        """
        0与下边换位
        :return:
        """
        # 首先判断是否处于边缘
        # 获取当前的路径和格局
        path = self.path[0].copy()
        border = self.path[1].copy()
        if path[-1] in [6, 7, 8]:
            print("处于下边缘")
            return False
        # 若不处于边缘，则向下移动
        zero_Position = border.index(0)
        down = border[zero_Position + 3]
        border[zero_Position + 3] = border[zero_Position]
        border[zero_Position] = down
        # 交换后记录该路径存入paths中，将self.path依然保持当前循环的值
        path.append(border.index(0))
        if [path, border] not in self.paths:
            self.temp_paths.append([path, border])
        # print(self.path)
        print(f"path = {self.path}")
        print(f"paths = {self.temp_paths}")

    def turn_left(self):
        """
        0与左边换位
        :return:
        """
        # 首先判断是否处于边缘
        # 获取当前的路径和格局
        path = self.path[0].copy()
        border = self.path[1].copy()
        if path[-1] in [0, 3, 6]:
            print("处于左边缘")
            return False
        # 若不处于边缘，则向左移动
        zero_Position = border.index(0)
        left = border[zero_Position - 1]
        border[zero_Position - 1] = border[zero_Position]
        border[zero_Position] = left
        # 交换后记录该路径存入paths中，将self.path依然保持当前循环的值
        path.append(border.index(0))
        if [path, border] not in self.paths:
            self.temp_paths.append([path, border])
        # print(self.path)
        print(f"path = {self.path}")
        print(f"paths = {self.temp_paths}")

    def turn_up(self):
        """
        0与上边换位
        :return:
        """
        # 首先判断是否处于边缘
        # 获取当前的路径和格局
        path = self.path[0].copy()
        border = self.path[1].copy()
        if path[-1] in [0, 1, 2]:
            print("处于上边缘")
            return False
        # 若不处于边缘，则向上移动
        zero_Position = border.index(0)
        up = border[zero_Position -3]
        border[zero_Position -3] = border[zero_Position]
        border[zero_Position] = up
        # 交换后记录该路径存入paths中，将self.path依然保持当前循环的值
        path.append(border.index(0))
        if [path, border] not in self.paths:
            self.temp_paths.append([path, border])
        # print(self.path)
        print(f"path = {self.path}")
        print(f"paths = {self.temp_paths}")

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

def show_border(border):
    print(border[:3])
    print(border[3:6])
    print(border[6:9])

border = Border()
deep = 1
stop = False
if border.canbeSolved():
    while(deep <= 6 and not stop):
        for path in border.paths:
            print(len(path[0]))
            border.path = path
            if len(path[0]) == deep:
                if border.if__complete():
                    stop = True
                    break
                border.turn_right()
                border.turn_down()
                border.turn_left()
                border.turn_up()
            print(len(border.paths))
        border.paths.extend(border.temp_paths.copy())
        border.temp_paths.clear()
        deep += 1
