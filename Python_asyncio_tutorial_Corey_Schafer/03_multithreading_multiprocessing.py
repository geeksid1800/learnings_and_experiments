'''
Sometimes we have synchronous code that we don't want to block us for a long time. This module provides a simple way to do that using threads/processes.
'''
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def fetch_data(param):
    '''Since we are using time, which does not have async support, this is a traditional synchronous/blocking function.'''
    print(f"Do something with {param}...", flush=True) #makes sure print is not buffered and appears immediately. Threads do some weird things
    time.sleep(param)
    print(f"Done with {param}!", flush=True)
    return f"Result for {param}"


async def main():
    
    # Approach 1: Run in threads
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1)) #notice how we don't call the function, just pass it as a reference along with its arguments
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("Thread1 fully completed")
    result2 = await task2
    print("Thread2 fully completed")
    print("*"*20, "Multithreading example complete", "*"*20)

    # Approach 2: Run in process pool
    loop = asyncio.get_running_loop() #Gets the currently running event loop.

    with ProcessPoolExecutor() as executor: #Creates a pool of worker processes. These are separate Python processes, not threads.
        task1 = loop.run_in_executor(executor, fetch_data, 1) #run_in_executor(...) submits the work right away. It does not wait until you later await it.
        task2 = loop.run_in_executor(executor, fetch_data, 2)
        
        result1 = await task1
        print("Process 1 fully completed")
        result2 = await task2
        print("Process 2 fully completed")
    
    return [result1, result2]

if __name__ == "__main__":
    results = asyncio.run(main())
    print(results)