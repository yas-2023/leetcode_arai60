## 今回の問題
[703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream)

### 概要
Design a class to find the kth largest element in a stream of integers.

## 次に取り組む予定の問題
[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 所与のk個をキューに入れる
- 新しい値がキューの最小値より大きい場合は最小値を捨てて新しい値をキューに入れる


#### 正解してから気づいたこと
- 初期化時に与えられるkとリストの長さが異なる場合の処置が必要
- add関数において与えられるリスト長がkより小さい場合の処置が必要

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- heapを使う解法が一般的らしい
- bisectを使った解法もあるらしい

### 解法の種類(step1の解法を除く)
- 1.heapqを使う
    - 時間計算量 O(nlogk)
- 2.bisectを使う
    - 先頭削除時は全要素が1つずつ左にシフトするため、時間計算量が不利 O(k)

## Step.3: 10分以内にノーミスで3回連続解く
今回は、時間計算量に優れたheapqを使った解法とする

### 計算量の見積もり
- 時間計算量_初期化時: O(nlogk)
- 時間計算量_追加時: O(logk)
- 空間計算量: O(k)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
703. Kth Largest Element in a Stream に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/kth-largest-element-in-a-stream/
PR: https://github.com/yas-2023/leetcode_arai60/pull/8
言語: Python3

どうぞよろしくお願い致します。
