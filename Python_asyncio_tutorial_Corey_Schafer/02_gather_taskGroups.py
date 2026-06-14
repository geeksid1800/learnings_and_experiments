'''
Sometimes we want to create multiple tasks and schedule/run them all at once. We can do this using asyncio.gather() or asyncio.TaskGroup().
'''
import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}!")
    return f"Result for {param}"


async def main():
    #Create Tasks manually
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    print(f"Task 1 and 2 awaited results: {[result1, result2]}")


    #Gather Coroutines
    coroutines = [fetch_data(i) for i in range(1,3)]
    #gather takes in multiple coroutine objects/functions and schedules them, instead of having to create a Task for each one manually.
    results = await asyncio.gather(*coroutines, return_exceptions=True) #return_exceptions=True allows us to get exceptions as part of the results list instead of them being raised immediately.
    print(f"Coroutines gathered results: {results}")


    #Gather Tasks - since it's a wrapper around Coroutines, Tasks offer some additional features like cancellation and exception handling.
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1,3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Tasks gathered results: {results}")


    #Task Groups
    async with asyncio.TaskGroup() as tg:
        '''
        TaskGroup itself is an async context manager that allows us to create and manage multiple tasks within its block.
        All tasks are awaited when the context manager exits, so we don't need to await them manually.
        If any of the tasks raise an exception, the context manager will raise an exception as well.
        So in a sense this is atomic: either all tasks succeed or all fail together. If one task raises an exception, the other tasks will be cancelled.
        '''
        results = [tg.create_task(fetch_data(i)) for i in range(1,3)]
    print(f"TaskGroup results: {[result.result() for result in results]}")

    return "Main Coroutine Done"

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)