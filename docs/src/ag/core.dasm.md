# Core subroutine library
## **function** `AG_CORE_DROP`($word) 

> Pop one word, ignoring its value

## **function** `AG_CORE_GETII`(!x, !y) → (x, y) 

> Push two inline words

## **function** `AG_CORE_GETI`(!x) → (x) 

> Push one inline word

## **function** `AG_CORE_STASI`($word, !addr) 

> Write `$word` at address `!addr`

## **function** `AG_CORE_STASS`($word, $addr) 

> Write `$word` at address `$addr`

## **function** `AG_CORE_STLSI`($word, !offs) 

> Store `$word` at frame offset `!offs`

## **function** `AG_CORE_LDLI`(!offs) → (x) 

> Load word at frame offset `!offs`

## **function** `AG_CORE_NEWI`(!index) → (addr) 

> Allocate `2 ** !index` words on the heap

## **function** `AG_CORE_DELSI`(!index, $addr) 

> Free memory previously allocated on the heap at address `$addr` with index `!index`

## **function** `AG_CORE_ADDSI`($a, !b) → (a + b) 

> Add inline word to top of stack

## **term function** `AG_CORE_JMPI`(!addr) 

> Continue threaded execution at `!addr`

## **function** `AG_CORE_RRANGELIT`(!offs, !exit) 

> Decrement or exit if zero

If the word at offset `!offs` in the frame is not zero, decrement it and
execute the next instruction. Otherwise, continue threaded execution at
address `!exit`.

If the trailing instruction sequence ends with AG_CORE_JMPI back to the call
to this function, and does not modify the word at offset `!offs` in the
frame, it will be executed once for each value of frame[offs] from one less
than its initial value down to zero.
