#!/usr/bin/python3

"""
filter_datum
"""

import re
import logging

def filter_datum(fields, redaction, message, separator):

    """
    filter_datum that returns the log message obfuscated
    """
    mgs = re.sub(r'{}(?={})'.format('|'.join(fields), separator), redaction, message)
    return mg


"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))s
