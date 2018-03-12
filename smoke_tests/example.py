#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from absl import app
from absl import flags
from absl import logging

import testtemp
import filetemp.testtemp

FLAGS = flags.FLAGS

FLAGS.alsologtostderr = True
FLAGS.log_dir = 'temp/log/'

print("log_dir: ", logging.find_log_dir())
print("actual_log_dir, file_prefix, program_name: ",
      logging.find_log_dir_and_names('main'))

flags.DEFINE_string('log_file', 'main', 'Text to echo.')


def main(argv):
    logging.get_absl_handler().start_logging_to_file(FLAGS.log_file)

    print("logging path: ", logging.get_log_file_name())
    logging.info(
        'Running under Python {0[0]}.{0[1]}.{0[2]}'.format(sys.version_info))
    logging.info("logging level: %d" % logging.get_verbosity())

    for i in range(50):
        logging.log_every_n(logging.INFO, "log_every_10", 10)


if __name__ == '__main__':
    app.run(main)
