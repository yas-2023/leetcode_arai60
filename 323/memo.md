## 今回の問題
[323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph)
### NEET CODE: 
[323. Number of Connected Components in an Undirected Graph](https://neetcode.io/problems/count-connected-components)

### 概要
You are given an undirected graph with n nodes, numbered from 0 to n - 1 (inclusive). Each edge is represented as a pair of nodes that are connected by the edge.

## 次に取り組む予定の問題
[127. Word Ladder](https://leetcode.com/problems/word-ladder)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

### 何を考えて解いていたか
- UnionFindで解けそう 
- 他の方法も考えてみる。
- 無指向グラフなので,問題を次のように捉え直す(言語化の一環で)。
    - 番号のついたボールが2個セットで箱に入って１列で置かれている。
    - グループ化するための箱(グループ1~)を準備する。
    - 左から1箱目はそのままグループ1の箱に入れる。
    - ２箱目以降を見ていき、同じ番号が１つでも含まれる箱はグループの箱に入れていく。
    - 同じ番号が１つも含まれない場合は新しいグループの箱を作りそこに入れる。
    - すべての箱を処理したら、グループの箱の数を返す。
- 既存のグループの箱はsetで管理することでグループ１箱あたりはO(1)で検索可能。
- でも全体ではワーストケース(全てバラバラ)ではO(N^2)かかる。
- ひとまず、この方法とUnionFindで解く。

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- DFS, BFSを使った解法やUnionFindを使った解法が一般的のようだった。
- DFS, BFSでは、隣接ノードをvisitedを除いてたどっていくことで効率的に探索できるので、隣接ノードを管理する辞書の構築コストはかかるが、O(N)で探索できる。
- DFS, BFSは探索予定ノードを右からpopするのか左からpopするかの違いだけ。
- DFS,BFSの解法についても自然言語で書き下す
    - 番号のついたボールが2個セットで箱に入って１列で置かれている。
    - 黒板にボールの番号1~Nを書いておく。
    - 左の箱から順番にボールの番号の対応(繋がり)をみて黒板に対応表を書いていく。
    - これからいくつの独立した繋がりができるかを数えていく。
    - これを数えるカウンタをインクリメントする
    - ボールの番号１番から、繋がりを書いていく
    - 繋がりに使われた番号は黒板に「処理済み」として記録しておく
    - 番号1番の繋がりが終わったら、 次の（処理済みを除く）番号の繋がりを書いていく処理へ(カウンタもインクリメント)
    - すべてのボールの番号の繋がりを書いていく
    - カウンタの値を返す
    
## Step.3: 10分以内にノーミスで3回連続解く
今回はBFSで解き直した。
### 計算量の見積もり
- N : ノードの数
- 時間計算量: O(N)
- 空間計算量: O(N)


## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
323. Number of Connected Components in an Undirected Graph に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
NEET CODE: https://neetcode.io/problems/count-connected-components
PR: https://github.com/yas-2023/leetcode_arai60/pull/6
言語: Python3

どうぞよろしくお願い致します。