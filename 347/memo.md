## 今回の問題
[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

### 概要
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## 次に取り組む予定の問題
[373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 辞書で頻度をカウントする方法が真っ先に思いついた
    - 時間計算量：O(n + m log m)　 辞書作成にn, ソート(TimSort)にmlogm
    - 空間計算量：O(m)
    - mはユニーク数

#### 正解してから気づいたこと
- pythonのsortはTimSortではなくpowersortらしい
- returnがany orderで良いので、もっと良い手があるはず

## Step.2: 他の人の回答、レビュー内容を参考にする

### 解法の種類(step1の解法を除く)
- 1.辞書で頻度をカウントして、heapqでtopkを抽出
    - 時間計算量：O(n + m log k)
    - 空間計算量：O(m)
- 2.Bucket sort
    - 時間計算量：O(n)
    - 空間計算量：O(n)
- 3.Quick select
    - 時間計算量 平均：O(m)
    - 時間計算量 最悪：O(m^2)
    - 空間計算量：O(m)

## Step.3: 10分以内にノーミスで3回連続解く
- Bucket sort

### 計算量の見積もり
- Bucket sort
    - 時間計算量：O(n)
    - 空間計算量：O(n)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
347. Top K Frequent Elements に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/top-k-frequent-elements/
PR: https://github.com/yas-2023/leetcode_arai60/pull/9
言語: Python3

どうぞよろしくお願い致します。
