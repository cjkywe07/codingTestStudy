import heapq

'''min heap'''
heap = [7, 3, 9, 4, 1, 2, 6]

heapq.heapify(heap)
print('최소힙 :', heap)

print('삭제값 : ', heapq.heappop(heap))
print('최소힙 :', heap)

heapq.heappush(heap, 5)
print('추가값 : ', 5)
print('최소힙 :', heap)
print('------------------------------')


'''max heap'''
# (1)
heap = [7, 3, 9, 4, 1, 2, 6]

heapq._heapify_max(heap)
print('최대힙 :', heap)

print('삭제값 : ', heapq._heappop_max(heap))
print('최대힙 :', heap)

# [ heapq._heappush_max() -> 존재X ]
# heapq._heappush_max(heap, 8)
# print('최대힙 :', heap)
print('------------------------------')

# (2)
heap = [7, 3, 9, 4, 1, 2, 6]
heap = [-1 * n for n in heap]

heapq.heapify(heap)
print('최대힙 :', heap)

weight = heapq.heappop(heap)
value = -1 * weight
print('삭제값 : ', value)
print('최대힙 :', heap)

heapq.heappush(heap, -8)
print('추가값 : ', 8)
print('최대힙 :', heap)
print('------------------------------')

# (3)
heap = [7, 3, 9, 4, 1, 2, 6]
heap = [(-1 * n, n) for n in heap]

heapq.heapify(heap)
print('최대힙 :', heap)

weight, value = heapq.heappop(heap)
print('삭제값 : ', value)
print('최대힙 :', heap)

heapq.heappush(heap, (-8, 8))
print('추가값 : ', 8)
print('최대힙 :', heap)
