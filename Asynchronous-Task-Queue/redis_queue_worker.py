import redis

from redis_queue import SimpleQueue

def worker():
    r = redis.Redis()
    queue = SimpleQueue(r, 'sample')
    if queue.get_length() > 0:
        queue.dequeue()
    else:
        print('No tasks in queue')

if __name__ == '__main__':
    worker()