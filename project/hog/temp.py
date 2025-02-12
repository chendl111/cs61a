from hog import announce_highest
f0 = announce_highest(1) # Only announce Player 1 score gains
f1 = f0(12, 0)
f2 = f1(12, 9)
f3 = f2(20, 9)
f4 = f3(20, 30)
f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
f6 = f5(21, 47)
f7 = f6(21, 77)