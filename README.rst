============
Py.test demo
============

This is a little demo I gave to show how tests can be rewritten in py.test and highlights some of the basic py.test features

Tests can be run using the following command::

    $ py.test

To select a particular test by name::

    $ py.test -k test_name

To select a particular test by path::

    $ py.test path_to_test_file/test_file.py::TestClass::test_method


Parametrized tests
==================

``test_old.py`` contains two tests written using unittest syntax, while ``test_new.py`` contains the same tests rewritten using the Py.test syntax.

Marked tests
============

Tests can be marked using default or custom markers.

To run marked tests use::

    $ py.test -m marker_name

To run all the test but the marked ones::

    $ py.test -m 'not marker_name'


