import logging, os
from logging.handlers import SysLogHandler
from colored import fg, bg, attr

"""Tutorials Helped
https://stackoverflow.com/questions/14844970/modifying-logging-message-format-based-on-message-logging-level-in-python3
https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
https://realpython.com/python-logging/
"""

class MyFormatter(logging.Formatter):
	def format(self, record):
		format_orig = self._style._fmt

		if record.levelno == logging.DEBUG:
			self._style._fmt = fg(45) + format_orig + attr(0)
		elif record.levelno == logging.WARNING:
			self._style._fmt = fg(220) + format_orig + attr(0)
		elif record.levelno == logging.ERROR:
			self._style._fmt = fg(196) + format_orig + attr(0)
		elif record.levelno == logging.CRITICAL:
			self._style._fmt = fg(201) + format_orig + attr(0)

		result = logging.Formatter.format(self, record)

		self._style._fmt = format_orig

		return result

class CreateLogger:
	def __init__(self, logger_name, log_file):
		# Create a custom logger
		self.logger = logging.getLogger(logger_name) # name of the module
		self.logger.setLevel(logging.DEBUG)

		# Create handlers
		c_handler = logging.StreamHandler()
		f_handler = logging.FileHandler(log_file)
		sysl_handler = SysLogHandler(address='/dev/log')

		sysl_handler.setLevel(logging.CRITICAL)
		# c_handler.setLevel(logging.NOTSET)
		f_handler.setLevel(logging.ERROR)

		# Create formatters and add it to handlers
		c_format = MyFormatter('%(name)s - %(levelname)s - %(message)s')
		f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		sysl_format = logging.Formatter('sentinel-logger: %(message)s')
		c_handler.setFormatter(c_format)
		f_handler.setFormatter(f_format)
		sysl_handler.setFormatter(sysl_format)

		# Add handlers to the logger
		self.logger.addHandler(c_handler)
		self.logger.addHandler(f_handler)
		self.logger.addHandler(sysl_handler)

	def debug(self, msg):
		if os.getenv('ENV') == 'development':
			self.logger.debug(msg)

	def info(self, msg):
		self.logger.info(msg)

	def warning(self, msg):
		self.logger.warning(msg)

	def error(self, msg):
		self.logger.error(msg)

	def critical(self, msg):
		self.logger.critical(msg)
