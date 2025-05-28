def some_function():
    pass


try:
    result = some_function()
except ValueError as e:
    print(f"ValueError occurred: {e}")
