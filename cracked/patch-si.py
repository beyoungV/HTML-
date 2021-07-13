#source insight Python补丁

#coding: utf-8
import argparse


AUTHOR_TAG = "[Po->] "
PATCH_OFFSET = 0x1159F0
PATCH_VALUES = b'\xB8\x01\x00\x00\x00\xC3'
PATCH_FILE_PATH = r'C:\Users\Po\Desktop\sourceinsight4_test.exe'


def debug_info( msg, *args, **kwargs ):
    print( AUTHOR_TAG+msg, *args, **kwargs )


def patch_si4( si4_path ):
    debug_info("Begin patch file...")
    with open(si4_path, "r+b") as f:
        f.seek( PATCH_OFFSET, 0 )
        f.write( PATCH_VALUES )
        f.close()
        debug_info("Patch success!")




if __name__ == "__main__":   
    parser = argparse.ArgumentParser()
    parser.add_argument( '-f', '--si4file', metavar="<si4's abs path>" )
    args = parser.parse_args()


    if args.si4file:
        si4_path = args.si4file
    else:
        exit("Please specify sourceinsight4.exe's absolute path!") 


  patch_si4( si4_path )
