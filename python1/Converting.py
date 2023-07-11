print("*** Converting hh.mm.ss to seconds ***")
h, m, s = input("Enter hh mm ss : ").split()
if int(m) < 0 or int(m) >= 60 or int(s) < 0 or int(s) >= 60:
    print(f"mm({m}) is invalid!")
else:
    h = h.zfill(2)
    m = m.zfill(2)
    s = s.zfill(2)
    print(f"{h}:{m}:{s} = {int(h) * 3600 + int(m) * 60 + int(s):,} seconds")