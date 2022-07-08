import wmi
import os
import signal

f = wmi.WMI()
pid_list = []

# Buscar programas pelo nome
for i in f.Win32_Process():
    if i.name.count('Store') >= 1 or i.name.count('store') >= 1:
        pid_list.append(i.ProcessId)
        print(i.ProcessId)

# Matar processo
for pid in pid_list:
    os.kill(pid, signal.SIGABRT)
