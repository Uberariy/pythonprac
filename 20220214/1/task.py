import zlib
import sys
from glob import iglob
from os.path import join

pref = ".git"   # Maybe "../../.git"
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
        kind, size = header.split()
        print(body.decode())