from pid_killer import PID_Killer

if __name__ == '__main__':
    # Matar processo
    while True:
        with open('deny-list.txt', 'r') as file:
           data = file.readline()
           obj = PID_Killer(data)
           obj.killer()
