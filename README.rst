logentries-cli
==============

Get your logs from Logentries on the comandline. Provides the
``logentries`` command which makes it easy to call their
`https://logentries.com/doc/api-download/ <Download%20API>`__.

Examples
--------

``logentries web nginx``

With only the required arguments (host and log) filled in, the last 20
minutes of messages from that log are downloaded (streamed through).

``logentries web nginx -f code=500``

Passing a `https://logentries.com/doc/search/ <Logentries%20filter>`__
means that fewer messages are downloaded and you can analyze faster.

``logentries web nginx -f 'code=500' -s '1am' -e '5 minutes ago'``

A wide variety of datetime formats are supported for specifying the
start and end of the time period to fetch messages for, thanks to the
awesome `https://github.com/bear/parsedatetime <parsedatetime>`__.
