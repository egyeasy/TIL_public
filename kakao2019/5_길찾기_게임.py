nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]

def arrange_node(node, former_nodes):
    for former in former_nodes:
        if not mat[i][0]:
            former_node = mat[i][2]
            while former_node:
                # x가 크면 버리고
                # former_node = 

                # 작으면 


def solution(nodeinfo):
    total_num = len(nodeinfo)
    mat = [[0] * 3 for _ in range(total_num + 1)]

    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    print("sorted:", nodeinfo)
    print()

    level = nodeinfo[0][1]
    former_nodes = []
    this_nodes = []
    for i in range(1, total_num):
        node = nodeinfo[i]
        # 레벨이 같으면
        if node[1] == level:
            # 이전 노드와 비교해서 정리
            arrange_node(node, former_nodes)
            # 각 레벨에 이전 노드들을 담아줘야할 듯
            this_nodes.append([i, node])
        # 레벨이 다르면
        else:
            # former nodes 리스트를 갱신
            former_nodes = this_nodes
            # 맨 왼쪽부터 돌아가면서 비교
            

    answer = [[]]
    return answer

solution(nodeinfo)