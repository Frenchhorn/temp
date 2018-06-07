import multiprocessing

def run():
    books = [
        'data1.txt',
        'data2.txt',
        'data3.txt',
        'data4.txt'
    ]
    queue = multiprocessing.Queue()

    print('Enqueuing...')
    for book in books:
        print(book)
        queue.put(book)

    print('\nDequeuing...')
    while not queue.empty():
        print(queue.get())

if __name__ == '__main__':
    run()