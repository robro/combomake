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
  'siad': [['2'], ['9', 7], ['6', 6]], # super instant air dash
  'jc': [['8', 5]], # jump cancel neutral
  'jcf': [['9', 5]], # jump cancel forward
  'jcb': [['7', 5]], # jump cancel backward
  'sj': [['2'], ['8', 5]], # super jump neutral
  'sjf': [['2'], ['9', 5]], # super jump forward
  'sjb': [['2'], ['7', 5]], # super jump backward
  'dr': [['lm', 90]], # dragon rush
  '[dr]': [['lm', -112]], # dragon rush (hold)
}

cell = {
  '5l': [['l', 14]],
  '5m': [['m', 20]],
  '5h!': [['h', 39]],
  '5[h]!': [['h', -54]],
  '6h': [['6h', 27]],
  '2m': [['2m', 23]],
  '2h!': [['2h', 41]],
  'jl': [['l', 14]],
  'jm': [['m', 20]],
  'djm': [['9m', 20]],
  'jh': [['h', 27]],
  'djh': [['9h', 27]],
  'js': [['s', 23]],
  'jll': [['l', 14], ['l', 20]],
  'jlll': [['l', 14], ['l', 20], ['l', 27]],
  'jml': [['m', 20], ['l', 14]],
  'j2m': [['2m', 44]],
  'j2h!': [['2h', 36]],
  'djlll': [['9l', 14], ['l', 20], ['l', 27]],
  'j236l': [['2'], ['3'], ['6l', 19]],
  'j236m': [['2'], ['3'], ['6m', 19]],
  'j214m': [['2'], ['1'], ['4m', 68]],
  'j214h': [['2'], ['1'], ['4h', 68]],
  '214s': [['2'], ['1'], ['4s', 132]],
  '236s': [['2'], ['3'], ['6s', 31]],
  '236l+m': [['2'], ['3'], ['6lm', 79]],
  '214l+m': [['2'], ['1'], ['4lm']],
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

bardock = {
  '5l': [['l', 17]],
  '5ll': [['l', 17], ['l', 22]],
  '5l(w)l': [['l', 8], ['l', 22]],
  '5lll': [['l', 17], ['l', 22], ['l', 38]],
  '5m': [['m', 23]],
  '5mm': [['m', 23], ['m', 21]],
  '5h': [['h', 31]],
  '5h!': [['h', 39]],
  '5s': [['s', 18]],
  '2l': [['2l', 15]],
  '2m': [['2m', 21]],
  '2h!': [['2h', 35]],
  '6m': [['6m', 55]],
  'jl': [['l', 14]],
  'jll': [['l', 14], ['l', 19]],
  'jll(2)': [['l', 14], ['l', 41]],
  'jlm': [['l', 14], ['m', 19]],
  'jlll': [['l', 14], ['l', 19], ['l', 27]],
  'jm': [['m', 19]],
  'jm(2)': [['m', 41]],
  'jh': [['h', 27]],
  'js': [['s', 17]],
  'j2h': [['2h', 26]],
  'j2h!': [['2h', 37]],
  'jmm': [['m', 19], ['m', 22]],
  'jmml': [['m', 19], ['m', 22], ['l', 14]],
  'jm(2)l': [['m', 41], ['l', 14]],
  'djll': [['9l', 14], ['l', 19]],
  'djll(2)': [['9l', 14], ['l', 41]],
  'djm': [['9m', 19]],
  'djmm': [['9m', 19], ['m', 22]],
  'djm(2)': [['9m', 41]],
  '214l': [['2'], ['1'], ['4l', 61]],
  '214m!': [['2'], ['1'], ['4m', 75]],
  '236l': [['2'], ['3'], ['6l', 22]],
  '236h': [['2'], ['3'], ['6h', 33]],
  '236h!': [['2'], ['3'], ['6h', 33], ['h', 56]],
  '236l+a1': [['2'], ['3'], ['6'], [['l', 'a1'], 22]],
  'j214l': [['2'], ['1'], ['4l', 41]],
  'j214m': [['2'], ['1'], ['4m', 49]],
  'j214m!': [['2'], ['1'], ['4m', 58]],
  'j236l': [['2'], ['3'], ['6l', 22]],
  'j236m!': [['2'], ['3'], ['6m', 67]],
  'j236m': [['2'], ['3'], ['6m', 28]],
  'j236h': [['2'], ['3'], ['6h', 33]],
  '236m': [['2'], ['3'], ['6m', 27]],
  '236m!': [['2'], ['3'], ['6m', 56]],
  '236s': [['2'], ['3'], ['6s', 94]],
  '236s!': [['2'], ['3'], ['6s', 124]],
  '236[s]!': [['2'], ['3'], ['6s', -35]],
  '236a1[s]!': [['2'], ['3'], ['6'], [['a1']], ['s', -35]],
  '2369m!': [['2'], ['3'], ['6'], ['9', 4], ['m', 40]],
  '236l+m': [['2'], ['3'], ['6lm', 64]],
  '236h+s': [['2'], ['3'], ['6hs', 115]],
  '236h+s+a1': [['2'], ['3'], ['6'], [['h','s','a1'], 114]],
  '236a1~h+s': [['2'], ['3'], ['6'], [['a1']], ['hs', 114]],
  '236a2~h+s': [['2'], ['3'], ['6'], [['a2']], ['hs', 114]],
  '214l+m': [['2'], ['1'], ['4lm']],
}

zamasu = {
  '5l': [['l', 15]],
  '5ll': [['l', 15], ['l', 20]],
  '5m': [['m', 23]],
  '5mm': [['m', 23], ['m', 23]],
  '5h': [['h', 31]],
  '5h!': [['h', 40]],
  '5s': [['s', 19]],
  '2l': [['2l', 16]],
  '2m': [['2m', 23]],
  '2mm': [['2m', 23], ['m', 23]],
  '2h!': [['2h', 40]],
  '6m': [['6m', 53]],
  'jl': [['l', 15]],
  'djl': [['9l', 15]],
  'jll': [['l', 15], ['l', 21]],
  'jlm': [['l', 15], ['m', 21]],
  'jlh': [['l', 15], ['h', 27]],
  'djll': [['9l', 15], ['l', 21]],
  'jlll': [['l', 15], ['l', 21], ['l', 27]],
  'djlll': [['9l', 15], ['l', 21], ['l', 27]],
  'jlml': [['l', 15], ['m', 21], ['l', 15]],
  'jlmh': [['l', 15], ['m', 21], ['h', 27]],
  'djlmh': [['9l', 15], ['m', 21], ['h', 27]],
  'jmlh': [['m', 21], ['l', 15], ['h', 27]],
  'jm': [['m', 21]],
  'djm': [['9m', 21]],
  'jml': [['m', 21], ['l', 15]],
  'djml': [['9m', 21], ['l', 15]],
  'jmh': [['m', 21], ['h', 27]],
  'jmll': [['m', 21], ['l', 15], ['l', 15]],
  'djmlh': [['9m', 21], ['l', 15], ['h', 27]],
  'jh': [['h', 27]],
  'j2h': [['2h', 32]],
  'j2h!': [['2h', 43]],
  'js': [['s', 20]],
  'j2s': [['2s', -20]],
  'js(2)': [['s', -30]],
  'j2s(2)': [['2s', -30]],
  'js(3)': [['s', -40]],
  'j2s(3)': [['2s', -40]],
  '236l': [['2'], ['3'], ['6l', 29]],
  'j236l': [['2'], ['3'], ['6l', 29]],
  '236m': [['2'], ['3'], ['6m', 25]],
  '236m!': [['2'], ['3'], ['6m', 40]],
  '236[s]': [['2'], ['3'], ['6s', -45]],
  '236s': [['2'], ['3'], ['6s', 33]],
  '236s!': [['2'], ['3'], ['6s', 42]],
  '214l': [['2'], ['1'], ['4l', 35]],
  'fly': [['s', 16]],
  '236l+m': [['2'], ['3'], ['6lm', 64]],
  '236h+s': [['2'], ['3'], ['6hs', 64]],
}