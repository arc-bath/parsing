# The Rainfall Problem

(C) James Grant (r.j.grant@bath.ac.uk)

The repository contains exercises based around the classic rainfall problem, to design a function `read_structures(filename)` which:

1. Reads in and process a data file containing a number of atomic structures
2. If the line begins with `##` there are no more structures
3. If the line begins with `**` that is the end of the current structure
4. Otherwise the line consists of `<Element label>  <x_coordinate>  <y_coordinate>  <z_coordinate>`
5. The element label should be read into `elements`, a list of list so that each can be accessed with [ <structure_no> ][ <element_no> ] 
6. The coordinates should be read in `x`, `y`, `z` lists of lists with the same structure as for elements.
7. The coordinates should be converted to floats.
8. Your function should count the number of elements in each structure and store these in a list, if any other elements/positions cannot be converted the structure should be marked as invalid.
9. Your function should count the number of valid and invalid structures.
10. Finally your function should return:
    ```python
    return [ valid_structs,
             [ invalid structs, [ list_of_invalid_structs ] ],
             [ elements_per_struct ],
             [[ elements ]],
             [[ x ]] , [[ y ]], [[ z ]] ]
    ```

The repository consists of a set of tests `test_parsing.py` and prototype functions `parsing.py`.  The students aim to write functions to satisfy the tests.

More detailed instructions about this exercise are available in the [Now Code lesson](https://arc-bath.github.io/now-code/02-parsing.html).
