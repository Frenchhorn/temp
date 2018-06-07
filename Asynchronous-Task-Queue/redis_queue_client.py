import redis

from redis_queue import SimpleQueue
from tasks import get_word_counts

NUMBER_OF_TASKS = 10

if __name__ == '__main__':
    r = redis.Redis()
    queue = SimpleQueue(r, 'sample')
    count = 0
    for num in range(NUMBER_OF_TASKS):
        queue.enqueue(get_word_counts, 'data1.txt')
        queue.enqueue(get_word_counts, 'data2.txt')
        queue.enqueue(get_word_counts, 'data3.txt')
        queue.enqueue(get_word_counts, 'data4.txt')
        count += 4
    print('Enqueue %d tasks!'%count)