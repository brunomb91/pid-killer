from pid_killer import PID_Killer

if __name__ == '__main__':
    # Matar processo
    while True:
        processes_to_kill = []
        
        with open('deny-list.txt', 'r') as f:
            while f.readline() != '':
                processes_to_kill.append(f.readline())

        for data in processes_to_kill:
            obj = PID_Killer(data)
            obj.killer()

