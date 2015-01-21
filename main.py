#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from __future__ import print_function, unicode_literals

import argparse
import calendar
import datetime as dt
import os
import sys

import parsedatetime
import requests

# Unbuffer stdout
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)


parser = argparse.ArgumentParser(
    prog="logentries-search",
    description=""
)
parser.add_argument(
    'host',
    type=str,
    help="The name of the host to retrieve the log from"
)
parser.add_argument(
    'log',
    type=str,
    help="The name of the log to retrieve"
)
parser.add_argument(
    '-f',
    '--filter',
    dest='the_filter',
    type=str,
    default=None,
    help="The logentries syntax filter to search by"
)
parser.add_argument(
    '-s',
    '--start',
    type=str,
    default=None,
    help="The start time for the search, defaults to 20 minutes ago. If it is a number, this many minutes will be taken off the end time."
)
parser.add_argument(
    '-e',
    '--end',
    type=str,
    default=None,
    help="The end time for the search, defaults to now."
)

URL_TEMPLATE = 'https://pull.logentries.com/{account_key}/hosts/{host}/{log}/'


def main(host, log, start, end, the_filter):
    url = URL_TEMPLATE.format(
        account_key=os.environ['LOGENTRIES_ACCOUNT_KEY'],
        host=host,
        log=log,
    )

    params = {}
    if end is None:
        end = dt.datetime.utcnow()
    else:
        end = parse_human_datetime(end)

    if start is None:
        start = 20

    try:
        start = float(start)
        start = end - dt.timedelta(minutes=start)
    except ValueError:
        start = parse_human_datetime(start)

    params['end'] = as_logentries_timestamp(end)
    params['start'] = as_logentries_timestamp(start)

    if the_filter is not None:
        params['filter'] = the_filter

    r = requests.get(url, params=params)

    if r.status_code != 200:
        print("Cannot retrieve log, got error message:", file=sys.stderr)
        print(r.content, file=sys.stderr)
        return 1

    print(r.content)

    return 0


parse_cal = parsedatetime.Calendar()


def parse_human_datetime(a_string):
    parsed, result = parse_cal.parse(a_string)
    if result == 0:
        # Not parsed at all
        raise ArithmeticError()

    elif result == 1:
        # is a date
        date_fields = parsed[:3]
        return dt.datetime(*date_fields)

    elif result == 2:
        # is a time
        h, m, s = parsed[3:6]
        today = dt.datetime.utcnow()
        return today.replace(hour=h, minute=m, second=s)

    if result == 3:  # parsedatetime magic for "it's a datetime"
        datetime_fields = parsed[:6]  # the last two seem bad
        return dt.datetime(*datetime_fields)
    else:
        return None


def as_logentries_timestamp(a_datetime):
    """
    Milliseconds since UNIX epoch
    """
    return calendar.timegm(a_datetime.timetuple()) * 1000


if __name__ == '__main__':
    kwargs = dict(parser.parse_args(sys.argv[1:])._get_kwargs())
    sys.exit(main(**kwargs))
