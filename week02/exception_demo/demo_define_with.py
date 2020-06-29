class UserOpen():

  def __enter__(self):
    print('open')

  def __exit__(self, type, value, trace):
    print('close')

  def __call__(self):
    print('call')


with UserOpen() as f:
  pass