#! /usr/bin/python3

import sys, shutil, os, re, codecs, pprint

def replacetoken(sInput,sOld,sNew):
    sOutput = sInput.replace(sOld,sNew)
    return sOutput

def escapehtml(sInput):
    sOutput = sInput.replace("&","&apos;")
    sOutput = sOutput.replace(">","&gt;")
    sOutput = sOutput.replace("<","&lt;")
    return sOutput


def testdef():
    sResult = escapehtml("& Aho <>")
    print(sResult)

def main():
    testdef()

if __name__ == '__main__':
    main()