"""
Solutions to exam tasks for module 4.
"""
import concurrent.futures as future
from time import perf_counter as toc

from PIL import Image
import os
import sys

# A9
def matrix(x,n):
    """Method that returns a list of lists (with contents of each row of M),
    using a list comprehension"""
    '''
    list = []
    for i in range(len(x)):
        list.append([x[i]**j for j in range(n)])
    '''

    return [[x[i]**j for j in range(n)] for i in range(len(x))]

# A10
def dice(n):
    """Method thats simulates a broken dice. Do not modify."""
    from random import choice
    return [choice([1,2,3,4,5,5]) for _ in range(n)]

def dice_average():
    n = 10000
    times = 20
    """Method that runs dice(n), with n=100000, twenty times in parallel.
    Then, compute the average of all the throws, and return that value."""
    result = 0
    with future.ProcessPoolExecutor() as ex:
        for i in range(times):
            pro = ex.submit(dice,n)
            res = pro.result()
            for r in res:
                result += r
    print(result/(times*n))
# B4


def create_tn(path):
    im = Image.open(path)
    size = im.size
    im.thumbnail((size[0] // 8, size[1] // 8))
    im.save("thumb_" + path)
    im.show()
def thumbnail():
    """Method that creates thumbnails of all .png and .jpg images in 
    current directory, and saves them in a directory called 'thumb' 
    (created if it does not exist). Excution should be done in parallel."""
    filelist = os.listdir('C:/Users/Max/PycharmProjects/prog2/tenta_2021_10')
    for file in filelist[:]:  # filelist[:] makes a copy of filelist.
        if not (file.endswith(".png") or file.endswith(".jpg")) or file.startswith("thumb_") :
            filelist.remove(file)
    s = toc()
    with future.ProcessPoolExecutor() as ex:
        for path in filelist:
            ex.submit(create_tn, path)
    e = toc()
    print(f"{e-s}s")


#-------------------------------
def main():
    print('Test of A9 ')
    x=[5, 1.5, 3]
    print(matrix(x,3))
    print(matrix(x,4))
    print('Test of A10 ')
    print(dice_average())
    print('Test of B4 ')
    thumbnail()

if __name__ == "__main__":
    main()