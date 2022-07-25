import wmi
import os
import signal

class PID_Killer:
    def __init__(self, processName):
        self.__processName = processName

    def killer(self):
        f = wmi.WMI()
        pid_list = []

        # Buscar programas pelo nome
        for i in f.Win32_Process():
            if i.name.count(self.__processName) >= 1 or i.name.count(self.__processName.lower()) >= 1:
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

if __name__ == '__main__':
    # Matar processo
    while True:
        obj = PID_Killer('Store')
        obj.killer()
