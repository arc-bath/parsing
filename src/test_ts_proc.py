import ts_parser as tsp

def test_proc_ts_coords():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/ts_coords.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 38
    num_atoms = []
    for count in range(38):
        num_atoms.append(41)

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


