# Chapter 10 – Debugging

> Q: 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

`assert(spam >= 10, 'The spam should be less than 10.')`

> Q: 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

`assert(eggs.lower() != bacon.lower(), 'The eggs and bacon should contain different string.')`

> Q: 3. Write an assert statement that always triggers an AssertionError.

`assert(False, 'Always triggers an AssertionError')`

> Q: 4. What are the two lines that your program must have in order to be able to call logging.debug()?

```py
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

> Q: 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

```py
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

> Q: 6. What are the five logging levels?

DEBUG, INFO, WARNING, ERROR, CRITICAL

> Q: 7. What line of code can you add to disable all logging messages in your program?

`logging.disable()`

> Q: 8. Why is using logging messages better than using print() to display the same message?

You can disable logging message without removing the logging function calls. You can selectively disable lower-level logging messages.

> Q: 9. What are the differences between the Step, Over, and Out buttons in the Debug Control window?

Step: move in the function call.
Over: execute the function call without stepping into it.
Out:  execute the rest of the code until it steps out of the function it currently is in.

> Q: 10. After you click Go in the Debug Control window, when will the debugger stop?

the end of the program or a line with a breakpoint.

> Q: 11. What is a breakpoint?

debugger to pause.

> Q: 12. How do you set a breakpoint on a line of code in IDLE?

Set breakpoint.