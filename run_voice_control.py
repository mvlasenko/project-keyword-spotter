from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import model

class ExecCommand(object):

  def __init__(self):

  def run_command(self, command, labels):
    print("Executing: [{}]".format(command))
    
    if command == "exit_application":
      sys.exit()
    else:
      os.system(command)

def main():
  parser = argparse.ArgumentParser()
  model.add_model_flags(parser)
  args = parser.parse_args()
  interpreter = model.make_interpreter(args.model_file)
  interpreter.allocate_tensors()
  mic = args.mic if args.mic is None else int(args.mic)
  exec_command = ExecCommand()
  sys.stdout.write("--------------------\n")
  sys.stdout.write("This script will execute shell commands via voice control.\n")
  sys.stdout.write("--------------------\n")

  model.classify_audio(mic, interpreter,
                       labels_file="config/labels_gc2.raw.txt",
                       commands_file="config/commands_exec.txt",
                       dectection_callback=exec_command.run_command,
                       sample_rate_hz=int(args.sample_rate_hz),
                       num_frames_hop=int(args.num_frames_hop))


if __name__ == "__main__":
  main()
