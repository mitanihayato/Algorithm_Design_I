'''
    部分集合和問題をしらみつぶし法で解いたプログラム
'''

import time


def subset_sum_exhaustive(nums, W):
    
    max_weight = 0  # 最大の重みの総和
    max_subsets = []  # 最大となる品物の集合のリスト

    # 時間計測開始
    time_sta = time.time()

    n = len(nums)

    for i in range(2 ** n):
        subset = []
        weight_sum = 0

        for j in range(n):
            if (i >> j) & 1:
                subset.append(j)
                weight_sum += nums[j]

        # 重みの総和がW以下であれば、結果に追加する
        if weight_sum <= W:
            # 最大の重みの総和と比較して、大きければ更新する
            if weight_sum >= max_weight:
                if weight_sum > max_weight:
                    max_weight = weight_sum
                    max_subsets = []
                max_subsets.append(subset)

    # 時間計測終了
    time_end = time.time()
    # 経過時間（秒）
    tim = time_end- time_sta

    print("計測時間")
    print(tim)

    print("最大の重みの総和:", max_weight)
    print("最大となる品物の集合:")
    for max_subset in max_subsets:
        print(max_subset)

    return max_subsets


# # テスト用例
# weights = [3, 4, 2, 1, 5]
# W = 19
# subset_sum_exhaustive(weights, W)

# 実験1
weights = [1, 2, 3, 5, 7, 8, 10, 13, 15, 16]
W = 15
subset_sum_exhaustive(weights, W)

# 実験2
weights = [1, 2, 3, 5, 7, 8, 10, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
W = 15
subset_sum_exhaustive(weights, W)

# 実験3
weights = [1, 2, 3, 5, 7, 8, 10, 13, 15, 16]
W = 30
subset_sum_exhaustive(weights, W)