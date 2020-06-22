logentries-cli
==============

.. image:: https://img.shields.io/pypi/v/loentries-clis.svg
   :target: https://pypi.org/project/logentries-cli/

----

**Unmaintained:** I'm no longer maintaining this package because I am no longer
using Logentries. If you want to continue its maintenance please contact me.

----

Stream your logs from Logentries on the commandline. Provides the ``logentries``
command which makes it easy to call their
`Download API <https://logentries.com/doc/api-download/>`_ and pipe it around.

Setting up
----------

1. Install it::

    $ pip install logentries-cli

2. Find your Logentries account key. At time of writing, this can be found at
   Accounts->Profile and appears when you press the "Show" button:

   .. figure:: https://raw.github.com/adamchainz/logentries-cli/master/account-key.png

3. (Optional) store your account key in the environment variable
   ``LOGENTRIES_ACCOUNT_KEY``. You could set this up in e.g. your bashrc. Your
   other option is to always pass it to ``logentries`` with ``--account-key``.

4. Filter your logs! Run with the syntax::

        $ logentries <logset> <logname> [-f filter] [-s start] [-e end]

   Verbose help for the options is provided with ``logentries -h``.


Examples
--------

``$ logentries web nginx``

With only the required arguments (logset and log) filled in, the last 20
minutes of messages from that log are downloaded. They are streamed so they
play nicely with other commandline utilities.

``$ logentries web nginx -f code=500``

Passing a `Logentries filter <https://logentries.com/doc/search/>`_ means that
fewer messages are downloaded and you can analyze faster.

``$ logentries web nginx -f 'code=500' -s '1am' -e '5 minutes ago'``

A wide variety of date/time formats are supported for specifying the start and
end of the time period to fetch messages for, thanks to the awesome
`parsedatetime <https://github.com/bear/parsedatetime>`_ and `dateutil
<https://dateutil.readthedocs.io/en/latest/>`_.
