# Direct threaded multitasking execution engine
## **word** `AG_THREAD_ACTIVEPTR` 

> Pointer to the currently active process

TODO: Pointing this variable to a process object shall cause that process to
execute following the next interleave. A scheduler should be responsible for
updating this variable at the appropriate time.
## **machine code** `AG_THREAD_ENTER` 

> Execute an inline threaded instruction sequence

### Inline Arguments

| Offset | Size | Description |
| - | - | - |
| 0 | 1 | Size of the stack frame to allocate |
| 1 | 1+ | Sequence of threaded instructions |

### Explanation

Within a **function** (written in machine code), `JSR AG_THREAD_ENTER`
transitions to threaded execution, pushing a new **frame** onto the call
stack and executing a threaded instruction sequence, stored immediately
after the branch.

A **threaded instruction sequence** is a **function** address followed by
any inline arguments. It is, strictly speaking, not a sequence. Most
functions expect a threaded instruction sequence as their final inline
argument, to be executed afterwards. Thus, through recursion, one threaded
instruction sequence may contain arbitrarily many others.

The new **frame** contains the following:
- The frame and machine stack pointers to be restored when the threaded
instruction sequence executes AG_THREAD_EXIT
- Space for the local variables used by the threaded instruction sequence
- Space for the machine stack at its maximum size during the execution of
the threaded instruction sequence

The machine stack size must include any data pushed during the execution of
any called **functions** (eg. one word for a function beginning with
`JSR AG_THREAD_ENTER`), plus two words in case of an interrupt.
## **term function** `AG_THREAD_EXIT`() 

> Threaded return to caller

