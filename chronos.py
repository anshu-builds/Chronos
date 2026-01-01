import sys
import os
from lib import data, base

def parse_commit(sha):
    type_, content = data.get_object(sha)
    if type_ != "commit":
        raise ValueError(f"Object {sha} is not a commit!")
    
    text = content.decode()
    lines = text.split("\n")
    
    parent = None
    message = ""
    
    for line in lines:
        if line.startswith("parent "):
            parent = line.split(" ")[1]
        elif not line.startswith(("tree ", "author ", "committer ")):
            message += line.strip()
            
    print(f"🔸 Commit: {sha}")
    print(f"   Message: {message}\n")
    
    return parent

def main():
    if len(sys.argv) < 2:
        print("Usage: chronos <command>")
        return

    command = sys.argv[1]
    
    if command == "init":
        if data.init():
            print(f"✨ Initialized Chronos in {os.getcwd()}/.chronos")
        else:
            print("⚠️ Already initialized.")

    elif command == "hash-object":
        filename = sys.argv[2]
        with open(filename, 'rb') as f:
            content = f.read()
        sha = data.hash_object(content, write=True)
        print(f"🔑 ID: {sha}")

    elif command == "cat-file":
        sha = sys.argv[2]
        type_, content = data.get_object(sha)
        if content:
            print(f"Type: {type_}")
            print(content.decode())
        else:
            print("❌ Object not found.")

    elif command == "write-tree":
        sha = base.write_tree()
        print(f"🌳 Root Tree: {sha}")

    elif command == "commit":
        tree_sha = sys.argv[2]
        message = sys.argv[3]
        sha = base.commit(tree_sha, message)
        print(f"🚀 Commit: {sha}")
    
    elif command == "commit":
        tree_sha = sys.argv[2]
        message = sys.argv[3]
        parent = sys.argv[4] if len(sys.argv) > 4 else None
        
        sha = base.commit(tree_sha, message, parent)
        print(f"🚀 Commit: {sha}")

    elif command == "log":
        sha = sys.argv[2]
        print("📜 History Log:")
        print("=================")
        
        while sha:
            sha = parse_commit(sha)

if __name__ == "__main__":
    main()