"""
날짜 : 2021/04/27
이름 : 오유리
내용 : 파이썬 자료구조 Set 실습하기 교제 p96
"""

# Set 생성
set1 = {1, 2, 3, 4, 5, 3}
print('set1 type :', type(set1))
print('set1 :', set1)

set2 = set('Hellow World')
print('set2 type :', type(set2))
print('set2 :', set2)

# 집합 출력(List 변환)
list1 = list(set1)
print('list1 :', list1)
print('list1[0] :', list1[0])
print('list1[3] :', list1[3])

list2 = list(set2)
print('list2 :', list2)
print('list2[0] :', list2[0])
print('list2[3] :', list2[3])
