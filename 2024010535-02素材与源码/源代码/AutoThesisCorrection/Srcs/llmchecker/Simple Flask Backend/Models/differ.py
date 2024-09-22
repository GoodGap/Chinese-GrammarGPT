def diff(a, b):
    """
    比较两个字符串的差异，输出需要变换的操作序列
    :param a: 字符串a
    :param b: 字符串b
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    # 记录操作序列
    res = []
    """
    Operation:
    0, not change
    1. add
    2. delete
    3. modify
    """
    i, j = m, n
    while i != 0 or j != 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1]:
            res.append([0, ""])
            i -= 1
            j -= 1
        else:
            if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                res.append([2, a[i - 1]])
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                res.append([1, b[j - 1]])
                j -= 1
            else:
                res.append([3, b[j - 1]])
                i -= 1
                j -= 1
    res.reverse()
    return res


if __name__ == "__main__":
    a = "I ad a boy"
    b = "I dont am a boy"
    print(diff(a, b))
