import requests  # You might need to install this: pip install requests
import sys

SERVER_URL = "http://127.0.0.1:8081"

def start_driver():
    print(f"🏎️  Sarathi (Driver) initialized.")
    print(f"📡 Connecting to Setu at {SERVER_URL}...")
    print("------------------------------------------------")
    
    while True:
        try:
            command = input("sarathi > ").strip().lower()
        except KeyboardInterrupt:
            print("\n🛑 Emergency Stop.")
            break

        if command == "exit" or command == "quit":
            print("👋 Disconnecting...")
            break
            
        elif command == "status":
            try:
                response = requests.get(f"{SERVER_URL}/")
                data = response.json()
                print(f"✅ System: {data.get('system')}")
                print(f"📊 Status: {data.get('status')}")
                print(f"📦 Objects: {data.get('total_objects')}")
            except Exception as e:
                print(f"❌ Error connecting to Setu: {e}")

        elif command == "log":
            try:
                response = requests.get(f"{SERVER_URL}/log")
                data = response.json()
                print("📜 --- SERVER INVENTORY ---")
                for obj in data.get('objects', []):
                    print(f"   🔹 {obj}")
                print("---------------------------")
            except Exception as e:
                print(f"❌ Error fetching log: {e}")

        elif command == "":
            pass
        else:
            print(f"⚠️  Unknown command: '{command}'")

if __name__ == "__main__":
    start_driver()