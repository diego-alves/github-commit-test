""" consume module """

from logging import info
from json import loads

def process(message):
  """ Proccess the massage """
  info(message.body)
