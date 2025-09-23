# 83. Remove Duplicates from Sorted List
[問題83のURL](https://leetcode.com/problems/remove-duplicates-from-sorted-list)

## これまでの指摘を受けての改善点
- ファイル保存時にflake8を自動適用し、最終行の空行漏れという凡ミスを防止
- while node: ではなく、 while (node is not None) のように明示的に None を比較するようにしました

## Step.2
- 時間計算量：O(n)
- 空間計算量：O(1)

## Step.3
- 空間計算量は増えてしまうが、再帰を使ってみたいため、再帰にて実装
- 時間計算量：O(n)
- 空間計算量：O(n) （再帰スタック分で余分に空間を使ってしまうと解釈しました）
- Step2の非再帰の方が直感的に理解しやすく感じ、空間計算量や関数のオーバーヘッドも減るため、非再帰の方が良いと思いました。

## その他
- 問題ごとにgitブランチを切るようにしていますが、ローカル環境のフォルダ構成はどのようにされていますでしょうか？
    - 私はallというルートフォルダの下に、問題名のフォルダを作成し、そのフォルダの下にgit cloneしたリポジトリを置くようにしています。
    - 例えば、この問題は /all/83/leetcode_arai60/83 という構造になっています。
    - もっとよい管理方法があるのではと思い、ご助言をいただけたら幸いです。

## 次に取り組む予定の問題
[問題82のURL](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)
