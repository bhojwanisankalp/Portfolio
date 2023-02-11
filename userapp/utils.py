from base64 import b32encode
from hashlib import sha1
from random import random


def get_pk():
	""" Auto generate random string for Model's primary key as default task """
	primary_key = b32encode(sha1(str(random()).encode('utf-8')).digest()).lower()[:9]
	return primary_key