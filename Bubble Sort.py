import random

list_of_values = [int(random.random()*100) for _ in range(10)]
print(list_of_values)

def bubble_sort(nums):
    # 负责设置冒泡排序进行的次数（例如：n个数，则需要进行n-1次冒泡）[外循环]
    for i in range(len(nums) - 1):
        # 负责设置冒泡每次排序的循环次数[内循环]
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def bubble_sort1(nums1):
    for i in range(len(nums1) - 1):
        #设置标志位，标识是否排好序
        ex_flag = False
        for j in range(len(nums1) - i - 1):
            if nums1[j] > nums1[j + 1]:
                nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                ex_flag = True
        if not ex_flag:
            return nums1
    return nums1

print(bubble_sort(list_of_values))

print(bubble_sort1(list_of_values))