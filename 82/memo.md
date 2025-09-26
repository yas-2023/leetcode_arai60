## 今回の問題
[82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)

### 概要
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

## 次に取り組む予定の問題
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）
- 方針
    - 辞書で値の出現回数をカウントし、出現回数が1の値のみを連結リストに追加する
    - 異なる値ごとにカウントするため、空間計算量は増えるが、実装がシンプルでミスしにくいだろうと考えた
    - 時間計算量：O(n)
    - 空間計算量：O(n)

## Step.2: 他の人の回答、レビュー内容を参考にする
- 解法の種類(step1の解法を除く)
    - 1.Stack
    - 2.1重ループの解法（重複を見つけたら引き継ぐ）
    - 3.2重ループの解法（重複を発見したら帰るな）
- 1.Stack
    - 前後の値を比較し、いずれも異なるノードをpushしていくシンプルな解法
    - stack用のメモリ空間が必要なので、空間計算量は増える点はデメリット(しかし、stackするのは非重複ノードのみなのでstep1の解法よりは小さくて済む)
    - 時間計算量：O(n)
    - 空間計算量：O(n)
- 2.1重ループの解法（重複を見つけたら引き継ぐ）
    - [1,1]のような重複のみの場合は、最後のノードが消えず、最後のノードのnextをNoneにする必要がある点に注意が必要でした。
    - 時間計算量：O(n)
    - 空間計算量：O(1)
- 3.2重ループの解法（重複を発見したら帰るな）
    - 重複の有無で何を更新し、何を更新しないかを明確にするのがポイントだと思いました
    - 時間計算量：O(n)
    - 空間計算量：O(1)

## Step.3: 10分以内にノーミスで3回連続解く
2重ループ解法で解いた

## Step.4: レビューをもとにコードを修正する

## その他
- leetcodeにvimモードがあることを今さら知りました
    - settings > code editor > key binding > select Vim.

## discord送信用
お世話になっております。
82. Remove Duplicates from Sorted List II に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
PR: https://github.com/yas-2023/leetcode_arai60/pull/4
言語: Python3

どうぞよろしくお願い致します。