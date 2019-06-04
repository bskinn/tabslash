.. tabslash documentation master file, created by
   sphinx-quickstart on Tue Jun  4 15:53:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tabslash's documentation!
====================================

.. tabs:: 
    .. group-tab:: no-slash

        .. autofunction:: tabslash.tabslash.foo

    .. group-tab:: with-slash

        .. autofunction:: tabslash.tabslash.foo(a, b, /)


.. tabs:: 
    .. group-tab:: no-slash

        .. autofunction:: tabslash.tabslash.bar

    .. group-tab:: with-slash

        .. autofunction:: tabslash.tabslash.bar(a, /, b, *, c=1)


.. toctree::
    :maxdepth: 2
    :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
