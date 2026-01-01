import os
import time
from . import data  

def write_tree(directory="."):
    entries = []
    
    for entry in sorted(os.listdir(directory)):
        if entry.startswith(".") or entry == "__pycache__" or entry == "lib":
            continue
            
        full_path = os.path.join(directory, entry)
        
        if os.path.isfile(full_path):
            with open(full_path, 'rb') as f:
                content = f.read()
            # Ask data layer to save it
            sha = data.hash_object(content, "blob", write=True)
            entries.append(f"blob {sha} {entry}")
            
        elif os.path.isdir(full_path):
            sha = write_tree(full_path)
            entries.append(f"tree {sha} {entry}")
    
    tree_content = "\n".join(entries).encode()
    return data.hash_object(tree_content, "tree", write=True)

def commit(tree_sha, message, parent=None):
    timestamp = int(time.time())
    author = f"Anshu <anshu@chronos> {timestamp} +0000"
    
    lines = []
    lines.append(f"tree {tree_sha}")
    if parent:
        lines.append(f"parent {parent}")  # <--- The Link to the Past
    
    lines.append(f"author {author}")
    lines.append(f"committer {author}")
    lines.append("")
    lines.append(message)
    lines.append("")
    
    content = "\n".join(lines).encode()
    return data.hash_object(content, "commit", write=True)