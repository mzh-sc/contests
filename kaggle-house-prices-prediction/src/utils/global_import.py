class GlobalImport:
    '''
    Can be used to import packages via function call

    def import_dependencies():
        with u.GlobalImport() as gi:
            import pandas as pd 
            gi()
    
    pd.DataFrame()
    '''
    
    def __enter__(self):
        return self

    def __call__(self):
        import inspect
        self.collector = inspect.getargvalues(inspect.getouterframes(inspect.currentframe())[1].frame).locals

    def __exit__(self, *args):
        globals().update(self.collector)