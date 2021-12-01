import argparse

args = argparse.ArgumentParser()

args.add_argument('-x', '--xVal', required=True) # argument가 이런 형식으로 되어야 한다는 것을 선언만 한 것이다. 
# args.add_argument('-y', '--yVal', required=False) 

argvar = vars(args.parse_args())

pass #print 쓰면 안된다.
