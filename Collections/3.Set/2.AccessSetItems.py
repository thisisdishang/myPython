# You cannot access items in a set by referring to an index or a key because set is unindexed and unordered
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword
myset={"MCA","BCA","BTech","MTech"}
for i in myset:
    print(i)

# check specified value is present in a set
print("BCA" in myset)