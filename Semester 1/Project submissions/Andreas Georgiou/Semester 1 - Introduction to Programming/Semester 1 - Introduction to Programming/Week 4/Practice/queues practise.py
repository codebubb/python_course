# Queues work on a FIRST IN, FIRST OUT basis. first item to be added to the
# que moves down the que and then gets removed.

waiting_room = ["cust1", "cust2", "cust3"]

waiting_room.insert(0, "cust4")

print waiting_room

waiting_room.pop()

print waiting_room


# James's version below

waiting_room = []
waiting_room.insert(0, "Patient1")
waiting_room.insert(0, "Patient2")
waiting_room.insert(0, "Patient3")
waiting_room.pop()
waiting_room.insert(0, "Patient4")
print waiting_room
