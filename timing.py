# Syntax: [str|list buttons, int frames=1]
# Positive frames for press, negative frames for hold

universal = {
  'sd': [['hs', 41]], # super dash
  'a1': [[['a1']]], # assist 2
  'a2': [[['a2']]], # assist 2
  'zc1': [[['6', 'a1']]], # z-change 2
  'zc2': [[['6', 'a2']]], # z-change 2
  'sparking': [['lmhs', 46]],
  'vanish': [['mh', 60]],
  '[vanish]': [['mh', -28]], # empty vanish
  'dash': [['6'], ['6', 4]],
  'ad': [['6'], ['6', 6]], # air dash
  'iad': [['9', 7], ['6', 6]], # instant air dash
  'jc': [['8', 5]], # jump cancel neutral
  'jcf': [['9', 5]], # jump cancel forward
  'jcb': [['7', 5]], # jump cancel backward
  'sjf': [['2'], ['9', 5]],
  '[dr]': [['lm', -112]],
}

goku = {
  '5l': [['l', 14]],
  '5ll': [['l', 14], ['l', 20]],
  '5m': [['m', 20]],
  '5mm': [['m', 20], ['m', 21]],
  '5h': [['h', 30]],
  '5h!': [['h', 41]],
  '5s': [['s', 18]],
  '2l': [['2l', 14]],
  '2m': [['2m', 21]],
  '2h': [['2h', 30]],
  '2h!': [['2h', 41]],
  '2s': [['2s', 18]],
  '6m': [['6m', 38]],
  'jl': [['l', 14]],
  'jll': [['l', 14], ['l', 21]],
  'jlll': [['l', 14], ['l', 21], ['l', 27]],
  'jlml': [['l', 14], ['m', 21], ['l', 14]],
  'jlmh': [['l', 14], ['m', 21], ['h', 27]],
  'jmlh': [['m', 21], ['l', 14], ['h', 27]],
  'jm': [['m', 21]],
  'jml': [['m', 21], ['l', 14]],
  'jmh': [['m', 21], ['h', 27]],
  'jmll': [['m', 21], ['l', 14], ['l', 14]],
  'jh': [['h', 27]],
  'jh!': [['h', 40]],
  'j2h': [['2h', 25]],
  'j2h!': [['2h', 36]],
  'js': [['s', 17]],
  'djl': [['9l', 14]],
  'djll': [['9l', 14], ['l', 21]],
  'djlll': [['9l', 14], ['l', 21], ['l', 27]],
  'djm': [['9m', 21]],
  'djh': [['9h', 27]],
  'djs':  [['9s', 18]],
  '214l': [['2'], ['1'], ['4l', 37]],
  '214m': [['2'], ['1'], ['4m', 72]],
  '214m!': [['2'], ['1'], ['4m', 76]],
  '2148m!': [['2'], ['1'], ['4'], ['8', 4], ['m', 76]],
  '236l': [['2'], ['3'], ['6l', 38]],
  '236l!': [['2'], ['3'], ['6l', 50]],
  '236s': [['2'], ['3'], ['6s', 31]],
  '236s[2]': [['2'], ['3'], ['6s'], ['2', -31]],
  '2369[8s]': [['2'], ['3'], ['6'], ['9', 4], ['8s', -31]],
  'j214l': [['2'], ['1'], ['4l', 34]],
  'j214m': [['2'], ['1'], ['4m', 68]],
  'j214m!': [['2'], ['1'], ['4m', 72]],
  'j236l': [['2'], ['3'], ['6l', 34]],
  'j236l!': [['2'], ['3'], ['6l', 46]],
  'j236s': [['2'], ['3'], ['6s', 31]],
  'j236s[2]': [['2'], ['3'], ['6s'], ['2', -29]],
  '236l+m': [['2'], ['3'], ['6lm', 79]],
  '236a1~l+m': [['2'], ['3'], ['6'], [['a1']], ['lm', 153]],
  '236a2~l+m': [['2'], ['3'], ['6'], [['a2']], ['lm', 153]],
  '236l+m[2]': [['2'], ['3'], ['6lm'], ['2', -77]],
  '236h+s': [['2'], ['3'], ['6hs', 106]],
  'j236l+m': [['2'], ['3'], ['6lm', 79]],
  'j236l+m[2]': [['2'], ['3'], ['6lm'], ['2', -79]],
  'j236h+s': [['2'], ['3'], ['6hs', 106]],
  '214l+m': [['2'], ['1'], ['4lm']],
}

trunks = {
  '5m': [['m', 20]],
  '5mm': [['m', 20], ['m', 23]],
  '2m': [['2m', 23]],
  '5h': [['h', 29]],
  '5h!': [['h', 38]],
  '5s': [['s', 23]],
  'jl': [['l', 14]],
  'jm': [['m', 21]],
  'djm': [['9m', 21]],
  'jh': [['h', 28]],
  'js': [['s', 24]],
  'jll': [['l', 14], ['l', 21]],
  'jlll': [['l', 14], ['l', 21], ['l', 28]],
  '236l': [['2'], ['3'], ['6l', 140]],
  '236m': [['2'], ['3'], ['6m', 150]],
  '236s': [['2'], ['3'], ['6s', 31]],
  '214s!': [['2'], ['1'], ['4s', 60]],
  'j214l': [['2'], ['1'], ['4l', 14]],
  '236l+m': [['2'], ['3'], ['6lm', 100]],
  '214l+m': [['2'], ['1'], ['4lm']],
}

broly = {
  '5m': [['m', 20]],
}