from queue import Queue
import time


def _sleep(seconds):
    start_time = time.time()
    while time.time()-start_time < seconds:
        yield


async def sleep(seconds):
    task = create_task(_sleep(seconds))
    return await task


event_loop = Queue()


class Task():
    def __init__(self, generator):
        self.iter = generator
        self.finished = False

    # keep track of if the generator is done running
    def done(self):
        return self.finished

    def __await__(self):
        while not self.finished:
            # print("rohit")
            yield self


def create_task(generator):
    task = Task(generator)
    event_loop.put(task)

    return task


def run(main):
    event_loop.put(Task(main))

    while not event_loop.empty():
        task = event_loop.get()
        try:
            task.iter.send(None)
        except StopIteration:
            task.finished = True
        else:
            event_loop.put(task)
