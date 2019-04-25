# Prompt: https://leetcode.com/problems/my-calendar-iii

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

# Runtime: 3036 ms, faster than 6.70% of Python3 online submissions for My Calendar III.
# Memory Usage: 13.4 MB, less than 14.29% of Python3 online submissions for My Calendar III.

class MyCalendarThree:
    def __init__(self):
        self.begins = []
        self.ends = []
        self.maxK = 0

    def findK(self):
        localK = 0
        k = 0 # keeps tracks of nested simultaneous events
        time = 0
        # indices for traversing self.begins & self.end
        begins_i = 0
        ends_i = 0
        # traverse self.begins and self.ends chronologically
        while ends_i < len(self.ends):
            # if all events have begun or if next end comes before next begin, subtract from k (an event ended)
            if begins_i >= len(self.begins) or self.ends[ends_i] < self.begins[begins_i]:
                localK -= 1
                ends_i += 1
            # if next begin comes before next end, add to k (a new event started)
            elif self.begins[begins_i] < self.ends[ends_i]:
                localK += 1
                begins_i += 1
            # this is when an event begins while another one ends; since we are using a half-open interval
            # that doesn't include the end time, these two are not simultaneous
            else:
                begins_i += 1
                ends_i += 1
            if localK > k:
                k = localK
        return k
        
    # adds element to arr and keeps sorted
    def addToArr(self, arr, element):
        added = False
        for i in range(len(arr)):
            if element < arr[i]:
                arr.insert(i, element)
                added = True
                break
        if not added:
            arr.append(element)
        
    def book(self, start: int, end: int) -> int:
        self.addToArr(self.begins, start)
        self.addToArr(self.ends, end)
        k = self.findK()
        if k > self.maxK:
            self.maxK = k
        return self.maxK


