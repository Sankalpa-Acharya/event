import string
import random

mapper = {
    "C": "JNV4",
    "t": "rOl0",
    "e": "y2Am",
    "I": "UsZJ",
    "R": "XaNY",
    "K": "RrsO",
    "n": "VR0T",
    "M": "WXZq",
    "x": "O8fI",
    "Z": "B2kg",
    "U": "13sW",
    "z": "wuAv",
    "l": "hvRh",
    "q": "dBan",
    "G": "MpnY",
    "E": "yiDQ",
    "V": "gUuB",
    "B": "REKc",
    "w": "LP5Q",
    "d": "9idG",
    "p": "qImb",
    "h": "64d2",
    "i": "FdNq",
    "o": "ofMA",
    "A": "bwfV",
    "y": "QCy8",
    "F": "RboZ",
    "W": "Th4C",
    "P": "OneK",
    "S": "uGfs",
    "s": "XZIc",
    "k": "gQrT",
    "Y": "3rHL",
    "J": "MuZ1",
    "j": "XMHM",
    "X": "MV3b",
    "Q": "nYse",
    "r": "ni7W",
    "c": "eDMi",
    "H": "Cs76",
    "T": "4XBP",
    "O": "mUfu",
    "b": "dCjG",
    "L": "8ztW",
    "m": "icvC",
    "a": "cY1S",
    "u": "ZLMt",
    "N": "da2d",
    "f": "y1Si",
    "v": "ngsQ",
    "D": "WpS8",
    "g": "IJCY",
    " ":"1212",
    "{":"fff",
    "}":"sss"
}


reverse_mapper = {
    "JNV4": "C",
    "rOl0": "t",
    "y2Am": "e",
    "UsZJ": "I",
    "XaNY": "R",
    "RrsO": "K",
    "VR0T": "n",
    "WXZq": "M",
    "O8fI": "x",
    "B2kg": "Z",
    "13sW": "U",
    "wuAv": "z",
    "hvRh": "l",
    "dBan": "q",
    "MpnY": "G",
    "yiDQ": "E",
    "gUuB": "V",
    "REKc": "B",
    "LP5Q": "w",
    "9idG": "d",
    "qImb": "p",
    "64d2": "h",
    "FdNq": "i",
    "ofMA": "o",
    "bwfV": "A",
    "QCy8": "y",
    "RboZ": "F",
    "Th4C": "W",
    "OneK": "P",
    "uGfs": "S",
    "XZIc": "s",
    "gQrT": "k",
    "3rHL": "Y",
    "MuZ1": "J",
    "XMHM": "j",
    "MV3b": "X",
    "nYse": "Q",
    "ni7W": "r",
    "eDMi": "c",
    "Cs76": "H",
    "4XBP": "T",
    "mUfu": "O",
    "dCjG": "b",
    "8ztW": "L",
    "icvC": "m",
    "cY1S": "a",
    "ZLMt": "u",
    "da2d": "N",
    "y1Si": "f",
    "ngsQ": "v",
    "WpS8": "D",
    "IJCY": "g",
    "1212":" ",
    "fff":"{",
    "sss":"}"
}



def encoder(msg):
    message = ''
    letters = [*msg]
    for i in letters:
        if mapper.get(i) is None:
            message+="*"+" "
        else:
            message+=str(mapper.get(i))+" "
    return message


def decoder(msg):
    message = ''
    letters = msg.split(' ')
    for i in letters:
        if reverse_mapper.get(i) is None:
            message+="*"+" "
        else:    message += reverse_mapper.get(i)+" "
    return message

