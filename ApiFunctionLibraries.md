# Introduction #
PyGEP provides some standard function libraries to ease development.

# Words of Caution #
You are responsible for type consistency within your chromosome's function set and for handling semantic errors.  While GEP chromosomes are guaranteed to be syntactically correct, make sure you aren't doing something weird, like mixing boolean and numeric types, and that you catch errors (such as the `ZeroDivisionError` raised by `divide(1,0)`).

# Function Libraries #
Each library puts its functions into `__all__`, so importing all of them is as easy as:
```
from pygep.functions.arithmetic import *
```

## pygep.functions.arithmetic ##
Provides basic arithmetic non-terminals for use in Chromosomes. Any semantic exceptions (ZeroDivisionError, etc.) are passed up the call chain to the user.  Typically one should catch any exceptions when calling chromosome.evaluate() and set the fitness of nonviable organisms to 0.
  * (`*`) multiply: `x * y`
  * (`+`) add: `x + y`
  * (`-`) subtract: `x - y`
  * (`/`) divide: `x / y`
  * (`^`) power: `x ** y`
  * (`Q`) root: `math.sqrt(x)`

## pygep.functions.comparison ##
Provides basic comparison non-terminals.  If each is true, it returns the first value given.  If false, it returns the second.
  * (`=`) equal: `return x if x == y else y`
  * (`U`) unequal: `return x if x != y else y`
  * (`<`) less: `return x if x < y else y`
  * (`>`) greater: `return x if x > y else y`
  * (`L`) less\_or\_equal: `return x if x <= y else y`
  * (`G`) greater\_or\_equal: `return x if x >= y else y`

## pygep.functions.logic ##
Provides basic logical operators: and, or, not, if.  The former three will return boolean values, whereas if returns one of the values passed in, so be careful mixing these with other operators.
  * (`&`) and\_op: `return x and y`
  * (`|`) or\_op: `return x or y`
  * (`!`) not\_op: `return not x`
  * (`I`) if\_op: `if x then y else z`