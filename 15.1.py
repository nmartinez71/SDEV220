#15.1
import multiprocessing, time, random
from datetime import datetime


def sayfunc():
    wait = random.uniform(0,1) #Gives a number between 0 and 1 
    time.sleep(wait) #Delays execution of the above by the wait variable

    print(f"The process is {multiprocessing.current_process().name} and the time is {datetime.now()}")

if __name__ == "__main__":
    processes = []
    for x in range(3):
        p = multiprocessing.Process(target=sayfunc)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()