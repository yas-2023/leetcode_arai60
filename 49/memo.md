## 今回の問題
[49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

### 概要
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

## 次に取り組む予定の問題
[349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 文字の頻度が同じかを見れば良さそう
- 辞書自体をキーにして、値をリストにしていく
- 時間計算量: O(nk)
- 空間計算量: O(nk)
- n:len(strs)
- k:max(len(strs[i]))

#### 正解してから気づいたこと
- 当初、辞書自体をキーにする方法がわからなかったがイミュータブルにすれば可能だった
## Step.2: 他の人の回答、レビュー内容を参考にする
### 解法の種類(step1の解法を除く)
- 1.ソート文字列をキーにする
    - 時間計算量: O(nklogk)
    - 空間計算量: O(nk)
    - ソートするため、与えられる文字列が長いほどstep1の解法より不利

## Step.3: 10分以内にノーミスで3回連続解く
実装がシンプルなstep2の解法で解く
### 計算量の見積もり
- 時間計算量: O(nklogk)
- 空間計算量: O(nk)
- n:len(strs)
- k:max(len(strs[i]))


## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
49. Group Anagrams に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/group-anagrams/
PR: https://github.com/yas-2023/leetcode_arai60/pull/12
言語: Python3

どうぞよろしくお願い致します。
