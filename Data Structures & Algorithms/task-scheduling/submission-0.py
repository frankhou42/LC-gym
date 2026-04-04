"""
Key Insight:
use maxHeap to see the most number task of same type that need to be
processed. use queue to track number of tasks of same type and the 
time when it will be avilable again.

we need to keep processing the task with highest freq

heapify returns None, it modifies list in-place 

Sol:
At each cycle we check the queue to see if there are free elements
at the front of the queue and add it back to maxHeap.
process the most frequent task (count decrement by 1, 
if 0 after decrement, pop) and pop it from maxHeap and 
add it to the waiting queue. We then time += 1

If there are no task in heap and queue not ready we just time = front
of queue's time

We terminate when maxHeap and queue empty

Trace:
[x,x,y,y], n = 3

iter = 2
maxHeap = []
queue = [[1,3][1,5]]

"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        maxHeap = [-counter[key] for key in counter]

        heapq.heapify(maxHeap)
        
        q = deque() #[remaining tasks of same type, which iter will it be ready]
        
        cycles = 0
        while maxHeap or q:
            cycles += 1
            if not maxHeap and q and q[0][1] > cycles:
                continue

            if q and q[0][1] == cycles:
                heapq.heappush(maxHeap, -q[0][0])
                q.popleft()
            
            if maxHeap:
                freqTask = -heapq.heappop(maxHeap)

                freqTask -= 1

                if freqTask != 0: 
                    q.append([freqTask, cycles + n + 1])
            

        return cycles