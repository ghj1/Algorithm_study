# def fun_callback():
#     try:
        

# def fun_call():
#     pass
#     return

if __name__ == '__main__':
   try:
      f = open('./testfile.txt', 'r')
      length = len(f.read())
      f.close()
      print(length)
   except Exception as e:
      pass
