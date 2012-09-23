#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys
import logging
import subprocess

logger = logging.getLogger("git.pre.commit")
sumCommand = '/opt/local/bin/git diff --cached --name-status'


def getCommitSummary():
#    logger.info(sumCommand)
    logger.info(subprocess.check_output(sumCommand.split(" ")))



def initLog():
    hdfile = logging.FileHandler("/Users/gengjet/temp/git-hook.log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdfile.setFormatter(formatter)
    logger.addHandler(hdfile)
    logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    initLog()
    getCommitSummary()
