import os
import time

pid = os.fork() #Creation du fils

if pid == 0 : #le code executer par le processus fils
    print("I'm the child and my pid is", os.getpid())
    print("My father's pid is ", os.getppid())
    time.sleep(3) # le processus fils attend time.sleep(n) n second avant de se terminer
    exit(0)
else: #le code du processus pere
    option = os.WSTOPPED | os.WEXITED # option
    idtype = os.P_ALL #n'importe qu'elle pid fils
    id = pid #le pid fils
    print("I'm the father and my pid is", os.getpid())
    print("My child's pid is ", pid)
    status = os.waitid(idtype, id, option) #on recupere le status du fils mort
    print("I'm the father, my dead child's status is : ", status)
    if status.si_status == 0: #on verifie le status du fils mort
        print("My child's ended normal\nhis return code is", status.si_status)#si le fils s'est terminer normalement
    else:
        print("You killed my child\nhis return code is", status.si_status); #ou s'il a recu un signal qui la interrompu
