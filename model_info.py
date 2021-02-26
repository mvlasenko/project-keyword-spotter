from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import model
import numpy as np


def main():
  parser = argparse.ArgumentParser()
  model.add_model_flags(parser)
  args = parser.parse_args()
  interpreter = model.make_interpreter("models/" + args.model_file)
  interpreter.allocate_tensors()


  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()


  input_shape = input_details[0]['shape']

  print(input_shape)




if __name__ == "__main__":
  main()
