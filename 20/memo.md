## 今回の問題
[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

### 概要
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

## 次に取り組む予定の問題
[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）
### 目的
- 方法を思いつく

### 方法
- 5分考えてわからなかったら答えをみる
- 答えを見て理解したと思ったら全部消して答えを隠して書く
- 5分筆が止まったらもう一回みて全部消す
- 正解したら終わり

#### 何がわからなかったか
-

#### 何を考えて解いていたか
- 離れた括弧をどう扱うか
- 連続した括弧を1つずつ消していけば、離れた括弧を扱う必要はなさそう
- 連続した括弧を消していき、長さがゼロになればvalid,そうでなければinvalid

#### 想定ユースケース
-

#### 正解してから気づいたこと
- replace関数を使ってよかったのか？

### 方針: 
- 

### 実装: 
- 

## Step.2: 他の人の回答、レビュー内容を参考にする
### 目的
- 自然な書き方を考えて整理する

### 方法
- Step1のコードを読みやすくしてみる
- 他の人のコードを2つは読んでみること
- 正解したら終わり

#### 以下をメモに残すこと
- 講師陣はどのようなコメントを残すだろうか？
- 他の人のコードを読んで考えたこと
- 改善する時にかんがえたこと

### 講師陣はどのようなコメントを残すだろうか？
-
### 他の人のコードを読んで考えたこと
- stackを使った解法が問題の意図には沿っているような気がした
    - odaさんは、この問題からプッシュダウンオートマトンという単語を連想するらしい。カッコの対応付けは、スタックが一つあるようなオートマトンで書ける
- 再帰下降構文解析を使った解法があるらしい
    - 再帰下降構文解析を使った解法をEBNF記法で表現して整理しよう
### 他の想定ユースケース
-
### 改善する時にかんがえたこと

### 解法の種類(step1の解法を除く)
- 1. stackを使った解法
    - 
- 2. 再帰下降構文解析を使った解法
    - Group = { "(" {Group} ")" | "{" {Group} "}" | "[" {Group} "]" } 

## Step.3: 10分以内にノーミスで3回連続解く
### 目的
- 覚えられないのは、なんか素直じゃないはずなので、そこを探し、ゴールに到達する

### 方法
- 時間を測りながらもう一度解く
- 10分以内に一度もエラーを吐かず正解
- これを3回連続でできたら終わり
- レビューを受ける
- 作れないデータ構造があった場合は別途自作すること

### 計算量の見積もり
- N : len(s)
- 時間計算量: O(N)
- 空間計算量: O(N) ※厳密にはブラケットの辞書のサイズも含まれるがsより十分小さいとして無視


## Step.4: レビューをもとにコードを修正する

## その他

## 感想
- CSZAPで小西さんに教えていただいたEBNF、当初はどんなときに使うのかわからなかったが、実際に構文解析の課題に触れる中でそのありがたさを実感しました。

## discord送信用
お世話になっております。
20. Valid Parentheses に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/valid-parentheses/
PR: https://github.com/yas-2023/leetcode_arai60/pull/6
言語: Python3

どうぞよろしくお願い致します。
