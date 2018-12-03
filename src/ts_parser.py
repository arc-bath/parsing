def ts_parser(filename):
    '''
    Read structs from IHW/SCP file format:
    
    <element label> <x_coor> <y_coor> <z_coor>
    ** indicates end of structure
    ## indicates end of file

    Return list:
    [ [[ elements ]],
      [[ x ]],
      [[ y ]],
      [[ z ]] ]

    Convert x, y, z to floats.

    Part2:

    If line is empty raise execption
    If element line does not contain three floats store float(nan)
    If file does not end with ## riase exception
    '''

    all_elements = []
    all_x = []
    all_y = []
    all_z = []

    ## read file

    with open(filename) as file:
        for line in file:
            # process file

    return [ all_elements,
             all_x,
             all_y,
             all_z ]

