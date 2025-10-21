## 今回の問題
[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k)

### 概要
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

## 次に取り組む予定の問題
[200. Number of Islands](https://leetcode.com/problems/number-of-islands)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）
#### 何を考えて解いていたか
- 連続する部分の和がkになる部分列を数えるということなので、連続する部分のみ考慮すれば良い。
- 無駄が多いかもしれないが、累積和を所与の配列をシフトさせながら計算し、kの出現回数を数える
- 時間計算量: O(N^2)となり、遅い。もっと賢い方法ありそう。
- この解法は動くが、Time Limit Exceededとなる
- sliding windowで和がkを超えたら打ち切る事も考えたが、負の値も含まれるため、bad ideaだった。

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- 下記のodaさんの問題の捉え直しが参考になりました。
    - ちょっと問題を変えて、和が K となる区間を列挙する問題にしてみたらどうでしょうか。もうちょっと言い換えると、「鉄道があって、各駅間ごとの標高差が与えられます。標高差が ちょうど K であるようなすべての駅の組み合わせを列挙してください。」ということです。最後に len を取れば、元の問題の答えになるはずなので、ジャッジも使えるでしょう。これを累積和を使って出してください。
- https://github.com/docto-rin/leetcode/pull/16/commits/84080fc16480525f97ecf5bb8c8681f20cbcbdfe
    - 下記の考察が勉強になりました。 
    - ただし、下記抜粋の最後の行にあるhashtableへの挿入に関しては、defaultdictを使う副作用なので、通常のdictなら挿入は生じない。このため、通常のdictを使う際には、分岐がなくても、時間計算量や空間計算量で不利になることは無いように思いました。
        - if current_sum - k in sum_frequency:について、inよりも+, -が先に評価されるとのことで、冗長なカッコを外した。
        - https://docs.python.org/ja/3.13/reference/expressions.html#operator-precedence
        - if current_sum - k in sum_frequency:の分岐を無くしても動くが、分岐がある方が空間的に小さい（自明）のと、時間も高速。
        - current_sum - kが未出現だったとしても都度hashtableへの挿入が明示的に生じるため、衝突の可能性やhashtableの動的拡張により、inチェックより遅くなる。

## Step.3: 10分以内にノーミスで3回連続解く

### 計算量の見積もり
- dictを使った解法
- 時間計算量: O(N)
- 空間計算量: O(N)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
560. Subarray Sum Equals K に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/subarray-sum-equals-k/
PR: https://github.com/yas-2023/leetcode_arai60/pull/16
言語: Python3

どうぞよろしくお願い致します。
