print("name")
import queue,threading,time
class myThread(threading.Thread):
    def _init_(self,q1,q2):
        threading.Thread._init_(self)
        self.q1=q1
        self.q2=q2
    def run(self):
        print("Starting"+self.name)
        process_data(self.name,self.q1)
        process_data(self.name,self.q2)
        print("Exiting"+self.name)
def process_data(n,q):
    while not q.empty():
        print("{}processing{}".format(n,q.get()))
    time.sleep(5)
q1=queue.Queue(3)
q2=queue.PriorityQueue(3)
q1.put('name')
q1.put('surname')
q1.put('rno')
q2.put((10,'name'))
q2.put((1,'surname'))
q2.put((5,'rno'))
print(q2.qsize())
print(q2.full())
t1=myThread(q1,q2)
t2=myThread(q1,q2)
t1.start()
t2.start()
t1.join()
t2.join()
print(q2.empty())
