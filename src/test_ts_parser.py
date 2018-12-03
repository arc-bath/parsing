import ts_parser as tsp

def test_return_list():
    '''
    Test that read_structs(filename) returns a list of 4 lists(of lists)
    '''
    expect = 4

    filename = '../data/structs.txt'

    structs = tsp.read_structs(filename)

    assert len(structs) == expect

    for item in structs:
        assert isinstance(item, list)
        for subitem in item:
            assert isinstance(subitem, list)
