from random import randint
import csv
import asyncio
import aiofiles

# In this example, the AsyncFileIterable class implements only the .__aiter__()
# method as an async generator function.
# The method opens the input file and reads it in chunks.
# Then, it yields file chunks on demand. With this iterator,
# you can process large files in chunks without blocking the script’s execution.
# That’s what you simulate in the script’s main() function.


class AsyncFileIterable:
    def __init__(self, path, chunk_size):
        self.path = path
        self.chunk_size = chunk_size

    async def __aiter__(self):
        async with aiofiles.open(self.path, mode="rb") as file:
            while True:
                chunk = await file.read(self.chunk_size)
                if not chunk:
                    break
                yield chunk


async def main():
    async for chunk in AsyncFileIterable("large-file.md"):
        # Process the file chunk here...
        await asyncio.sleep(0.2)
        print(chunk.decode("utf-8"))

asyncio.run(main())


class AsyncCSVIterator:
    def __init__(self, path):
        self.path = path
        self.reader = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.reader is None:
            async with aiofiles.open(self.path, mode="r") as file:
                lines = await file.readlines()
                self.reader = csv.reader(lines)
        try:
            return next(self.reader)
        except StopIteration:
            raise StopAsyncIteration


async def main():
    csv_iter = AsyncCSVIterator("data.csv")
    # Skip the headers
    await anext(csv_iter)
    # Process the rest of the rows
    async for row in csv_iter:
        print(row)

asyncio.run(main())


async def async_range(start=0, end=5):
    for i in range(start, end):
        await asyncio.sleep(0.2)
        # When we yield we are creating a generator which takes the
        # burden of definig functions like __iter__ and __next__
        yield i


async def main():
    number_list = [i async for i in async_range(0, 5)]
    number_dict = {i: str(i) async for i in async_range(0, 5)}
    print(number_list)
    print(number_dict)


class AsyncCounterIterator:
    def __init__(self, name="", end=5):
        self.counter = 0
        self.name = name
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= self.end:
            raise StopAsyncIteration
        else:
            self.counter += 1
            await asyncio.sleep(randint(1, 3) / 10)
            return self.counter


async def task(iterator):
    async for item in iterator:
        print(item, f"From iterator {iterator.name}")


async def main():
    # This code runs sequentially:
    await task(AsyncCounterIterator("#1"))
    await task(AsyncCounterIterator("#2"))


async def main():
    # This code runs concurrenctly:
    await asyncio.gather(
        await task(AsyncCounterIterator("#1")),
        await task(AsyncCounterIterator("#2"))
    )
