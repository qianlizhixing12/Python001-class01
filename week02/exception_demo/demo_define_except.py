class UserException(Exception):

  def __init__(self, msg):
    super().__init__(self, msg)
    self.msg = msg

  def __str__(self):
    return self.msg


try:
  x = input('输入用户id:')
  if not x.isdigit():
    raise UserException('输入用户格式错误')
except (UserException, Exception) as e:
  print(e)