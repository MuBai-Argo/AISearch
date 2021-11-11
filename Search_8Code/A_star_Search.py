class A_star_Search():
    """
    利用A*算法来获取八数码最短路径
    """

    def __init__(self):
        self.border = [1, 2, 3, 7, 0, 4, 6, 8, 5]
        self.final_border = [1, 2, 3, 8, 0, 5, 6, 7, 4]
        # 八数码问题中的节点就是0向不同方向移动的行为，并为每个行为遍历赋一个f(n)值
        self.step_open = []  # 存储估价后的结点
        self.step_close = []  # 逆序存储路径
        # 估价方式
        # h(n):
        # 1. 经此方向行动后border与final_border的非对应位置数
        # 2. 经此方向行动后border中每个数字离最终位置的距离
        # g(n):
        # 已移动的步数(可用循环的次数来获取)
        # 通过向不同方向前进来向step_Open中引入新的结点    [0 : right, 1 : down, 2 : left, 3 : up]
        # 结点 将border的状态作为结点来进行保存，故需要path， 元素为[当前0的位置， 当前border， f(n)]
        # 计算初始f(0)
        f0 = 0
        for i in range(len(self.border)):
            f0 += (self.border[i] == self.final_border[i])
        self.path = []  # path从paths中获取内容
        # paths用于存储当前拓展的路径 paths包含的存储内容应当为：[border, f(n)]
        self.paths = [[self.border.copy(), f0]]
        self.step_open.append([self.border.copy(), f0])
        self.temp_paths = []
        # borders用于存储当前已经走过的状态，避免二次进入该状态
        self.borders = []
        # parents用于在转向时确定亲子关系
        self.parents = []
        # 路径表
        self.step = []

    def h_1(self, border: list):
        """
        状态n的估价函数
        经此方向行动后border与final_border的非对应位置数
        :param self:
        :return:
        """
        show_border(border)
        h = 0
        for i in range(len(border)):
            h += (border[i] == self.final_border[i])
        return h

    def turn_right(self):
        path = self.path.copy()
        border = path[0].copy()
        zero_position = border.index(0)
        if zero_position in [2, 5, 8]:
            print("处于边缘")
            return False
        right = border[zero_position + 1]
        border[zero_position + 1] = border[zero_position]
        border[zero_position] = right
        if border not in self.borders:
            self.temp_paths.append([border.copy(), self.h_1(border.copy())])
            # self.step_open.append([border.copy(), self.h_1(border.copy())])
        else:
            return False
        return True

    def turn_down(self):
        path = self.path.copy()
        border = path[0].copy()
        zero_position = border.index(0)
        if zero_position in [6, 7, 8]:
            print("处于边缘")
            return False
        up = border[zero_position + 3]
        border[zero_position + 3] = border[zero_position]
        border[zero_position] = up
        if border not in self.borders:
            self.temp_paths.append([border.copy(), self.h_1(border.copy())])
            # self.step_open.append([border.copy(), self.h_1(border.copy())])
        else:
            return False
        return True

    def turn_left(self):
        path = self.path.copy()
        border = path[0].copy()
        zero_position = border.index(0)
        if zero_position in [0, 3, 6]:
            print("处于边缘")
            return False
        left = border[zero_position - 1]
        border[zero_position - 1] = border[zero_position]
        border[zero_position] = left
        if border not in self.borders:
            self.temp_paths.append([border.copy(), self.h_1(border.copy())])
            # self.step_open.append([border.copy(), self.h_1(border.copy())])
        else:
            return False
        return True

    def turn_up(self):
        path = self.path.copy()
        border = path[0].copy()
        zero_position = border.index(0)
        if zero_position in [0, 1, 2]:
            print("处于边缘")
            return False
        up = border[zero_position - 3]
        border[zero_position - 3] = border[zero_position]
        border[zero_position] = up
        if border not in self.borders:
            self.temp_paths.append([border.copy(), self.h_1(border.copy())])
            # self.step_open.append([border.copy(), self.h_1(border.copy())])
        else:
            return False
        return True


def show_border(border: list):
    print()
    print(border[:3])
    print(border[3:6])
    print(border[6:])
    print()


a_star = A_star_Search()
show_border(a_star.border)
# a_star.path = a_star.paths[0].copy()
# if a_star.turn_right():
#     for i in a_star.temp_paths:
#         i[1] += 0
#
#     a_star.paths.pop(0)
#     a_star.paths.extend(a_star.temp_paths)
deep = 0
#     a_star.temp_paths = []
#     for i in a_star.paths:
#         print(i)
circle = True
# while(circle):
#     for path in a_star.paths:
#         a_star.path = path.copy()
#         a_star.borders.append(a_star.path.copy()[0])
#         if a_star.turn_right():
#             a_star.temp_paths[-1][1] += deep
#         if a_star.turn_down():
#             a_star.temp_paths[-1][1] += deep
#         if a_star.turn_left():
#             a_star.temp_paths[-1][1] += deep
#         if a_star.turn_up():
#             a_star.temp_paths[-1][1] += deep
#         a_star.step_close.append(a_star.paths.pop(0))
#         if [1, 2, 3, 8, 0, 4, 7, 6, 5] in [i[0] for i in a_star.paths]:
#             print("搜索成功")
#             circle = False
#             break
#         a_star.paths.extend(a_star.temp_paths.copy())
#         a_star.step_open.extend(a_star.temp_paths.copy())
#         a_star.temp_paths = []
#         for i in a_star.paths:
#             print(i)

while (circle):
    a_star.paths = sorted(a_star.paths, key=lambda x: x[1])
    a_star.path = a_star.paths[0].copy()
    parent = a_star.path.copy()
    a_star.borders.append(a_star.path.copy()[0])

    a_star.step_close.append([a_star.paths.pop(0), deep])

    if a_star.turn_right():
        a_star.temp_paths[-1][1] += deep
    if a_star.turn_down():
        a_star.temp_paths[-1][1] += deep
    if a_star.turn_left():
        a_star.temp_paths[-1][1] += deep
    if a_star.turn_up():
        a_star.temp_paths[-1][1] += deep
    a_star.parents.append((parent, a_star.temp_paths.copy()))
    if [1, 2, 3, 8, 0, 4, 7, 6, 5] in [i[0] for i in a_star.paths]:
        final_step = []
        for final_path in a_star.paths:
            if final_path[0] == [1, 2, 3, 8, 0, 4, 7, 6, 5]:
                a_star.step_close.append([final_path.copy()])
                final_step = final_path.copy()
        print("搜索成功")
        # 通过亲子表来寻找搜索路径
        for step in reversed(a_star.parents):
            if final_step in step[1]:
                a_star.step.append(final_step)
                final_step = step[0]
        a_star.step.append([a_star.border, 0])
        print("搜索路径为:")
        for i in a_star.step:
            show_border(i[0])
        # for i in a_star.step_close:
        #     print(i)
        print(f"一共需要{len(a_star.step) - 1}个步骤")
        break
    a_star.paths.extend(a_star.temp_paths.copy())
    a_star.step_open.extend(a_star.temp_paths.copy())
    a_star.temp_paths = []
    for i in a_star.paths:
        print(i)
    deep += 1


