# import numpy
# from itertools import permutations
# person = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
# index = [1, 2, 3, 4]
# person_index = []
# sum = []
# for i in permutations(index):
#     person_index.append(list(i))
# for i in person_index:
#     temp = 0
#     temp += person[0][i[0] - 1]
#     temp += person[1][i[1] - 1]
#     temp += person[2][i[2] - 1]
#     temp += person[3][i[3] - 1]
#     sum.append(temp)
#     print(f"方案{i}成本为{temp}")
# sum = numpy.array(sum)
# number = numpy.argmin(sum)
# print(f"最佳方案为：{person_index[number]}，成本为{sum[number]}")