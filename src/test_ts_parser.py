import ts_parser as tsp

def test_read_ts_coords():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    expect = 4

    filename = '../data/ts_coords.txt'

    structs = tsp.read_structs(filename)

    assert len(structs) == expect

    for item in structs:
        assert isinstance(item, list)
        for subitem in item:
            assert isinstance(subitem, list)

def test_read_ts_coords2():
    '''
    Test that read_structs(filename) returns a list of 4 lists:
    of correct length and correct type.
    '''

    filename = '../data/ts_coords.txt'

    structs = tsp.read_structs(filename)

    for item in structs:
        assert len(item) == 38

    for item in structs[0]:
        for subitem in item:
            assert isinstance(subitem, str)
    
    for item in structs[1]:
        for subitem in item:
            assert isinstance(subitem, float)
    
    for item in structs[2]:
        for subitem in item:
            assert isinstance(subitem, float)
    
    for item in structs[3]:
        for subitem in item:
            assert isinstance(subitem, float)

def test_read_structs_a():
    '''
    Test that read_structs(filename) returns a list of 4 lists:
    of the expected length
    '''
    expect = 4

    filename = '../data/test_structs_a.txt'

    structs = tsp.read_structs(filename)

    assert len(structs) == expect

    for item in structs:
        assert len(item) == 1
        assert len(item[0]) == 2

def test_read_structs_b():
    '''
    Test that read_structs(filename) returns a list of 4 lists:
    of the expected length
    '''
    expect = 4

    filename = '../data/test_structs_b.txt'

    structs = tsp.read_structs(filename)

    assert len(structs) == expect

    for item in structs:
        assert len(item) == 2
        assert len(item[0]) == 4
        assert len(item[1]) == 4

def test_read_structs_c():
    '''
    Test that read_structs(filename) returns a list of 4 lists 
    of the expected length
    '''
    expect = 4

    filename = '../data/test_structs_c.txt'

    structs = tsp.read_structs(filename)

    assert len(structs) == expect

    for item in structs:
        assert len(item) == 3
        assert len(item[0]) == 2
        assert len(item[1]) == 4
        assert len(item[2]) == 6
