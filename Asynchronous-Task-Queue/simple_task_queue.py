import os
import time
import logging
import multiprocessing

from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() - 1
NUMBER_OF_TASKS = 10

def create_logger(pid):
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('logs/process_{}.log'.format(pid))
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def process_tasks(task_queue):
    proc = os.getpid()
    # logger = multiprocessing.get_logger()
    logger = create_logger(proc)
    while not task_queue.empty():
        try:
            book = task_queue.get()
            get_word_counts(book)
        except Exception as e:
            logger.error(e)
        logger.info('Process %d completed successfully'%proc)
    return True

def add_tasks(task_queue, number_of_tasks):
    for num in range(number_of_tasks):
        task_queue.put('data12.txt')
        task_queue.put('data2.txt')
        task_queue.put('data3.txt')
        task_queue.put('data4.txt')
    return task_queue

def run():
    empty_task_queue = multiprocessing.Queue()
    full_task_queue = add_tasks(empty_task_queue, NUMBER_OF_TASKS)
    processes = []
    print('Running with %d processes'%PROCESSES)
    start = time.time()
    for n in range(PROCESSES):
        p = multiprocessing.Process(
            target=process_tasks, args=(full_task_queue,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print('Time taken %f'%(time.time()-start))

if __name__ == '__main__':
    run()