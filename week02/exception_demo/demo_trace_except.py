import pretty_errors


def a():
  return b()


def b():
  return c()


def c():
  return d()


def d():
  x = 0
  return 2 / x


a()