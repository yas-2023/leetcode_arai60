## 今回の問題
[127. Word Ladder](https://leetcode.com/problems/word-ladder)

### 概要
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

## 次に取り組む予定の問題
「全問題を通して「やりたいことを明確にする能力」が鍵だと感じます。この能力を養うには二分探索が有効」とのコメントを拝見し、順番を変更します。
[35. Search Insert Position](https://leetcode.com/problems/search-insert-position)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

### 何を考えて解いていたか
- まず問題を自然言語で考える
- 大方針として、最初のワードから次を探索する方法、最後のワードから探索する方法、最初と最後の両面から探索する方法がありあそう。今回は、シンプルに最初のワードから次々に探索する。
- 問題の前提
    - 最初のワードと最後のワードと使用可能なワードリストが定義されている
    - 一文字違いで次のワードに遷移し、最後のワードに最短で到達できるワード数を求める問題
    - 最後のワードも使用可能リストの中に含まれている必要がある
- 手順
- 前準備
    - 黒板に、最初のワードとワードリストのワードを1行に1ワードで書き出していく
    - ワードの横に、次の単語の候補となるワードをすべて書き出す
    - ワードと次のワード候補群の対応表ができる
    - この対応表を見ながら探索することとする
    - 手元のワードカウンタを１に設定する

- 探索
- 初回の探索
    - ワードカウンタをインクリメントする
    - まず、２つ目の単語の候補を調べる、
    - 対応表の最初の単語の右に書かれたワード群を候補ワード群として、黒板の右端に転記する
    - 候補ワード群の中に最後のワードがあるかを確認する
    - あれば、ワードカウンタの値を答として返す
    - なければ、候補ワード群を前回の候補ワード群として転記する

- 2回目以降の探索
    - ワードカウンタをインクリメントする
    - ３つ目の単語の候補を調べる
    - 前回の候補ワード群すべてについて、対応表を見ながら候補ワードを洗い出す（重複は除く）
    - 候補ワード群を更新する
    - 候補ワード群の中に最後のワードがあるかを確認する
    - あれば、ワードカウンタの値を答として返す
    - なければ、候補ワード群を前回の候補ワード群として転記する

- 上記を繰り返す。
    - 最短という指定があるのでワードを重複して使うことはない
    - このため、単語の遷移は最長でもワードリストのワード数回＝繰り返しの上限となる。

- 候補算出の際に、過去の候補を含めないことで探索の幅を削減することもできそうであるが、今回は深さに制約(ワードリストのワード数)があるので、処理をシンプルにするためにもこれは考慮しないこととする
- また、上記は幅優先探索をしているが、深さ優先探索をする手もありそう

#### 正解してから気づいたこと
- acceptはされるものの、非常に遅い
- 1文字違いのワードを探すのにO(N^2 * L) ※ワード数をN、文字数をLとする

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- https://github.com/docto-rin/leetcode/pull/19/commits/45fd1779e01ede9800cfd6284afe21e388ed92c3
    - 問題の捉え方：　 beginWordからendWordへの無向グラフ上での最短距離を求める問題
        - 問題を既知のパターンに当てはめて考えると、素直な実装ができそうに感じた(step1の自分のやり方は、パターンを知っている人からみたらわかりにくいかもしれない)  
    - step1 では多くの人が1文字の違いを探すのにナイーブな手法で解いていた印象
    - ボトルネックとなる探索の高速化(hash table)について 
        - 辞書でキーを1文字ワイルドカード、値を隣接ワードのlistとする
        - 辞書構築にワード数をN、文字数をLとするとO(NL)
        - 1ワードの隣接ワードの探索にO(LM)かかり、ワーストケースでワード数分の探索なのでO(LMN)
        - Mは平均隣接ノード数とする
    - 気になった点
        - 辞書の値をリストにしていたが、setにすれば時間計算量をさらに下げられる(O(LMN)　→ O(LN))のではと思った。
- 双方向BFSについては今回はスキップ(step4でやる)し、単方向BFS + Hash tableによる探索の高速化のみを実装する

## Step.3: 10分以内にノーミスで3回連続解く
単方向BFS + Hash tableによる探索の高速化を実装する
step2に同じ。

### 計算量の見積もり
- N : wordListのワード数
- L : wordListのワードの文字数
- 時間計算量: O(NL)
- 空間計算量: O(NL)


## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
127. Word Ladder に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/word-ladder/
PR: https://github.com/yas-2023/leetcode_arai60/pull/20
言語: Python3

どうぞよろしくお願い致します。

次問以降は、「全問題を通して「やりたいことを明確にする能力」が鍵だと感じます。この能力を養うには二分探索が有効」とのコメントを拝見し、順番を変更し35～を先に行う予定です。