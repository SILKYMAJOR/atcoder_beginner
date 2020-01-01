def main():
    s = input()

    div = 13
    dp = [0] * div
    mod = 1000000007

    # ループカウンタ
    count = 0

    # 0を13で割った時のあまりを格納
    dp[0] = 1
    # print("-" * 50)
    # print("v : {:>20}  ".format(0), end="")
    # print(dp)

    for v in reversed(s):
        tmp_dp = [0] * div
        digit = 10**count

        if v == "?":
            for i in range(10):
                for k in range(div):
                    a = (i * digit + k) % div
                    tmp_dp[a] += dp[k]
                    tmp_dp[a] %= mod
        else:
            int_v = int(v)
            for k in range(div):
                a = (int_v * digit + k) % div
                tmp_dp[a] += dp[k]
                tmp_dp[a] %= mod

        count += 1
        dp = tmp_dp

        # print("v : {:>20}  ".format(s[len(s)-count:]), end="")
        # print(dp)

    print(dp[5] % mod)


if __name__ == '__main__':
    main()

