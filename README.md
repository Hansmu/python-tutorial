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