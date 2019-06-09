# Simple heap memory allocator
## **word** `AG_HEAP_ENDPTR` 

> Pointer to the beginning of unsegmented memory

## **word[16]** `AG_HEAP_FREEPTRARY` 

> Free list head pointers, indexed by log2(size)

## **subroutine** `AG_HEAP_ALLOC`(in *size*, out *address*) 

> Allocate space on the heap

### Registers

| Register | Mode | Description |
| - | - | - |
| `A` | in | **size**: minimum size to allocate |
| `B` | out | **address**: base address of allocation |

Clobbers `I`, `J`

TODO: Take in the pool index directly instead of number of words needed.
This is usually known at compile time after all.
## **subroutine** `AG_HEAP_FREE`(in *address*) 

> Free allocated space on the heap

### Registers

| Register | Mode | Description |
| - | - | - |
| `A` | in | **address**: base address of allocation to free |

Clobbers `I`
