# Python3 code to demonstrate
# swap of key and value

# initializing dictionary
old_dict = {
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
    "g": "IJCY"
}


new_dict = dict([(value, key) for key, value in old_dict.items()])

# Printing original dictionary

mapper = {}

# Printing new dictionary after swapping keys and values
print ("Dictionary after swapping is : ")
print("keys: values")
for i in new_dict:
	mapper[i] = new_dict[i]


print(mapper)