from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import model
import time

class ExecCommand(object):

  def __init__(self, args):
    self.args = args

  def run_command(self, label, command):
    if label == self.args.exit_label or label == "exit_application":
      sys.stdout.write("Exit application...")
      sys.exit()
    elif label == self.args.init_label:
      sys.stdout.write("Start hearing...")
      self.start_hearing = time.perf_counter()
    elif not self.args.init_label or time.perf_counter() - self.start_hearing < self.args.init_time:
      sys.stdout.write("Executing...")
      self.start_hearing = time.perf_counter()
      os.system(command)
    elif self.args.init_label and time.perf_counter() - self.start_hearing >= self.args.init_time:
      sys.stdout.write("Hearing time is over. Say init word again.")

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--init_label", help="init label")
  parser.add_argument("--init_time", help="init time", default=10)
  parser.add_argument("--exit_label", help="exit label", default="exit_application")
  model.add_model_flags(parser)
  args = parser.parse_args()
  interpreter = model.make_interpreter("models/" + args.model_file)
  interpreter.allocate_tensors()
  mic = args.mic if args.mic is None else int(args.mic)
  exec_command = ExecCommand(args)
  sys.stdout.write("--------------------\n")
  sys.stdout.write("This script will execute shell commands via voice control.\n")
  sys.stdout.write("--------------------\n")

  model.classify_audio(mic, interpreter,
                       labels_file="config/" + args.labels_file,
                       commands_file="config/commands_exec.txt",
                       dectection_callback=exec_command.run_command,
                       sample_rate_hz=int(args.sample_rate_hz),
                       num_frames_hop=int(args.num_frames_hop))


if __name__ == "__main__":
  main()
