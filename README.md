# Python Race Condition Solution

This repository contains a solution to the race condition in a multi-threaded program that increments a shared variable (`global_var`). Without synchronisation, threads access and modify `global_var` simultaneously, causing inconsistent results.

## Solution Explanation

To eliminate the race condition, a lock (`Lock`) was implemented that synchronises access to the shared variable.

### Key Changes

- Creation of `Lock`**: A `lock` object is created using `threading.Lock()`.
- **Lock Usage**: Access to `global_var` is protected with `with lock` in the `run()` method of the `IncrementThread` class. This ensures that only one thread modifies the variable at a time, thus avoiding the race condition.
- Correct Result**: With this modification, `global_var` will have the expected value of 50 after 50 increments, ensuring accurate results.

Translated with DeepL.com (free version)
