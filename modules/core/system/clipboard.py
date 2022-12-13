import clipboard


def copy(
        to_copy,
):
    return clipboard.set(to_copy)


def get(

):
    return clipboard.get()


x = get()
print(x)