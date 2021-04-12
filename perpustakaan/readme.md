#Introduction
versuchsstand: Python implementation for the testing platform of the newly developed sensor by IMKO Micromodultechnik.
**This package has been tested on the Raspberry Pi, thus you will find some package is only applicable on the Raspberry Pi**
==================================================================

-------------
##Requirements
-------------

Before you can start using the verscuchsstand software you have to make sure,
that you have at least the following software packages installed.

1. Python (http://python.org)
2. PySerial (http://pyserial.sourceforge.net)
3. minimalmodbus (https://pypi.org/project/minimalmodbus/)
4. implib2 (https://pypi.org/project/IMPLib2/)
5. smbus (https://pypi.org/project/smbus2/)
6. RPi.GPIO (https://pypi.org/project/RPi.GPIO/)


For instructions on how to get and install these packages on your OS
please head over to the official project pages.

##Installation
------------

Install the stable branch using pip::

    pip install versuchsstand

Depending on your system you may have to prefix these commands with ``sudo``!

##Quick Start Manual
------------------

This small quick start manual is intended to give you a basic example of how to use this library. You can use these command or just run the test_package.py

After successfully installing the package and connecting start the python Shell within your terminal::
    $ python
    Python 3.6.2 (default, Jul 17 2017, 16:44:45)
    [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Import the versuchsstand module::
    >>> import versuchsstand


