logentries-cli
==============

Get your logs from Logentries on the comandline. Provides the `logentries`
command which makes it easy to call their
`Download API <https://logentries.com/doc/api-download/>`_.


Examples
--------

``logentries web nginx``

With only the required arguments (host and log) filled in, the last 20 minutes
of messages from that log are downloaded (streamed through).

``logentries web nginx -f code=500``

Passing a `Logentries filter <https://logentries.com/doc/search/>`_ means that
fewer messages are downloaded and you can analyze faster.

``logentries web nginx -f 'code=500' -s '1am' -e '5 minutes ago'``

A wide variety of datetime formats are supported for specifying the start and
end of the time period to fetch messages for, thanks to the awesome
`parsedatetime <https://github.com/bear/parsedatetime>`_.
