import ts_parser as tsp

def test_proc_ts_coords():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/ts_coords.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 38
    num_atoms = [ 35, 45, 39, 45, 51, 39, 51, 33, 42, 36, 42, 39, 42, 48, 48, 
                  42, 36, 42, 42, 42, 42, 33, 51, 42, 48, 33, 48, 45, 39, 42, 
                  48, 42, 45, 45, 39, 45, 39 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_a():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_struct_a.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 1
    num_atoms = [2]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_b():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_struct_b.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 2
    num_atoms = [ 4, 4 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_c():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_struct_c.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 3
    num_atoms = [ 2, 4, 6 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_d():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_struct_d.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 3
    num_atoms = [ 2, 4, 6 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_3():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_struct_e.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 3
    num_atoms = [ 2, 4, 6 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms


