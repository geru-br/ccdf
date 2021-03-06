import unittest
import pkgutil
import logging
import sys
import unittest

def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        yield 'geru.ccdf.test.' + modname

def all():
    logging.basicConfig(stream=sys.stderr)
    return unittest.defaultTestLoader.loadTestsFromNames(all_names())


class TestCase(unittest.TestCase):
    pass
