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

    Later if not ...
    '''
