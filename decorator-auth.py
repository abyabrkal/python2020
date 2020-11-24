# Create an @authenticated decorator that only allows the function 
#  to run is user1 has valid set to TRUE
user1 = {
  'name': 'Sorra',
  'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
      return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
  print('Message has been sent')


# The message will be sent if the user is validated/authenticated.
# Below function is passed through a HOC function and additional logic is applied 
message_friends(user1)
