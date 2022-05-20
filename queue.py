from queuelib import FifoDiskQueue
from queuelib import LifoDiskQueue
#from Queue import LifoQueue 
#import queue
  
# Initializing a queue 
q = FifoDiskQueue("queuefile") 
  
# qsize() give the maxsize  
# of the Queue  
#print(q.qsize())  
  
# Adding of element to queue 
q.push(b'a') 
q.push(b'b') 
q.push(b'c') 

q.pop  
