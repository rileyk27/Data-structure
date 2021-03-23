#python language

import queue

data_queue=queue.Queue()
data_queue.put("coding")
data_queue.put(1)

data_queue.qsize()
#2
data_queue.get()
#coding
data_queue.qsize()
#0
data_ququq.get()
#1

queue_list = list()

def enqueue(data):
  queue_list.append(data)
  
def dequeue():
  data=queue_list[0]
  del queue_list[0]
  return data
  
