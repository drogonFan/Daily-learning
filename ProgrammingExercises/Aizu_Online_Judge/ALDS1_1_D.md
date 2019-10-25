# Maximum Profit

Topic link: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D

You can obtain profits from foreign exchange margin transactions. For example, if you buy 1000 dollar at a rate of 100 yen per dollar, and sell them at a rate of 108 yen per dollar, you can obtain (108 - 100) × 1000 = 8000 yen.

Write a program which reads values of a currency Rt at a certain time t (t=0,1,2,...n−1), and reports the maximum value of Rj−Ri where j>i .

Input
>The first line contains an integer n. In the following n lines, $R_t$ (t=0,1,2,...n−1) are given in order.

Output
>Print the maximum value in a line.

Constraints
>$2≤n≤200,000$
>$1≤R_t≤109$

Solution:

```python
if __name__ == '__main__':
    # 最大利益问题
    n = int(input())
    prices = []
    # get price
    for i in range(n):
        prices.append(int(input()))
    print(prices)
    maxp = prices[1] - prices[0]
    minp = prices[0]
    for i in range(1, n):
        maxp = max(maxp, prices[i] - minp)
        minp = min(minp, prices[i])
    print(maxp)
```