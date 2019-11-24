# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\B\B_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可

N = int(input())
A_list = [int(item) for item in input().split()]

all_sum = sum(A_list)

F_sum_list = [A_list[0]]

for j in range(1,N):
    F_sum_list.append(F_sum_list[-1] + A_list[j])

delta_list = [abs(all_sum - 2* i) for i in F_sum_list]

print(min(delta_list))
