text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find('0')
host = text[atpos:]
f = float(host)
print(f)
