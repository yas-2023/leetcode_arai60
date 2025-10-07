## 今回の問題
[1. Two Sum](https://leetcode.com/problems/two-sum)

### 概要
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## 次に取り組む予定の問題
[49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）
#### 何を考えて解いていたか
- 一度辞書をつくる、辞書の値は目標値との差分とする
- 非破壊でソート済みのlistをつくる
- ループで辞書のキーを小さい順に回していく、目標値と現在値の差分が、リストにあるかを逐次確認する
- 小さい順に回すのは同じ値を足し合わせるケースを一番最後にもっていきたいため（最後にしないと要素が２つあるかの確認が必要）
- 無駄の多い実装のように思うが、とりあえず解けた

#### 正解してから気づいたこと
- 同値の場合、indexの取得に工夫が必要
- sortがボトルネックで、時間計算量がO(n log n)
- 空間計算量はO(n)

## Step.2: 他の人の回答、レビュー内容を参考にする
- 辞書を使う発想に誤りは無いが、辞書を値とindexにすべきだった
### 解法の種類(step1の解法を除く)
- 1. hashを使う解法
    - 時間計算量: O(n)
    - 空間計算量: O(n)
- 2.sort + two_pointer
    - 時間計算量: O(n log n)
    - 空間計算量: O(n)
- 3.brute force（2重ループ）
    - 問題の意図とは異なるだろうが、空間計算量は最も小さい
    - 時間計算量: O(n^2)
    - 空間計算量: O(1)

## Step.3: 10分以内にノーミスで3回連続解く
### 計算量の見積もり
- 1. hashを使う解法
    - 時間計算量: O(n)
    - 空間計算量: O(n)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
1. Two Sum に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/two-sum/
PR: https://github.com/yas-2023/leetcode_arai60/pull/11
言語: Python3

どうぞよろしくお願い致します。
