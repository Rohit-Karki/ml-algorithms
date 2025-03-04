import rkasyncio


async def task1():
    for _ in range(2):
        print('Task 1')
        await rkasyncio.sleep(1)


async def task2():
    for _ in range(3):
        print('Task 2')
        await rkasyncio.sleep(5)


async def main():
    one = rkasyncio.create_task(task1())
    two = rkasyncio.create_task(task2())

    await one
    await two
    print('done')


if __name__ == '__main__':
    rkasyncio.run(main())
