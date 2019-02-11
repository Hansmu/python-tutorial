#Python tutorial
String are immutable

None is a placeholder value in Python

Tuples are immutable. Same as a list, except use () instead of [] to define it. So a tuple is an immutable list.

Can add 'pass' as placeholders in empty bodies.

Variables follow the LEGB rule, from L to B. The most specific rule gains priority:

L - Local within a function. Highest priority.

E - enclosing function locals, from inner to outer

G - global, names assigned at the top-level

B - built-in Python

A Python module is a file that has a .py extension and a Python package is any folder that has modules inside it. 
In Python two the folder had to have an \_\_init__.py file in it as well.

import abc - import resource directly. abc can be a package or a module.

from abc import xyz - import resource from another package or module. xyz can be a module, subpackage or object such as a class or function.

PEP 8 explicitly recommends absolute imports.

Sometimes relative imports are needed to avoid long import paths. Some examples:

from .some_module import some_class - same directory

from ..some_package import some_function - one directory above

from . import some_class - from init in the same folder

pylint can be used to view the code quality.

Counter object from the Collections module can be used to get statistics about items in a collection. E.g. how often they appeared.

defaultdict can be used as a dictionary, that'll automatically initialize if a value does not exist in a dict.

OrderedDict maintains the order of the values inserted into the dictionary. Regular dictionary may mix up the order.

namedtuple like a quick small class `Dog = namedtuple('Dog', 'age breed name'); Dog(age = 2, breed = 'Lab', name = 'Bob'); dog.age;`