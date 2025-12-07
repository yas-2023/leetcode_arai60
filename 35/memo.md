# LeetCode 35

## 今回の問題

[35. Search Insert Position](https://leetcode.com/problems/search-insert-position)

### 概要

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

## 次に取り組む予定の問題

[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

ソートされた値の配列の中に、ある値が含まれているかを探索する問題
値が含まれているならそのindex, 含まれていないなら値が含まれていた場合のindexを返す
時間計算量O(log n)

### 何を考えて解いていたか

- 時間計算量がO(log n)なので二分探索を使うのだろうと思われる
- まずは、自然言語で考える
- 黒板に数字が小さい順に並んでいる。
- その数字の上にはindexが書かれている
- firstとlastのindexを2で割った商のindexの値と比べる
- 対象の値がindexの値以上なら、探索区間をこのindex ～ last
- 対象の値がindexの値未満なら、探索区間をfirst ～ このindex
- この操作をfirstとlastのindexの差が1以下になるまで繰り返す
- 対象の値を含む場合はfirstとlastのいずれかと一致する
- 対象の値を含まない場合はlastのindexを返せばよいはずである

### 正解してから気づいたこと

- 当初、対象の値がlast_indexより後ろになるケースを考慮し忘れていた

## Step.2: 他の人の回答、レビュー内容を参考にする

### 他の人のコードを読んで考えたこと

- https://github.com/nanae772/leetcode-arai60/pull/40/commits/7033cd64f90e5d4681a7e9d5d5c20dc46484e33a
    - コードを書いた人の意図がよくわかる書き方をされており、学びになった
    - 開区間、半開区間の解法を記載
    - ※区間についての補足：
        - 閉区間: [left, right]
            - 両端を 含む。
        - 半開区間: [left, right)
            - left は含む、right は 含まない。
        - 開区間: (left, right)
            - 両端を 含まない

- https://github.com/Mike0121/LeetCode/pull/43/commits/f8718bb0d01f743db55a483114e3d9c101cf35ad
    - 解法の小田さんの言語化がわかりやすかった
    - 一番最後の解法、閉区間のコードについて結果的に問題のない動作をするのはわかるが、直感的な理解の難しいコードがあり、step2_confusing.pyに記載した。
    - 複数の方がこのような書かれ方をしていたので、何らかの見方をすれば自然に理解できるのかもしれないが私にはわからなかった。

## Step.3: 10分以内にノーミスで3回連続解く

step2 に同じ

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用

お世話になっております。
35. Search Insert Position に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/search-insert-position/
PR: https://github.com/yas-2023/leetcode_arai60/pull/21
言語: Python3

どうぞよろしくお願い致します。
