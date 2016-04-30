import os

rootDir = '.'

def find_files(x):
    for dirName,subdirList, fileList in os.walk(rootDir,topdown=False):
        #print dirName
        for fname in fileList:
            path,ext = os.path.splitext(fname)
            if ext == x:
                print '[{}] {}'.format(dirName,fname)
                with open(x.split('.')[1]+'.txt','a') as outfile:
                    outfile.write(fname+'\n')


def markdown_images(x):
    for dirName,subdirList, fileList in os.walk(rootDir,topdown=False):
        #print dirName
        for fname in fileList:
            path,ext = os.path.splitext(fname)
            if ext == x:
                print '[{}] {}'.format(dirName,fname)
                with open(x.split('.')[1]+'.md','a') as outfile:
                    outfile.write("![]({})\n".format(dirName+'/'+fname))

                    
# Implementation
#find_files('.png')
markdown_images('.png')



# Extra Stuff
def simple_walk():
    #root prints out directories only from what you specified
    #dirs prints out sub-directories from root
    #files prints out all files from root and directories
    for root, dirs, files in os.walk("."):
        print root
        print dirs
        print files
