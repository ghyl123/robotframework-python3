Robot Framework Remote Servers
==============================

Introduction
------------

This directory contains remote server implementations that can be used
with Robot Framework's Remote library. The main source for information
related to the Remote library and remote servers is the User Guide.

*NOTE:* Everything here is nowadays deprecated. Enhanced versions of
both Python and Ruby remote servers discussed below are available as
separate projects:

- https://github.com/robotframework/PythonRemoteServer
- https://github.com/semperos/robot-remote-server-rb

All future development is done in the external projects. Python remote
server distributed with Robot Framework 2.8.4 is the same as 1.0 version
of the new external project. Remote servers will be removed from Robot
Framework repository and will not be part of the source distribution
starting from Robot Framework 2.9.

Implemented Remote Servers
--------------------------

There are currently remote server implementations for Python and Ruby in
following files::

   robotremoteserver.py
   robotremoteserver.rb

Notice that the Python version works also with Jython. New remote
servers, for example for Java and Perl, can be added in the future.

Examples Using Remote Servers
-----------------------------

Examples on how test libraries can use the remote servers can be found from
`example` directory. These example libraries can be started with commands::

   python example/examplelibrary.py
   jython example/examplelibrary.py
   ruby example/examplelibrary.rb

Note that all the above commands require that language's module search
path is set so that the respective remote server module can be imported.
By default the servers listen to connections to localhost on port 8270,
but this can be configured like::

   python example/examplelibrary.py localhost 7777
   ruby example/examplelibrary.rb 192.168.0.1 8270

These examples will start the remote server so that it provides
keywords implemented in the example module. After the remote server is
started, an example test case file can be executed using the familiar
`pybot` or `jybot` commands, possibly giving the port where the server
is listening as a variable::

   pybot example/remote_tests.html
   jybot example/remote_tests.html
   pybot --variable PORT:7777 example/remote_tests.html

The results should be the same regardless of the example library or start-up
script used.

Testing Remote Servers
----------------------

All remote server tests were removed in Robot Framework 2.8.4 because they
were not updated and development of the servers had moved to separate projects.
