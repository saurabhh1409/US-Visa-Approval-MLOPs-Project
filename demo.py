from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("This is a info message")

try:
    a = 1/0
except Exception as e:
  raise USvisaException(e, sys)