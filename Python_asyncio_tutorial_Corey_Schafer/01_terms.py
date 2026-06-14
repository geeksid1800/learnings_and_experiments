import asyncio
import time

def sync_function(test_param: str) -> str:
    print("This is a synchronous function.")

    time.sleep(1)

    return f"Sync Result: {test_param}"

#ALSO KNOWN AS A COROUTINE FUNCTION
async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function.")

    await asyncio.sleep(1)

    return f"Async Result: {test_param}"

async def fetch_data(param: int) -> str:
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}!")
    return f"Result for {param}"

async def main():
    # sync_result = sync_function("Hello")
    # print(sync_result)

    # """
    # Calling this coroutine function does not execute it, but instead returns a coroutine object that can be awaited to get the result of the coroutine function.
    # The await keyword suspends the current coroutine function (including main) and hands back control to the event loop. In the background, 
    # the awaited value can be fetched/prepared.
    # When the event loop sees that this coroutine's return value is ready, it will pick it up when it (event loop) has control again and resume execution where it left off.
    # """
    # coroutine_obj = async_function("Test")
    # print(coroutine_obj)

    # """when we await a coroutine object, it's both scheduled on the event loop and run to completion at the same time."""
    # coroutine_result = await coroutine_obj
    # print(coroutine_result)

    """
    Tasks are wrapped coroutines that can be executed independently, and are how we run coroutines concurrently.
    When we wrap a coroutine in a Task (using asyncio.create_task()), it is handed over to the event loop and scheduled to run whenever it gets a chance.
    The task will keep track of whether the coroutine finished successfully, raised an error, got cancelled or is still pending.
    """
    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)

    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    return [result1, result2]
    

if __name__ == "__main__":
    asyncio.run(main())