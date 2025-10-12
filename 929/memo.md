## 今回の問題
[929. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses)

### 概要
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

## 次に取り組む予定の問題
[387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）
#### 何を考えて解いていたか
- split関数を使って@,+で区切り、正規化したメールアドレスを作成し、数を数える 
- "."についてはreplaceで除去
- 上記の手法で実装できるが、問題の意図としてはforで位置文字ずつ処理していくことが求められているように思う
- この場合は、local_name, domain_name用の配列を用意し、.を除いて、+もしくは@が現れるまで文字を追加していくことで実装できそう

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- 正規表現を用いた解法は考えていなかった。
- forを使う解法では、step1ではflagを使わず処理していたが、フラグを用いたほうが可読性が高まるかもしれない
- 入力の制約を考えて例外処理を実装している人も。実務では必要そう。


### 解法の種類(step1の解法を除く)
- 1.正規表現
- 2.forループ、フラグあり実装
## Step.3: 10分以内にノーミスで3回連続解く
- 1.正規表現
### 計算量の見積もり
- N: emails.len()
- M: average(emails[i].len()) 
- 時間計算量: O(N*M)
- 空間計算量: O(N*M)


## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
929. Unique Email Addresses に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/unique-email-addresses/
PR: https://github.com/yas-2023/leetcode_arai60/pull/14
言語: Python3

どうぞよろしくお願い致します。
