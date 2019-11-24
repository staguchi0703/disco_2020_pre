# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\A\A_input.txt', 'r', encoding="utf-8")
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
x, y = [int(item) for item in input().split()]

res = 0

if x == 1:
    res += 300000
elif x == 2:
    res += 200000
elif x == 3:
    res += 100000

if y == 1:
    res += 300000
elif y == 2:
    res += 200000
elif y == 3:
    res += 100000

if x == 1 and y == 1:
    res += 400000

print(res)