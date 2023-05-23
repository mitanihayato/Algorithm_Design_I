def dp(n, R):
    R.sort(key=lambda x: x[1])   # 終了時刻に対してRをソートする
    max_f = R[-1][1]    # Rの中で終了時刻が最大のものを取得
    DP = [[0] * (n+1)for _ in range(max_f+1)]   # DPの初期化

    # Rは0番目の要素がDPの1に対応するからj-1にすることに注意
    for i in range(1, max_f+1):
        for j in range(1, n+1):
            if i < R[j-1][1]:
                DP[i][j] = DP[i][j-1]
            else:
                DP[i][j] = max(DP[i][j-1], R[j-1][2]+DP[R[j-1][0]][j-1])
    
    # 答えの復元
    # DPには最大となる重みの和が格納されている
    # 時刻max_fにおけるj番目の要素までの中で1つ前のものと違えば，要求が追加されたことになる
    subset = []
    i = max_f
    j = n
    while i > 0 and j > 0:
        if DP[i][j] != DP[i][j-1]:
            i = R[j-1][0]
            subset.append(R[j-1])
        j = j-1

    print("最大和をとる要求の部分集合")
    for set in subset:
        print(set[0], set[1], set[2])

    print("最大和：", DP[max_f][n])



# テスト
n = 5
R = [[0, 2, 1], [1, 3, 1], [2 ,4 ,1], [3, 5, 1], [4, 6, 1]]
dp(n, R)


n = 5
R = [[0, 2, 1], [1, 3, 1], [3, 5, 1], [4, 6, 1], [2 ,4 ,1]]
dp(n, R)