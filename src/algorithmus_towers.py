def umsetz(disks, start, target):
    if disks == 0:
        return
    auxiliary = 3 - start - target
    umsetz(disks - 1, start, auxiliary)
    move(start, target)
    umsetz(disks - 1, auxiliary, target)


def move(start, target):
    pass
