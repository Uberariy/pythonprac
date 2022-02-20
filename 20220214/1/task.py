import zlib
import sys
from glob import iglob
from os.path import join

pref = "../../.git"
if len(sys.argv) == 1:
    branchpath = pref+"/refs/heads/*"
    for objname in iglob(branchpath):
        print(objname.split("/")[-1])
elif len(sys.argv) == 2:
    branchpath = pref+"/refs/heads/"+sys.argv[1]
    with open(branchpath) as objfile:
        filecont = objfile.read()
    commitpath = pref+"/objects/"+filecont[:2]+"/"+filecont[2:-1]

    with open(commitpath, "rb") as objfile:
        fullobj = zlib.decompress(objfile.read())
        header, _, body = fullobj.partition(b'\x00')
        commitcont = body.decode().split()
    treepath = pref+"/objects/"+commitcont[commitcont.index("tree")+1][:2]+"/"+commitcont[commitcont.index("tree")+1][2:]
    
    def shag(treepath, depth):
        if depth == 1:
            print("|-=-=-[TREE: "+commitcont[commitcont.index("tree")+1]+"]-=-=-|")
        with open(treepath, "rb") as objfile:
            fullobj = zlib.decompress(objfile.read())
            header, _, body = fullobj.partition(b'\x00')

            while body:
                treehdr, _, tail = body.partition(b'\x00')
                gitid, body = tail[:20], tail[20:]
                if treehdr.split()[0] == b'40000':
                    print("="*(depth+2)+"#\ "+f"{str(treehdr.split()[1])[2:-1]}, {gitid.hex()}")
                    shag(pref+"/objects/"+gitid.hex()[:2]+"/"+gitid.hex()[2:], depth+1)
                else:
                    print("-"*(depth-1)+"| "+f"{str(treehdr.split()[1])[2:-1]}, {gitid.hex()}")
            print("="*(depth+1)+"#/")

    shag(treepath, 1)