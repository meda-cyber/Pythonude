

lessons = ["Why Python Programming", "Data Types and Operators",
           "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield element, count
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(lesson, i))


# chunker
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))
