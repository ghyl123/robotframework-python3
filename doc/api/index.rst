=================================
Robot Framework API documentation
=================================

This documentation describes the public API of `Robot Framework`__.
Installation, basic usage and wealth of other topics are
covered by the `Robot Framework User Guide`__.

Main API entry points are documented here, but the lower level
implementation details are not always that well documented. If the
documentation is insufficient, it is possible to view the source code
by clicking `[source]` link in the documentation. In case viewing the
source is not helpful either, questions may be sent to the
`robotframework-users`__ mailing list.

__ http://robotframework.org
__ http://code.google.com/p/robotframework/wiki/UserGuide
__ http://groups.google.com/group/robotframework-users

.. toctree::
    :maxdepth: 2

Entry points
============

Command line entry points are implemented as Python modules and they also
provide programmatic APIs. Following entry points exist:

  * :py:mod:`robot.run` entry point for executing tests.
  * :py:mod:`robot.rebot` entry point for post-processing outputs.
  * :py:mod:`robot.libdoc` entry point for the `libdoc`__ tool.
  * :py:mod:`robot.testdoc` entry point for the `testdoc`__ tool.
  * :py:mod:`robot.tidy` entry point for the `tidy`__ tool.

__ http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#libdoc
__ http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#testdoc
__ http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#tidy

Java entry points
=================

The Robot Framework Jar distribution contains also a Java API, in the form
of the `org.robotframework.RobotFramework`__ class.

__ _static/javadoc/index.html

Public API
==========

.. automodule:: robot.api

All packages
============

All :py:mod:`robot` packages are listed below. Typically you should not
need to import anything from them directly, but the above public APIs may
return objects implemented in them.

.. toctree::
    :maxdepth: 1

    autodoc/robot
    autodoc/robot.api
    autodoc/robot.conf
    autodoc/robot.htmldata
    autodoc/robot.libdocpkg
    autodoc/robot.libraries
    autodoc/robot.model
    autodoc/robot.output
    autodoc/robot.parsing
    autodoc/robot.reporting
    autodoc/robot.result
    autodoc/robot.running
    autodoc/robot.utils
    autodoc/robot.variables
    autodoc/robot.writer

Indices
=======

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
