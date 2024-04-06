"""Create portable serialized representations of Python objects."""
# Module level constants and functions go here

def dump(obj, file, protocol=None, *, fix_imports=True):
    """Write a pickled representation of obj to the open file object file."""
    # Implementation of dump function

def dumps(obj, protocol=None, *, fix_imports=True):
    """Return the pickled representation of the object as a bytes object."""
    # Implementation of dumps function

def load(file, *, fix_imports=True, encoding="ASCII", errors="strict"):
    """Read and return an object from the pickle data stored in a file."""
    # Implementation of load function

def loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict"):
    """Read and return an object from the pickle bytes object."""
    # Implementation of loads function
