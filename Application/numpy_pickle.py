import os
import numpy as np
from .numpy_pickle_utils import (
    _validate_object,
    _warn_unused_kwargs,
    WRITABLE_ARR_ATTRS,
    PERSISTENT_ID_ARRAY,
    NumpyPickler,
    NumpyUnpickler,
)


def dump(value, filename, compress=0, cache_size=500, protocol=None,
         buffer_callback=None):
    _validate_object(filename)
    with open(filename, 'wb') as f:
        NumpyPickler(
            f, protocol=protocol, cache_size=cache_size,
            buffer_callback=buffer_callback).dump(value)
        if compress > 0:
            import zipfile
            with zipfile.ZipFile(filename, mode='a', compression=zipfile.ZIP_DEFLATED,
                                 allowZip64=True) as zipf:
                zipf.write(filename, os.path.basename(filename))
                os.remove(filename)


def load(filename, mmap_mode=None):
    with open(filename, 'rb') as f:
        obj = NumpyUnpickler(f, mmap_mode=mmap_mode).load()
    return obj


def load_old_pickle(*args, **kwargs):
    _warn_unused_kwargs(kwargs)
    # Loading numpy pickles generated before 1.16.3 will not load object
    # arrays correctly. For these files we need to open them with
    # allow_pickle=False to prevent unpickling them with the unpickling
    # machinery introduced in 1.16.3 and use the old NumPy unpickling.
    return np.load(*args, allow_pickle=False, **kwargs)


def load_compressed(filename, mmap_mode=None):
    import zipfile
    with zipfile.ZipFile(filename) as zipf:
        namelist = zipf.namelist()
        if len(namelist) != 1:
            raise ValueError('Pickled file had more than one top-level '
                             'object.  Only pickles with a single object are '
                             'supported.')
        with zipf.open(namelist[0]) as f:
            obj = NumpyUnpickler(f, mmap_mode=mmap_mode).load()
    return obj
