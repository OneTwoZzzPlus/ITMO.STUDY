def simmetry(tree):
    for k in range(len(tree)):
        for i in range(2 ** k // 2):
            # print(k, i, tree[k][i], len(tree[k]) - i - 1, tree[k][- i - 1])
            if (tree[k][i] is None) != (tree[k][- i - 1] is None):
                return False
    return True
        
tree1 = [[16], [8, 24], [4, 12, 20, 28], [2, 6, 10, 14, 18, 22, 26, 30], [1, 3, None, 7, 9, 11, None, 15, 17, None, 21, 23, 25, None, 29, 31]]
tree2 = [[16], [8, 24], [4, 12, 20, 28], [2, 6, 10, None, 18, 22, None, 30], [1, None, 5, 7, 9, 11, None, None, 17, 19, 21, 23, None, None, 29, 31]]


print(simmetry(tree1))
print(simmetry(tree2))