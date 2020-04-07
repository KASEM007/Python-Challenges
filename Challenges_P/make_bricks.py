# make_bricks
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks
# (5 inches each). Return True if it is possible to make the goal
# by choosing from the given bricks. This is a little harder than
# it looks and can be done without any loops.


# def make_bricks(small, big, goal):
#     big = big * 5
#     if small == goal or big == goal:
#         return True
#     elif small + big >= goal or big - small >= goal:
#         return True
#     else:
#         return False


################## Another Answer ##################################

# Try first to use as many big bricks as possible, then complete with
# the small ones. Note that this works because the size of the big
# ones is a multiple of the size of the small ones, you would need
# another approach if the sizes were for example 2 and 5.


def make_bricks(small, big, goal):
    max_big = goal // 5  # max number of big we can use
    nb_big = min(big, max_big)  # big ones we really use
    return small >= goal - 5 * nb_big  # True if we have enough small ones to complete


print(make_bricks(3, 1, 8))  # → True
print(make_bricks(3, 1, 9))  # → False
print(make_bricks(3, 2, 10))  # → True
print(make_bricks(1, 4, 12))  # → False
print(make_bricks(2, 1000000, 100003))  # → False
