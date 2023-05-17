'''
    部分集合和問題を動的計画法で解いたプログラム
'''

import time


def subset_sum(nums, W):
    # 時間計測開始
    time_sta = time.time()

    n = len(nums)
    # DPテーブルの初期化
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max (dp[i - 1][j], nums[i-1] + dp[i - 1][j - nums[i - 1]])


    # 時間計測終了
    time_end = time.time()

    # 解を表示させる
    max_weight = dp[n][W]
    max_subsets = []
    generate_subsets(dp, n, W, nums, [], max_subsets)


    # 経過時間（秒）
    tim = time_end- time_sta
    print("計測時間")
    print(tim)

    print("最大の重みの総和:", max_weight)
    print("最大となる品物の集合:")
    for subset in max_subsets:
        subset = [x for x in subset]
        subset.sort()
        print(subset)

    return max_subsets


# 解を表示させるための関数
def generate_subsets(dp, i, j, weights, current_subset, max_subsets):
    if i == 0 or j == 0:
        if dp[i][j] == 0:
            max_subsets.append(list(current_subset))
        return

    if dp[i][j] == dp[i - 1][j]:
        generate_subsets(dp, i - 1, j, weights, current_subset, max_subsets)

    if weights[i - 1] <= j and dp[i][j] == weights[i - 1] + dp[i - 1][j - weights[i - 1]]:
        current_subset.append(i - 1)
        generate_subsets(dp, i - 1, j - weights[i - 1], weights, current_subset, max_subsets)
        current_subset.pop()

    if dp[i][j] != dp[i - 1][j] and dp[i][j] != weights[i - 1] + dp[i - 1][j - weights[i - 1]]:
        generate_subsets(dp, i - 1, j, weights, current_subset, max_subsets)

# # テスト用例
# weights = [3, 1, 5, 9, 12, 4]
# W = 8
# subset_sum(weights, W)


# 実験1
weights = [1, 2, 3, 5, 7, 8, 10, 13, 15, 16]
W = 15
subset_sum(weights, W)

# 実験2
weights = [1, 2, 3, 5, 7, 8, 10, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
W = 15
subset_sum(weights, W)

# 実験3
weights = [1, 2, 3, 5, 7, 8, 10, 13, 15, 16]
W = 30
subset_sum(weights, W)