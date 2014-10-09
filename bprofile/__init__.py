#####################################################################
#                                                                   #
# __init__.py                                                       #
#                                                                   #
# Copyright 2014, Chris Billington                                  #
#                                                                   #
# This file is part of the bprofile project (see                    #
# https://bitbucket.org/cbillington/bprofile) and is licensed under #
# the Simplified BSD License. See the LICENSE.txt file in the root  #
# of the project for the full license.                              #
#                                                                   #
#####################################################################

from .bprofile import BProfile
from __version__ import __version__

__doc__ = r""" `bprofile` is a wrapper around profile/cProfile, gprof2dot and
    dot, providing a simple context manager for profiling sections of Python
    code and producing visual graphs of profiling results. It works on Windows
    and unix.

    **View on PyPI**: http://pypi.python.org/pypi/bprofile

    **Get the source from BitBucket**: http://bitbucket.org/cbillington/bprofile

    **Read the docs at readthedocs**: http://bprofile.readthedocs.org

    *************
    Installation
    *************

    to install `bprofile`, run:

    .. code-block:: bash

        $ pip install bprofile

    or to install from source:

    .. code-block:: bash

        $ python setup.py install

    .. note::

        `bprofile` requires `graphviz <http://www.graphviz.org/Download.php>`_
        to be installed. `bprofile` looks for it in  ``C:\Program Files`` and
        ``C:\Program Files (x86)`` on Windows, and in the PATH on unix.

    *************
    Introduction
    *************

    Every time I need to profile some Python code I go through the
    same steps: looking up profile/cProfile's docs, and then reading about
    gprof2dot and graphviz. And then it turns out the code I want to profile
    is a GUI callback or something, and I don't want to profile the whole
    program because it spends most of its time doing nothing.

    profile/cProfile certainly has this functionality, which I took one look
    at, and thought: *This should be a context manager, and when it exits, it
    should call gprof2dot and graphviz automatically so I don't have to
    remember their command line arguments, and so I don't accidentally print
    a .png to standard output and have to listen to all the ASCII beep
    characters.*

    :class:`BProfile` provides this functionality.


    *************
    Example usage
    *************

    .. code-block:: python

        profiler = BProfile('output.png')

        with profiler:
            do_some_stuff()

        do_some_stuff_that_wont_be_profiled()

        with profiler:
            do_some_more_stuff()

    see  :class:`BProfile` for more information.

    .. moduleauthor:: Chris Billington <chrisjbillington@gmail.com>
    """

__all__ = ['BProfile']
