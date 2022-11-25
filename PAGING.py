from queue import Queue
def FIFO(capacity,pages):
    s = set()
    indexes = Queue()
    ph,pf = 0,0
    n = len(pages)
    for i in range(len(pages)):
        if pages[i] not in s:
            if len(s) < capacity:
                s.add(pages[i])
                indexes.put(pages[i])
            else:
                val = indexes.queue[0]
                s.remove(val)
                indexes.get()
                s.add(pages[i])
                indexes.put(pages[i])
            pf+=1
        else:
            ph+=1
    return pf,ph,ph/n,pf/n

def LRU(capacity,pages):
    s = []
    n = len(pages)
    pf, ph = 0, 0
    for i in range(len(pages)):
        if pages[i] not in s:
            if len(s) < capacity:
                s.append(pages[i])
            else:
                s.remove(s[0])
                s.append(pages[i])
            pf += 1
        else:
            ph += 1
    return pf, ph,ph/n,pf/n


def OPTIMAL(capacity,pages):
    s = []
    n = len(pages)
    pf,ph = 0,0
    for i in range(len(pages)):
        if pages[i] not in s:
            if len(s) < capacity:
                s.append(pages[i])
            else:
                for x in range(len(s)):
                    if s[x] not in pages[i + 1:]:
                        s[x] = pages[i]
            pf += 1
        else:
            ph += 1
    return pf, ph,ph/n,pf/n

capacity = 3
pages = [7,0,1,2,0,3,0,4,2,3,0,3,1,2,0]
print(LRU(capacity,pages))
print(OPTIMAL(capacity,pages))
print(FIFO(capacity,pages))