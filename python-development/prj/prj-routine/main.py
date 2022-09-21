from concurrent.futures import process
from multiprocessing import Process
import alarm_dir.alarm as alarm
import bus_times.countdown as bus
from concurrent.futures import ThreadPoolExecutor

def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()



if __name__ == "__main__":
    run_cpu_tasks_in_parallel([
        alarm.run(), 
        bus.run()
    ])
    #p1 = Process(target=alarm.run())
    #p1.start()
    #p2 = Process(target=bus.run())
    #p2.start()

