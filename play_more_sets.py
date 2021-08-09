ma = [1, 3, 5, 10]
mb = [3, 10, 9]

sma = set(ma)
smb = set(mb)

# get the common set of marks scored in both the divisions - (3, 10)
print(sma & smb)

# get the union of marks scored in both the divisions - (1, 3, 5, 10, 9)
print(sma | smb)

# get the marks that were exclusively scored in division a - (1, 5)
print(sma - smb)

# get the marks that were exclusively scored in division b - (9)
print(smb - sma)

# get the marks that were exclusively scored in division a or division b; but not in both
print(sma ^ smb)