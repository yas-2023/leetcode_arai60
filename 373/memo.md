## 今回の問題
[373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)

### 概要
You may assume nums1 and nums2 are sorted in non-decreasing order.

## 次に取り組む予定の問題
[1. Two Sum](https://leetcode.com/problems/two-sum)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 総当りだと、時間計算量がO(n1*n2 log n1n2)なので、これはNG
- 昇順にソート済みであることを考えると、最小はnum1[0],num2[0], 
- 次に小さいのはnum1[0],num2[1] or num1[1],num1[0]のいずれか
- 2次元の表だと考えて、最初の列をheapに入れれば、後は行方向のみ考えれば良くなる
- 時間計算量O(k log k)、空間計算量 O(k)
## Step.2: 他の人の回答、レビュー内容を参考にする
### 解法の種類(step1の解法を除く)
- 1. Grid BFS
    - step1 の解法より、やや空間計算量が不利(visitedの保持が必要なため)
    - 時間計算量O(k log k)、空間計算量 O(2k) ※step1との違いを示すために2kとしているが、通常2の部分は無視され O(k)  
- 2. しきい値（sum <= T）を二分探索で求める 
    - 省メモリ
    - 時間計算量O((m + n) log R + k)、空間計算量 O(1)
    - Rは和の値域

## Step.3: 10分以内にノーミスで3回連続解く
step1の解法
### 計算量の見積もり
- 時間計算量: O(k log k)
- 空間計算量: O(k)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
373. Find K Pairs with Smallest Sums に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
PR: https://github.com/yas-2023/leetcode_arai60/pull/10
言語: Python3

どうぞよろしくお願い致します。
