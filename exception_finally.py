def func():
    pass
    return

if __name__ == '__main__':
    try:
        fh = open('../testfile.txt', 'w') # './testfile.txt'
        fh.write("This is exception finally.")
    except Exception as e:  #방어 코드를 넣기 위한 것  (마지막까지 실행되야 한다.)
        pass 
    finally:  # finally은 오류가 생겨도 무조건 지나간다. 
        fh.close()


pass


"""
ghgh

"""
