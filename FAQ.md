# Frequently Asked Questions #
#### Q: How can I write my own GEP functions? ####
A: Simple:
```
from pygep.chromosome import symbol

@symbol('~')
def foo(x, y, z):
    return bar(x, y, z)
```

Now you can use `foo` in your chromosomes just like any of the provided functions.  If your function uses a single character name, you do not need to use the `symbol` decorator.  The arity of non-terminal functions is culled from its `func_code.co_argcount`, meaning that using `*args` or `**kwds` will _not_ do anything.

See `pygep.functions` for examples.

#### Q: Can I provide my own linkers? ####
A: Of course!  A PyGEP linker just needs to accept `*args` and return a single result.  See the `sum_linker` code for an example:
```
def sum_linker(*args):
    '''Returns the sum of all sub-ETs'''
    return sum(args)
```

If you do not provide a linker for your population, the default linker will simply return the top results of each gene's evaluation.

#### Q: I know that GEP programs will always be syntactically correct provided I 	use compatible types for my operators and operands, but what do I do about semantic errors such as division by zero? ####

A: Chromosome evaluation doesn't swallow run time errors, so anything like this will be raised to whatever level you evaluate at, typically in the `_fitness(self, obj)` method.  The usual practice is to catch any such errors that occur and dock the responsible individual's fitness.  See the fitness method of the regression demo for an example of this:
```
def _fitness(self):
    total = 0
    for x in DataPoint.SAMPLE:
        try:
            guess = self(x) # Evaluation of this chromosome
            diff = min(1.0, abs((x.y - guess) / x.y))
            total += self.REWARD * (1 - diff)
	                                
        except ZeroDivisionError: # semantic error
            pass
	
    return total	
```
