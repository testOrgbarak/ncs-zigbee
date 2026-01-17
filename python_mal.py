#!/usr/bin/env python
#name run.py
import os

def main():
  print("----hello from file-----")

  os.system("""
  echo "-------------poc_hello--------------" >&2
  """)