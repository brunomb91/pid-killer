import wmi
import os
import signal

class PID_Killer:
    def __init__(self, fileOfProcesses):
        # self.__processName = processName
        self.__fileOfProcesses = fileOfProcesses

    def killer(self):
        f = wmi.WMI()
        pid_list = []

        listOfNames = []
        fp = open('deny-list.txt', 'r')
        listOfNames = fp.read().split('\n')
        
        # Buscar programas pelo nome
        
        for name in listOfNames:
            for i in f.Win32_Process():
                if i.name.count(name) >= 1 or i.name.count(name.lower()) >= 1:
                    pid_list.append(i.ProcessId)
                    # print(i.ProcessId)

        for pid in pid_list:
            try:
                os.kill(pid, signal.SIGABRT)
            except OSError:
                print ("Processo morto")
            except KeyboardInterrupt:
                print ("Execução do programa interrompida")

        pid_list.clear()
    