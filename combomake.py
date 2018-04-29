#!/usr/bin/env python
import os
import re
import sys
import argparse

import keys
import timing


def keyDown(match_obj):
  keys = match_obj.group(0)[1:]
  key_string = ''

  for key in keys:
    key_string += '{%s down}' % key

  return 'Send %s\n' % key_string


def keyUp(match_obj):
  keys = match_obj.group(0)[1:]
  key_string = ''

  for key in keys:
    key_string += '{%s up}' % key

  return 'Send %s\n' % key_string


def delay(match_obj):
  frames = int(match_obj.group(0)[1:])
  return 'DllCall("Sleep", UInt, %s)\n' % (frames * 16.67)


def buffer(timing_data):
  prebutton_count = 0

  for command in timing_data:
    if len(command) == 1 and len(command[0]) == 1:
      prebutton_count += 1

  return prebutton_count * -2


def switch(direction):
  num_map = {
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
  if direction in num_map:
    return num_map[direction]

  return -1


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
      delay_frames = command[1] - 1
    elif command[1] < -1:
      hold_frames = -command[1] - 1
    else:
      print 'Error: Invalid timing value:', command[1]
      sys.exit(1)

  for button in buttons:
    if is_switched and button.isdigit():
      button = switch(button)
      if button == -1:
        print 'Error: Unrecognized input:', button
        sys.exit(1)

    for key in keys.mapping[button]:
      key_str += key

  return '*{0}_{1}^{0}_{2}'.format(key_str, hold_frames, delay_frames)


def newTiming(timing_str, frames):
  delay_index = timing_str.rfind('_')
  last_delay = int(timing_str[delay_index+1:])

  if frames < 0 and last_delay == 1:
    # Try modifying the hold value instead
    hold_index = timing_str[:delay_index].rfind('_')
    release_index = timing_str.rfind('^')
    last_hold = int(timing_str[hold_index+1:release_index])

    new_hold = last_hold + frames

    if new_hold < 1:
      print timing_str
      print 'Error: Invalid delay:', new_hold
      sys.exit(1)

    return timing_str[:hold_index+1] + str(new_hold) + timing_str[release_index:]

  new_delay = last_delay + frames

  if new_delay < 1:
    print timing_str
    print 'Error: Invalid delay:', new_delay
    sys.exit(1)

  return timing_str[:delay_index+1] + str(new_delay)


def main():
  # Set-up argument parser
  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  args = parser.parse_args()

  combo_filename = os.path.abspath(args.filename)

  # Store combo strings into list
  with open(combo_filename, 'r') as combo_file:
    combo_strings = combo_file.read().lower().split()

  print 'Combo:', ' '.join(combo_strings)

  # First string should be the starting character
  character = combo_strings.pop(0)
  if not getattr(timing, character, False):
    print 'Error: Unknown character:', character
    sys.exit(1)

  timing_str = ''
  is_switched = False

  for string in combo_strings:
    # Side switch
    if string == 'ss':
      is_switched = False if is_switched else True

    # Change character
    elif string.startswith('c:'):
      character = string[2:]
      if not getattr(timing, character, False):
        print 'Error: Unknown character:', character
        sys.exit(1)

    # Custom delay
    elif string.startswith('d:'):
      timing_str = newTiming(timing_str, int(string[2:]))

    # Custom button(s) press or hold
    # Syntax: {str|list buttons, int frames=1} (no whitespace)
    elif string.startswith('{') and string.endswith('}'):
      command = eval('[%s]' % string[1:-1])
      timing_str += getTimingStr(command, is_switched)

    # Standard timing search in timing file
    else:
      timing_data = getTiming(string, character)

      if not timing_data:
        print 'Error: Unrecognized string:', string
        sys.exit(1)

      buffer_frames = buffer(timing_data)

      if timing_str and buffer_frames:
          timing_str = newTiming(timing_str, buffer_frames)
          
      for command in timing_data:
        timing_str += getTimingStr(command, is_switched)

  # Truncate final delay
  timing_str = timing_str[:timing_str.rfind('_')]

  print 'Timing:', timing_str, '\n'

  # Replace timing notation with AHK commands
  hotkey_str = timing_str
  hotkey_str = re.sub(r'\*[^_]+', keyDown, hotkey_str)
  hotkey_str = re.sub(r'\^[^_]+', keyUp, hotkey_str)
  hotkey_str = re.sub(r'_\d+', delay, hotkey_str)

  ext_index = combo_filename.rfind('.')

  hotkey_filename = combo_filename if ext_index == -1 else combo_filename[:ext_index]
  hotkey_filename += '.ahk'

  template_filename = 'template'

  with open(template_filename, 'r') as template_file:
    template_lines = template_file.readlines()

  insert_line = 20

  # Write AHK file
  with open(hotkey_filename, 'w') as hotkey_file:
    hotkey_file.writelines(template_lines[:insert_line])
    hotkey_file.write(hotkey_str)
    hotkey_file.writelines(template_lines[insert_line:])

  print 'AutoHotkey file saved to:', hotkey_filename

  return 0

if __name__ == "__main__":
    main()