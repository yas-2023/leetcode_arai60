from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        groups = []
        groups.append(set(edges[0]))
        for edge in edges[1:]:
            union_flag = False
            for group in groups:
                if edge[0] in group or edge[1] in group:
                    group |= set(edge)
                    union_flag = True
                    break
            if union_flag:
                continue
            groups.append(set(edge))
        return len(groups)
