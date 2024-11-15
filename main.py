from threading import Thread, Lock

global_var = 0
lock = Lock()  # Se crea un objeto de bloqueo

class IncrementThread(Thread):
    def run(self):
        global global_var
        with lock:  # Se usa el bloqueo para proteger la sección crítica
            read_value = global_var
            print(f"global_var in {self.name} is {read_value}")
            global_var = read_value + 1
            print(f"global_var in {self.name} after increment is {global_var}")

def use_increment_thread():
    threads = []
    for i in range(50):
        thread = IncrementThread()
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    print()
    print(f"After 50 modifications, global_var should be 50")
    print(f"But after 50 modifications, global_var is {global_var}")

if __name__ == "__main__":
    use_increment_thread()
