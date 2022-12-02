# from itertools import permutations
#
# my_list = [1, 2, 3, 4]
# list_of_permutations = permutations(my_list)
# cnt = 0
#
# for permutations in list_of_permutations:
#     cnt = cnt + 1
#     print(permutations)
# print(cnt)


# checking the performance and how fast the permutation grow
import cProfile


def faculty(n):
    if n <= 1:
        return 1
    else:
        return faculty(n - 1) * n


def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt

cProfile.run("counter(faculty(10))")
