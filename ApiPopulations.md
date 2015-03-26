# Introduction #
PyGEP allows the creation of Populations of a given Chromosome (ApiChromosomes), given that the members of each population have:
  * the same Chromosome type
  * equal head length
  * a consistent number of genes
  * a single linker function (ApiLinkers)

Population handles evaluating, recombining, and selecting the next generation through its cycle method.  Each cycle increments its age attribute.

# Important Attributes #
The Population class need not be overridden.  It just requires values during instantiation.  It provides standard GEP default attributes for generational cycling, but these can be overridden after instantiation by simply assigning to them (for instance `population.exclusion_rate = 1.8`):
  * **exclusion\_level**: selection pressure _(default = 1.5)_
  * **mutation\_rate**: probability of point mutation _(default = 2 per chromosome)_
  * **inversion\_rate**: head inversion probability _(default = 0.1)_
  * **is\_transposition\_rate**: non-root transposition _(default = 0.1)_
  * **is\_transposition\_length**: available IS transposition lengths _(default = 1,2,3)_
  * **ris\_transposition\_rate**: root transposition rate _(default = 0.1)_
  * **ris\_transposition\_length**: available RIS transposition lengths _(default = 1,2,3)_
  * **gene\_transposition\_rate**: gene transposition rate _(default = 0.1)_
  * **crossover\_one\_point\_rate**: 1-point crossover rate _(default = 0.3)_
  * **crossover\_two\_point\_rate**: 2-point crossover rate _(default = 0.3)_
  * **crossover\_gene\_rate**: full gene crossover _(default = 0.1)_

Point mutation, by default, is set to a rate where it will modify about two loci per chromosome.

# Example #
```
from pygep.functions.linkers import *
from pygep import *

# Chromosome class, population size, head length, # genes, linker
p = Population(MyChromosome, 50, 8, 4, sum_linker)
              
for _ in xrange(50): # maximum number of generations
    if p.best.solved:
        break
    p.cycle() # recombine and select next generation
```