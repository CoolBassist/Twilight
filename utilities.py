import rich
import time

def printout(s: str, colour: str = "black"):
    sl = f"[{colour}]hey"
    rich.print(sl)
    for c in s:
        rich.print(c, end="", flush=True)
        time.sleep(0.8/len(s))
