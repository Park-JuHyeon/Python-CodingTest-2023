# 백준 1991 -> 트리순회
import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()    # A ,B C 로 받을거라서
    tree[root] = [left, right]

def preorder(now):   # 전위
    if now == '.':
        return
    print(now, end = ' ')    # 루트
    preorder(tree[now][0])   # 왼쪽노드 탐색
    preorder(tree[now][1])   # 오른쪽 노드 탐색

def inorder(now):   # 중위
    if now == '.':
        return
    
    inorder(tree[now][0])   # 왼쪽노드 탐색
    print(now, end = ' ')    # 루트
    inorder(tree[now][1])   # 오른쪽 노드 탐색

def postorder(now):   # 후위
    if now == '.':
        return
    
    postorder(tree[now][0])   # 왼쪽노드 탐색
    postorder(tree[now][1])   # 오른쪽 노드 탐색
    print(now, end = ' ')    # 루트

preorder('A')
print()
inorder('A')
print()
postorder('A')






