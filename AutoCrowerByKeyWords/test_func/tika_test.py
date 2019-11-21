#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tika
import os
from tika import language

tika.initVM()
from tika import parser

print(os.listdir('./../test_docsavefile'))
print(language.from_file('./../test_docsavefile/aa.doc'))
parsed = parser.from_file(r'./../test_docsavefile/aa.doc')

# ph = parser.parse1('./../test_docsavefile/bb.pdf')
# print(parsed)
print(parsed["metadata"])
print(parsed["content"])

