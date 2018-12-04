import ts_parser as tsp

def test_proc_ts_coords():
    '''
    Test that proc_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/ts_coords.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 38
    num_atoms = [ 35, 44, 38, 44, 50, 38, 50, 32, 41, 35, 41, 38, 41, 47, 47, 
                  41, 35, 41, 41, 41, 41, 32, 50, 41, 47, 32, 47, 44, 38, 41,
                  47, 41, 44, 44, 38, 44, 38, 44 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_a():
    '''
    Test that proc_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_a.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 1
    num_atoms = [2]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_b():
    '''
    Test that proc_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_b.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 2
    num_atoms = [ 4, 4 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_c():
    '''
    Test that proc_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_c.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 3
    num_atoms = [ 2, 4, 6 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_d():
    '''
    Test that proc_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_d.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 3
    num_atoms = [ 2, 4, 6 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms

def test_proc_struct_e():
    '''
    Test that proc_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_e.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_structs = 3
    num_atoms = [ 2, 4, 6 ]

    assert struct_info[0] == num_structs
    assert struct_info[1] == num_atoms


def test_proc_ts_coords():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/ts_coords.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_inv = 0
    list_inv = []

    assert struct_info[2][0] == num_inv
    assert struct_info[2][1] == list_inv

def test_proc_struct_a():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_a.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_inv = 0
    list_inv = []

    assert struct_info[2][0] == num_inv
    assert struct_info[2][1] == list_inv

def test_proc_struct_b():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_b.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_inv = 0
    list_inv = []

    assert struct_info[2][0] == num_inv
    assert struct_info[2][1] == list_inv

def test_proc_struct_c():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_c.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_inv = 0
    list_inv = []

    assert struct_info[2][0] == num_inv
    assert struct_info[2][1] == list_inv

def test_proc_struct_d():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_d.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_inv = 1
    list_inv = [ 1 ]

    assert struct_info[2][0] == num_inv
    assert struct_info[2][1] == list_inv

def test_proc_struct_e():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    filename = '../data/test_structs_e.txt'

    structs = tsp.read_structs(filename)

    struct_info = tsp.proc_structs(structs)

    num_inv = 1
    list_inv = [ 1 ]

    assert struct_info[2][0] == num_inv
    assert struct_info[2][1] == list_inv


