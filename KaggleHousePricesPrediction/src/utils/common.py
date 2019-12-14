def full_path_name(relative_path):
    '''Returns full path name of relative path.'''
    
    import os.path as path
    return path.join(path.abspath(''), relative_path)