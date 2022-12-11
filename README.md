# Paging-Algorithms
Code comprises of FIFO, LRU and OPTIMAL algorithms
1. First In First Out (FIFO): This is the simplest page replacement algorithm. In this algorithm, the operating system keeps track of all pages in the memory in a queue, the oldest page is in the front of the queue. When a page needs to be replaced page in the front of the queue is selected for removal.
2. Optimal Page replacement: In this algorithm, pages are replaced which would not be used for the longest duration of time in the future. 
3. Least Recently Used: In this algorithm, page will be replaced which is least recently used. 

## Output of the code: 

C:\anaconda\python.exe "C:\Users\Harsh Deep Kalita\PycharmProjects\OS\venv\PAGING.py" 
<br>
(12, 3, 0.2, 0.8)                                               
(8, 7, 0.4666666666666667, 0.5333333333333333)<br>
(12, 3, 0.2, 0.8)<br>

Process finished with exit code 0

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- LRU -> page fault = 12, page hit = 3, hit ratio = 0.2, fault ratio = 0.8
- OPTIMAL -> page fault = 8, page hit = 7, hit ratio = 0.467, fault ratio = 0.534
- FIFO -> page fault = 12, page hit = 3, hit ratio = 0.2, fault ratio = 0.8




<b>We can observe that, OPTIMAL has the least number of page faults hence, it is the best Paging Replacement Algorithm.</b>

