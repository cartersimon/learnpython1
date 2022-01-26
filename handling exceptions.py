# try/except/finally, like Java's try/catch
try:
    x = 7 / 0
except Exception as e:  
    # can specify specific exception, or 'Exception' catches all types
    print(e)


try:
    x = 7 / 0
except:  
    # 'Exception' not needed
    print('there was an error')


try:
    x = 7 / 0
except:  
    # 'Exception' not needed
    print('there was an error')
finally:
    # runs no matter what, put cmds to clean up here. For example failed to write to a file, and so here close that file
    print('finally')