def full_path_name(relative_path):
    '''Returns full path name of relative path.'''
    
    import os.path as path
    return path.join(path.abspath(''), relative_path)


def load_notebook(notebook_name):
    import sys
    from importnb import reload

    if notebook_name in sys.modules:
        reload(sys.modules[notebook_name])
    
