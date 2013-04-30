#!/usr/bin/env python
# -*- coding:utf8 -*-

__author__ = "Daniel Grindelid"
__date__ = "$2013-04-26 15:18:00$"

import sys
import os

# Debug print time in file
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

OUTPATH = '../out/'
SLEEP = 0.2

if __name__ == '__main__':
    """
    """
    logging.info("Starting filter")

    # Read command line arguments
    outpath = OUTPATH
    if sys.argv[1:2]:
        outpath = sys.argv[1:2][0]

    source = sys.stdin.read()

    if "<!DOCTYPE s-lxf SYSTEM" not in source[1:200]:
        from random import randint
        filename = ".".join([str(randint(10000000, 99999999)), "dat"])
        filepath = os.path.join(OUTPATH, filename)

        try:
            logging.info("Got %s bytes in stdin stream" % len(source))
            logging.info("Storing stream in file %s" % filepath)
            f = open(filepath, 'wb')
            try:
                f.write(b''.join(source))
            finally:
                f.close()

            if SLEEP > 0:
                logging.info("Sleeping (ZzZzz) for %s seconds. Sch..." % SLEEP)
                from time import sleep
                sleep(SLEEP)
                logging.info("Wide awake again :)")
        except Exception, e:
            logging.exception("Exception: %s" % e)
            sys.stdout.write("ERROR STORING ATTACHMENT IN " + outpath)
        else:
            logging.info("Sending event to StreamServe")
            eventdata = "\n".join(["<event>", "<attachment>",
                                   filepath, "</attachment>",
                                   "</event>"])
            sys.stdout.write(eventdata)
    else:
        logging.info("Found lxf, passing throu")
        sys.stdout.write(source)
    logging.info("Finnished filter")
