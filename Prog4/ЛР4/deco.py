import functools

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, func.__doc__, args, kwargs) 
        if not inner.called: 
   
            func(*args, **kwargs)
            inner.called = True # ? 
            print('called is changed')
    
    print('init')       
    inner.called = False # ? 
    return inner 
