# 141. Linked List Cycle
[問題141のURL](https://leetcode.com/problems/linked-list-cycle)
## step2にて感じたこと
- 空間計算量：O(1)  の解法をすぐに思いつかなかった
- 初期に与えられている関数名がPEP8準拠でなかったので、少し違和感を覚えたのですが、過剰反応でしょうか。関数名にキャメルケースは、leetcodeに採用されるくらいなので、それなりに一般的？

## step3にて感じたこと
- 他の方の解法へのOdaさんの指摘を踏まえて、ローカル変数にcurrentを使うことの違和感を訂正
  - currentはcurrent_user, current_context, current_settingsのようなアプリケーション全体で共有される設定、状態に用いることが多いと理解 

## leetcodeの制約？
- 別解法として、ListNodeの構造を拡張し、visitedフラグを付けることを検討した。しかし、leetcodeの環境では、独自に定義したListNodeのクラスを参照できない（別クラスとしてVisitedListNodeを定義し、それを参照するようにしたのだが）ようであった。しかしながら、空間計算量も減らず、この問題専用の構造となってしまうため、動作したとしてもbad ideaだと考えている。
- どうやら、初期に与えられているクラス名、関数名を変更するとRUNが正常に通らないようであった。

## 次に取り組む予定の問題
[問題142のURL](https://leetcode.com/problems/linked-list-cycle-ii)