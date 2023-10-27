import time

stopwatches = {}


def track(name: str) -> float:
    if name not in stopwatches:
        stopwatches[name] = time.time_ns()
        return 0.
    return (time.time_ns() - stopwatches[name]) / 10**9


def reset(name: str):
    del stopwatches[name]
