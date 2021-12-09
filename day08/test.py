a = 'be'
b = 'cgeb'
c = 'cefdb'

# ed is in bedf but ed is not cbgef
# the best way to do this is delede ed in b

if all(ch in c for ch in a):
    print("okay")
    # and all(ch1 in test for ch1 in b)