# Introduction #

PyGEP provides a Chromosome base class which must be overridden to provide problem-specific expression trees and fitness functions.  Chromosomes provide the standard GEP variation operators, require both terminal symbols and non-terminal functions (ApiFunctionLibraries), and are managed by Populations (ApiPopulations).

# Required Attributes #
  * **functions**: tuple of nonterminals.  These should be actual function with a positive arity.  To specify a symbol for a nonterminal function, preface it with the `@symbol` decorator in `pygep.chromosome`.  Otherwise, it will be represented by the first letter in its name.
  * **terminals**: tuple of terminal symbols.  These can be either attributes for some data object or numeric constants.

# Important Methods #
  * `_fitness(self)`: determines the fitness of a given individual.  This is cached by the `fitness` property.  Typically one will call `self(obj)` one or more times where `obj` is some instance containing the terminal symbols as attributes.  _(Abstract)_
  * `_solved(self)`:  `True` if the problem is optimally solved.  By default this returns `False`.  Only override this if a given problem can be solved optimally and you can determine when that is the case.  Boolean return value is stored on `self.solved`.

# Example #
This is entirely arbitrary but it does illustrate the concepts behind Chromosomes and their evaluation.  Typically one will instantiate a Population to manage a group of chromosomes, so their methods aren't usually called directly.
```
    from pygep.functions.arithmetic import *
    from pygep import Chromosome
 
    class MyData(object):
        a = 10
     
    mydata = MyData() 

    class Calculation(Chromosome):
        functions = multiply, add, subtract, divide
        terminals = 'a', 1, 2

        def _fitness(self):
            return self(mydata)

        def _solved(self):
            return self.fitness == 20
```