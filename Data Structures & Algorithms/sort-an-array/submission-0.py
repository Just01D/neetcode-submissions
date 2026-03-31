class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge(arr, L, R, M):
            left_arr = arr[L:M+1]
            right_arr = arr[M+1:R+1]

            i,j,k = 0, 0, L

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    j+=1
                k+=1
            
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i+=1
                k+=1
            
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j+=1
                k+=1



        def mergeSort(arr, l, r):
            if l==r:
                return arr
            m = (l+r) // 2

            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)

            merge(arr,l,r,m)

            return arr
        
        return mergeSort(nums, 0, len(nums)-1)

