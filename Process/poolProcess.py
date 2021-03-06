#coding:utf-8

'Process testing '

from multiprocessing import Pool,Process

import os, time, random

def long_time_task( name ):
    print( 'Run task  %s ( %s ) ...'%( name, os.getpid() ) )

    start = time.time()
    time.sleep( random.random()*3 )
    end = time.time()
    print( 'Task %s run %0.2f seconds ...' %( name, (end-start) ) )

if __name__=='__main__':
    print( 'Parents process %s....' % os.getpid() )
    p = Pool(4)
    for i in range(5):
        p.apply_async( long_time_task, args = ( i, ) )

    print( 'Waitting for all subprocess done ....' )
    p.close()
    p.join()
    print( 'All subprocess done....' )
