import os
import hashlib
import zlib

def init():
    repo_path = ".chronos"
    if os.path.exists(repo_path):
        return False
    os.mkdir(repo_path)
    os.mkdir(os.path.join(repo_path, "objects"))
    return True

def hash_object(data, type_="blob", write=False):
  
    header = f"{type_} {len(data)}\0".encode()
    store_data = header + data
    
    sha1 = hashlib.sha1(store_data).hexdigest()
    
    if write:
        zlib_content = zlib.compress(store_data)
        folder = os.path.join(".chronos", "objects", sha1[:2])
        filepath = os.path.join(folder, sha1[2:])
        
        if not os.path.exists(folder):
            os.mkdir(folder)
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                f.write(zlib_content)
                
    return sha1

def get_object(sha1):

    path = os.path.join(".chronos", "objects", sha1[:2], sha1[2:])
    if not os.path.isfile(path):
        return None, None
        
    with open(path, 'rb') as f:
        compressed = f.read()
        
    full_data = zlib.decompress(compressed)
    null_index = full_data.find(b'\x00')
    
    header = full_data[:null_index].decode()
    type_ = header.split(" ")[0]
    
    content = full_data[null_index + 1:]
    
    return type_, content