# User function Template for python3

class Solution:

    # Function to return a list containing the union of the two arrays.
    def mergeArrays(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here
        arr = []
        i = 0
        j = 0
        c = 0
        if a[0] <= b[0]:
            arr.append(a[0])
            i += 1
        else:
            arr.append(b[0])
            j += 1

        while (i < n and j < m):
            if a[i] <= b[j]:
                if arr[c] != a[i]:
                    arr.append(a[i])
                    c += 1
                i += 1
            else:
                if arr[c] != b[j]:
                    arr.append(b[j])
                    c += 1
                j += 1

        while (i < n):
            if arr[c] != a[i]:
                arr.append(a[i])
                c += 1
            i += 1

        while (j < m):
            if arr[c] != b[j]:
                arr.append(b[j])
                c += 1
            j += 1

        return arr

# driver code
a=[1, 2, 3, 4, 5]
b=[1, 2, 3]
n=5
m=3
sol=Solution()
print(sol.mergeArrays(a,b,n,m))



