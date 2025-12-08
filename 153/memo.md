## 今回の問題
[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)

### 概要
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

## 次に取り組む予定の問題
[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 最小値を探し出す問題、入力はソート済みだが回転あり 
- すぐに思いついたのは、隣り合う値を順番に比べて大小が逆になる場所（回転部分）を探し出す方法
- しかし、この方法だと時間計算量はO(n)になってしまう
- O(log n)で解くには2分探索を使えばよさそう
- middleとrightを比べて、もしmiddleの方が大きい場合は、回転部分はmiddleより右にあるので、探索範囲をmiddleからrightに狭める
- 逆にmiddleの方が小さい場合は、回転部分はmiddleより左にあるので、探索範囲をleftからmiddleに狭める
- これを繰り返して、探索範囲を狭めていき、最終的に最小値を返す

## Step.2: 他の人の回答、レビュー内容を参考にする

### 他の人のコードを読んで考えたこと
- https://github.com/docto-rin/leetcode/pull/25/files
- 上記リンクの実装5, 早期リターンがあり、回転がない場合には早く処理できる工夫がしてある

## Step.3: 10分以内にノーミスで3回連続解く
- step2に同じ
- 時間計算量: O(log n)
- 空間計算量: O(1)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
153. Find Minimum in Rotated Sorted Array に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
PR: https://github.com/yas-2023/leetcode_arai60/pull/22
言語: Python3

どうぞよろしくお願い致します。
