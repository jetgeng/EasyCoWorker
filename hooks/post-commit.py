#!/usr/bin/python

# -*- coding: utf-8 -*-

import os
import logging
import subprocess

logger = logging.getLogger("git.pre.commit")
sumCmd = '/opt/local/bin/git diff --cached --name-status'
getLastMsgCmd = 'git log -n 1 HEAD '


def execShellCommd(cmd):
    proc = subprocess.Popen(cmd, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate()


def getCommitSummary():
#    logger.info(sumCommand)
    print os.getcwd()
    exeOut = execShellCommd(sumCmd)
    logger.info(exeOut[0] if len(exeOut[0]) > 0 else exeOut[1])
    exeOut = execShellCommd(getLastMsgCmd)
    logger.info(exeOut[0] if len(exeOut[0]) > 0 else exeOut[1])


def initLog():
    hdfile = logging.FileHandler("/Users/gengjet/temp/git-hook.log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdfile.setFormatter(formatter)
    logger.addHandler(hdfile)
    logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    initLog()
    logging.info(os.getcwd())
    getCommitSummary()

