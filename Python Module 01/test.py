class Plant:
  def __init__(self):
    self._height = 10

p = Plant()

# Real attribute name: _height
print(p._height)
p._height = 99
print(p._height)
# Convention only — Python
# does NOT block direct access