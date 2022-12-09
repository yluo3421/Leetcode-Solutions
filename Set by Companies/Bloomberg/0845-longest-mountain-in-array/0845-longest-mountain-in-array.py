class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        For a starting index base, let's calculate the length of the longest mountain A[base], A[base+1], ..., A[end].

If such a mountain existed, the next possible mountain will start at base = end; if it didn't, then either we reached the end, or we have A[base] >= A[base+1] and we can start at base + 1.

Here is a worked example on the array A = [1, 2, 3, 2, 1, 0, 2, 3, 1]:
base starts at 0, and end travels using the first while loop to end = 2 (A[end] = 3), the potential peak of this mountain. After, it travels to end = 5 (A[end] = 0) during the second while loop, and a candidate answer of 6 (base = 0, end = 5) is recorded.

Afterwards, base is set to 5 and the process starts over again, with end = 7 the peak of the mountain, and end = 8 the right boundary, and the candidate answer of 4 (base = 5, end = 8) being recorded.
        """
        N = len(arr)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and arr[end] < arr[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and arr[end] < arr[end+1]:
                    end += 1

                if end + 1 < N and arr[end] > arr[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and arr[end] > arr[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans