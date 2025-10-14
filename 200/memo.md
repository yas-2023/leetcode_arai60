## 今回の問題
[200. Number of Islands](https://leetcode.com/problems/number-of-islands)

### 概要
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## 次に取り組む予定の問題
[695. Max Area of Island](https://leetcode.com/problems/max-area-of-island)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 座標0,0から順番に島のタイルを探し、見つかったら周囲のタイルを水になるまで再帰で探索する 
- 破壊的な方法になるが、探索状況の管理がシンプルになりそうなので、一度探索したタイルは水に変えていく方針にする
- 最後の座標まで探索したら終了し島の数を返す
- stackの方が容易に実装できそうだったので途中で再帰からstackに変更
- DFS的解法

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- https://github.com/Mike0121/LeetCode/pull/34/commits/91ef98f20a17f81aa37e72231742d7198c9b6dd3
    - DFS、BFSともに一回の探索で連結成分を全て見て回るところは同じで、違うところは探索する順番
    - 非再帰で書くと スタック = DFS、キュー = BFS 
    - 動く方向をベタ書きせずに、配列に入れてforで回す
- https://github.com/docto-rin/leetcode/pull/17
    - 再帰での実装もされている 
    - 通常、関数の引数は非破壊が期待される 関数の使い手に配慮すべき

### 解法の種類
- 1. DFS（非破壊的）
    - 
- 2. BFS（破壊的）
    - 
- 3. Union Find
    - 

## Step.3: 10分以内にノーミスで3回連続解く

### 計算量の見積もり
- Union Findで実装してみる
- N: gridの要素数(rows x columns)
- 時間計算量: O(N)
- 空間計算量: O(N)


## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
200. Number of Islands に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/number-of-islands/
PR: https://github.com/yas-2023/leetcode_arai60/pull/17
言語: Python3

どうぞよろしくお願い致します。
