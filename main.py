from pid_killer import PID_Killer

if __name__ == '__main__':
    # Matar processo
    while True:
        obj = PID_Killer('Store')
        obj.killer()
