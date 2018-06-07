import time
import multiprocessing

from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() - 1

def run():
    print('Running with %s processes'%PROCESSES)
    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(get_word_counts, [
            'data1.txt',
            'data2.txt',
            'data3.txt',
            'data4.txt'
        ])
        # clean up
        p.close()
        p.join()
    print('Time taken = %f'%(time.time() - start))

if __name__ == '__main__':
    run()