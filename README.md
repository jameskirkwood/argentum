# Argentum DCPU Operating System

Unstable WIP

| Module | Description |
| - | - |
| **ag/heap** | A simple, standalone heap memory allocator |
| **ag/thread** | Direct threaded execution engine (uses `ag/heap`) |
| **ag/core** | Library of core "functions" (machine code subroutines that conform to the `ag/thread` ABI) |
| **ag/cpu** | Low level CPU related functions |

## Heap Implementation

> TODO: documentation

## Threaded ABI

> TODO: store the process pointer in the frame rather than storing the frame pointer in the process

A function must treat the CPU registers as follows:

- Registers `A`, `B`, `C`, `X`, `Y` and `J` are available for general use.
- Register `Z` is used as the process pointer. Its value must be preserved.
- Register `I` is used as the direct threaded instruction pointer. It may be modified to transfer control or to consume immediate arguments stored inline after the pointer to the function.
- Register `SP` is used as the operand stack pointer. It shoud be used to pop arguments and push the return value, if any.

A function must end with one of the following sequences:

- `STI PC, [I]`, which continues with the next threaded instruction
- `JSR AG_THREAD_ENTER`, followed by the required inline arguments as specified in docs/src/ag/thread.dasm.md

### Process Objects

During the execution of a function, the `Z` register points to the current process object. It may be used to access the stack frame for the active thread, as well as any process global variables for which space has been allocated.

A process object has the following structure:

```c
struct process {
    frame_ptr; // [Z + 0] pointer to the current call stack frame
    backup_ip; // [Z + 1] saved instruction pointer (when inactive)
    backup_sp; // [Z + 2] saved stack pointer (when inactive)
    globals[]; // flexible area for process global variables
}
```

### Stack Frames

Stack frames (thread activation records) are not stored on the machine stack. Instead, they are stored as singly linked list nodes on the heap.

The machine stack (associated with the `SP` register) is allocated within the stack frame, in addition to the thread's local variables and the caller's frame and stack pointers to be restored when the thread returns.

The calling thread's instruction pointer (callee's return link) is stored on the caller's stack to reduce the size of the callee's frame.

The structure of a stack frame is as follows:

```c
struct frame {
    caller_fp; // [[Z] + 0] caller's frame pointer (list 'next' pointer)
    caller_sp; // [[Z] + 1] caller's stack pointer
    locals[];  // flexible area for thread local variables and stack
}
```
