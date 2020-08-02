# Simple heap memory allocator
## **word** `AG_HEAP_ENDPTR` 

> Pointer to the beginning of unsegmented memory

## **word[16]** `AG_HEAP_FREEPTRARY` 

> Free list head pointers, indexed by log2(size)

## **subroutine** `AG_HEAP_ALLOC`(in *index*, out *address*) 

> Allocate space on the heap

| Register | Mode | Description |
| - | - | - |
| `A` | in | **index**: allocation pool index, equal to the base 2 logarithm of the allocation size |
| `B` | out | **address**: base address of allocation |
| `C` | out | **size**: allocation size (equal to `2 ** index`) |

TODO: use the free pointer address instead of index for reduced overhead
## **subroutine** `AG_HEAP_FREE`(in *index*, in *address*) 

> Free allocated space on the heap

| Register | Mode | Description |
| - | - | - |
| `A` | in | **index**: allocation pool index that was used to allocate the memory |
| `B` | in | **address**: base address of allocation to free |
