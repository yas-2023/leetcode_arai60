## 今回の問題
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

### 概要
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## 次に取り組む予定の問題
[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）
- 方針1: 各桁をまとめてから足し合わせる
    - 各桁ごとに値が格納されたリストを単一のintに戻してから足し合わせ、再びリストに戻すことを考える 
    - 桁数が多いと空間計算量の点で懸念あり
    - 所与の条件から最大100桁同士の足し算になるが、pythonならint型でそのまま扱えそう（任意精度整数）
    - 10^100なので、他の言語ではintやlong longでは入れられず、整数に戻さず各桁を足し合わせる方針が必須と思われる
    - 例えばc/c++ の unsigned long long int の最大値は2^64 -1 なので、10^20程度までしか扱えない
    - 問題の趣旨としては、各桁を足し合わせて解くべきであろう。今回は練習のためこちらの方針1でも実装してみる。繰り上がり処理が不要で、こちらの方が実装上のバグでは悩まされにくいと思われる。
    - leetcode上では実行するとMemoly Limit Exceededとなる

- 方針2: 対応する各桁同士を足し合わせる
    - 1桁ずつ足し合わせ、繰り上がりを次の桁に渡す方針で行く
    - 所与の２つのリストのうち、どちらかの桁が少ない場合が考えられるがその場合は０を足すようにしよう
    - ループで回し、どちらもnextがNoneだったら処理を終わりとする

## Step.2: 他の人の回答、レビュー内容を参考にする
- 解法の種類(step1の解法を除く)
    - 1.再帰(recursion)
        - ループではなく、再帰を使った方法
        - 当初思いつかなかったが、各桁での処理は同じで問題なく実装できそう
    - 2.loop + stack
        - ループを使った方法でstep1と似ているが、stackを使いリンクのつなぎ直しをしている
        - 厳密にはpopする際に先入れ後出しになっていない（popではなくpopleftを使っている）のでstackとは呼べないかもしれない このケースでは、stackではなく、FIFOと呼ぶのが正しいでしょうか？
        - リンクのつなぎ直しのために余分にループをまわす必要があること、stack用のメモリ空間が必要なことから時間計算量、空間計算量の点ではstep1の解法の方が筋が良さそうであるが、練習のためこちらも実装する

## Step.3: 10分以内にノーミスで3回連続解く
- step1の解法の書き方を改善した


## Step.4: レビューをもとにコードを修正する

## その他
- エディタ（vscode, windsurf）でpep8の適用
- 現状のsetting.jsonの内容
```
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.lintOnSave": true,
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "flake8.importStrategy": "fromEnvironment",
  "flake8.args": []
}
```
## discord送信用
お世話になっております。
2. Add Two Numbers に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/add-two-numbers/
PR: https://github.com/yas-2023/leetcode_arai60/pull/5
言語: Python3

どうぞよろしくお願い致します。