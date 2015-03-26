# Introduction #
`pygep.functions.linkers` provide two standard GEP linkers for linking the evaluation of genes.  These are passed to ApiPopulations during instantiation.

# Linkers #
  * **default\_linker**: returns a single result of evaluation for unigenic chromosomes, a tuple of results for multigenic
  * **sum\_linker**: adds the results each gene's evaluation
  * **or\_linker**: boolean ORs the results of each gene's evaluation