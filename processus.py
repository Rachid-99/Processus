import os
import time

pid = os.fork()

if pid == 0 :
    print("I'm the child and my pid is", os.getpid())
    print("My father's pid is ", os.getppid())
    time.sleep(3)
    exit(12)
else:
    option = os.WSTOPPED | os.WEXITED
    idtype = os.P_ALL
    id = pid
    print("I'm the father and my pid is", os.getpid())
    print("My child's pid is ", pid)
    status = os.waitid(idtype, id, option)
    print("I'm the father, my dead child's status is : ", status)

