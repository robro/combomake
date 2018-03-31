#!/usr/bin/env python

# Make an AutoHotkey script that performs a combo in Dragon Ball FighterZ.
#
# Reads modified numpad notation from a user-specified file
# and converts it to AHK commands, eg:
#
#   goku
#   5m 2m 214l
#
# becomes
#
#   Send {u down}
#   DllCall("Sleep", UInt, 16.67)
#   Send {u up}
#   DllCall("Sleep", UInt, 316.73)
#   Send {s down}{u down}
#   DllCall("Sleep", UInt, 16.67)
#   Send {s up}{u up}
#   DllCall("Sleep", UInt, 266.72)
#   Send {s down}
#   DllCall("Sleep", UInt, 16.67)
#   Send {s up}
#   DllCall("Sleep", UInt, 16.67)
#   Send {s down}{a down}
#   DllCall("Sleep", UInt, 16.67)
#   Send {s up}{a up}
#   DllCall("Sleep", UInt, 16.67)
#   Send {a down}{j down}
#   DllCall("Sleep", UInt, 16.67)
#   Send {a up}{j up}
#
# This script uses timing info from 'timing.py' to calculate
# the delays specific to each characters' moves.
#
# Custom delay timing can also be specified in the combo notation, eg:
#
#   2m d:5 5m (5M is pressed 5 frames later)
#
# Custom delays can be negative as well, eg:
#
#   js d:-3 5m (5M is pressed 3 frames earlier)
#
# Key mapping can be changed in 'keys.py'.

import os
import re
import sys
import argparse

import keys
import timing


def keyDown(keys):
  key_string = ''

  for key in keys:
    key_string += '{%s down}' % key

  return 'Send %s\n' % key_string


def keyUp(keys):
  key_string = ''

  for key in keys:
    key_string += '{%s up}' % key

  return 'Send %s\n' % key_string


def delay(frames):
  frame_time = 16.67
  delay_frames = frames * frame_time

  return 'DllCall("Sleep", UInt, %s)\n' % delay_frames


def buffer(string):
  prebutton_count = len(re.findall(r'\d(?=\d)', string))

  return prebutton_count * -2


def switch(direction):
  switch_map = {
    '1': '3',
    '2': '2',
    '3': '1',
    '4': '6',
    '5': '5',
    '6': '4',
    '7': '9',
    '8': '8',
    '9': '7',
  }

  return switch_map[direction]


def getTiming(string, character):
  if string in getattr(timing, 'universal'):
    return getattr(timing, 'universal')[string]
  
  if string in getattr(timing, character):
    return getattr(timing, character)[string]

  return []


def getTimingStr(command, is_switched=False):
  buttons = command[0]
  hold_frames = 1
  delay_frames = 1
  key_str = ''

  if len(command) > 1:
    if command[1] > 1:
      hold_frames = command[1]
    elif command[1] < -1:
      delay_frames = command[1]
    else:
      print 'Error: Invalid timing value:', command[1]
      sys.exit(1)

  for button in buttons:
    if is_switched and button.isdigit():
      button = switch(button)

    for key in keys.mapping[button]:
      key_str += key

  return '*{0}_{1}^{0}_{2}'.format(key_str, hold_frames, delay_frames)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  args = parser.parse_args()

  combo_filename = os.path.abspath(args.filename)

  with open(combo_filename, 'r') as combo_file:
    combo_strings = combo_file.read().lower().split()

  character = combo_strings.pop(0)
  if not getattr(timing, character, False):
    print 'Error: Unknown character:', character
    sys.exit(1)

  print 'Combo:', ' '.join(combo_strings)

  timing_str = ''
  is_switched = False

  for string in combo_strings:
    # side switch
    if string == 'ss':
      is_switched = False if is_switched else True

    # custom delay
    elif string.startswith('d:'):
      timing_str += '_' + string[2:]

    # change character
    elif string.startswith('c:'):
      character = string[2:]
      if not getattr(timing, character, False):
        print 'Error: Unknown character:', character
        sys.exit(1)

    # custom button(s) press or hold
    # syntax: {str|list buttons, int hold_frames, int delay_frames} (no spaces)
    # example: {'2s',1,50}
    elif string.startswith('{') and string.endswith('}'):
      command = eval('[%s]' % string[1:-1])
      timing_str += getTimingStr(command, is_switched)

    else:
      timing_data = getTiming(string, character)

      if not timing_data:
        print 'Error: Unrecognized string:', string
        sys.exit(1)

      if timing_str and buffer(string):
        timing_str += '_%s' % buffer(string)

      for command in timing_data:
        timing_str += getTimingStr(command, is_switched)

  # Replace final delay with end symbol
  timing_str = timing_str[:timing_str.rfind('_')] + ':'

  print 'Timing:', timing_str, '\n'

  hotkey_lines = []
  input_str = ''
  input_mode = ''
  delay_frames = 0

  # Use timing string to build list of ahk commands
  for char in timing_str:
    if char in ['*', '^', '_', ':']:
      if input_mode == 'down':
        hotkey_lines.append(keyDown(input_str))

      elif input_mode == 'up':
        hotkey_lines.append(keyUp(input_str))

      elif input_mode == 'delay':
        delay_frames += int(input_str)

        if char != '_':
          if delay_frames < 0:
            print 'Error: Invalid delay:', delay_frames
            sys.exit(1)

          if delay_frames > 0:
            hotkey_lines.append(delay(delay_frames))
            delay_frames = 0

      input_str = ''

    if char == ':':
      break
    if char == '*':
      input_mode = 'down'
      continue
    if char == '^':
      input_mode = 'up'
      continue
    if char == '_':
      input_mode = 'delay'
      continue
  
    input_str += char

  ext_index = combo_filename.rfind('.')

  hotkey_filename = combo_filename if ext_index == -1 else combo_filename[:ext_index]
  hotkey_filename += '.ahk'

  template_filename = 'template'

  with open(template_filename, 'r') as template_file:
    template_lines = template_file.readlines()

  insert_line = 20

  with open(hotkey_filename, 'w') as hotkey_file:
    hotkey_file.writelines(template_lines[:insert_line])
    hotkey_file.writelines(hotkey_lines)
    hotkey_file.writelines(template_lines[insert_line:])

  print 'AutoHotkey file saved to:', hotkey_filename

  return 0

if __name__ == "__main__":
    main()