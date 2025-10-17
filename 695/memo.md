## 今回の問題
[695. Max Area of Island](https://leetcode.com/problems/max-area-of-island)

### 概要
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

## 次に取り組む予定の問題
[323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph)

## Step.1: 何も見ず考える（まずは正解を通すことを目標に）

#### 何を考えて解いていたか
- 島の最大面積を求める問題
- 前問200のUnion find解法を採用する場合は、クラス内に最大面積をを管理する変数をおいて、union関数実行時に更新すれば良さそう

#### 正解してから気づいたこと
- grid:1x1のケースでは、union関数が実行されないが、島があるケースもあり、これを考慮していなかった
- LAND_CELLが存在し、max_area_of_islandが0の場合に、max_area_of_islandを1にする実装に修正

## Step.2: 他の人の回答、レビュー内容を参考にする
### 他の人のコードを読んで考えたこと
- https://github.com/Mike0121/LeetCode/pull/36/commits/b5221484475bd2075b6d7ea8d7870ecf28830ccf
    - visitedの状態を表現する方法として、CELLの値をvisited=2としている
    - visitedの状態を表現する方法
        1. CELLの値をwater=0としている
        2. CELLの値をvisited=2としている
        3. visited配列を用意する
        4. gridをディープコピーする
    - これまで上記1,3,4は把握していたが、2はなるほど思った。1よりもデバッグはしやすそう。
- https://github.com/nanae772/leetcode-arai60/pull/19/commits/4ed0458b866226b7a6f83afb955864d46edba225
    - 再帰を使った解法も試されている(再帰利用時の注意点を下記に抜粋)
        - 盤面のサイズが最大2500なので、デフォルトのrecursionlimitだと1000なので再帰上限エラーになるが
        - LeetCode上では550000に引き上げられているので再帰でも解ける
    

### 解法の種類(step1の解法を除く)
1. DFS
2. DFS 再帰
3. BFS
4. BFS 再帰

## Step.3: 10分以内にノーミスで3回連続解く
- visited を set にすることで、in visitedの処理をO(1)にできる（listだと in visitedの処理にワーストでO(N)）
- 例外処理（入力が空配列のケース）を考慮する
- テストケースの実装

### 計算量の見積もり
DFSにて実装
- N: gridの要素数(height x width)
- 時間計算量: O(N)
- 空間計算量: O(N)

## Step.4: レビューをもとにコードを修正する

## その他

## discord送信用
お世話になっております。
695. Max Area of Island に取り組みました。
お忙しい中恐れ入りますが、お手隙の際にレビューいただけたら幸いです。

問題: https://leetcode.com/problems/max-area-of-island/
PR: https://github.com/yas-2023/leetcode_arai60/pull/18
言語: Python3

どうぞよろしくお願い致します。
