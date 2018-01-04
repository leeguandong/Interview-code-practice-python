'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的
最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，
请返回0。
'''

'''
这一题也不好解，在算法上，考虑数字没有重复的情况的话，使用二分法，有两个指针，第一个指针指向front，第二个指针指向rear，
midIndex是中间数字，只要是旋转数组，那么首位一定大于中间位，所以如果首位大于中间位的话，那么就把指针从首位移到中间
位，前面数字向后移动，不断迭代，当首位和最后位只差1时，最后维就是最小值。此时最坏时间复杂度是O(logn),但是要考虑数字
重复的话，情况只可能是首位和末尾和中间重这种[1,0,1,1]只能取其中最小值，逐一排列，对于首位和中间位重的，比如[1,1,0],
把首位移动到后面去，可以处理，或者中间位和末尾重，比如[1,0,0]，也是能处理，其他情况不存在，因为前提要求是旋转数组
830ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        front, rear = 0, len(rotateArray) - 1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[midIndex] and rotateArray[front] == rotateArray[rear]:
                return self.minOrder(rotateArray, front, rear)

            if rotateArray[front] <= rotateArray[midIndex]:
                front = midIndex
            elif rotateArray[rear] >= rotateArray[midIndex]:
                rear = midIndex
        return rotateArray[midIndex]

    def minOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end + 1]:
            if i < result:
                result = i
        return result