# combomake
Python script that generates an AutoHotkey script to perform a combo in Dragon Ball FighterZ.

Reads modified numpad notation from a user-specified file and converts it to AHK commands, eg:

    goku 5m 2m 214l

becomes:

    Send {u down}
    DllCall("Sleep", UInt, 16.67)
    Send {u up}
    DllCall("Sleep", UInt, 316.73)
    Send {s down}{u down}
    DllCall("Sleep", UInt, 16.67)
    Send {s up}{u up}
    DllCall("Sleep", UInt, 266.72)
    Send {s down}
    DllCall("Sleep", UInt, 16.67)
    Send {s up}
    DllCall("Sleep", UInt, 16.67)
    Send {s down}{a down}
    DllCall("Sleep", UInt, 16.67)
    Send {s up}{a up}
    DllCall("Sleep", UInt, 16.67)
    Send {a down}{j down}
    DllCall("Sleep", UInt, 16.67)
    Send {a up}{j up}

The first word (one or more non-whitespace characters followed by whitespace) of the input notation must be a recognized character's name. If you want to switch characters mid-combo, they must be specified with 'c:' immediately followed by that character's name, eg:

    goku 2h zc1 c:vegeta jlll

This is because move timing is read from 'timing.py' to calculate the necessary delays specific to each characters' moves.

Additional custom delay timing can be specified in the input notation with 'd:' immediately followed by an integer value, eg:

    2m d:5 5m = press 5M five frames later than usual

Custom delays can be negative integers as well, eg:

    js d:-3 5m = press 5M three frames earlier than usual

Custom button combinations and timing can also be specified with a list of at least one value inside curly braces with no whitespace in between. The first value must be a string which represents one or more simultaneous button presses, and the second (optional) value must be an integer representing the number of frames until the next input. A positive integer means press and release followed by a delay of that many frames, while a negative integer means hold for that many frames followed by a release, eg:

    {'2s',-50} = hold 2S for 50 frames

 If no second value is present, the delay is assumed to be 1 frame.

 The character is assumed to be facing to the right (P1 side) by default, but a mid-combo side switch can be signified with the notation 'ss', eg:

    2m 5m jc jlll vanish ss 236l+m

Key mappings can be modified in 'keys.py'.