"""
LCS2
Author : Donghak Park
Contact: donghark03@naver.com
"""

first = [""] + list(input())
second = [""] + list(input())

dp_table = [[""] * len(second) for _ in range(len(first))]

for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + first[i]
        else:
            if len(dp_table[i - 1][j]) >= len(dp_table[i][j - 1]):
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = dp_table[i][j - 1]

print(len(dp_table[-1][-1]))
print(dp_table[-1][-1])
