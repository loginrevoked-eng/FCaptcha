import httpx
import sys

BASE_URL = "http://127.0.0.1:2300"

def test_flow():
    with httpx.Client(base_url=BASE_URL) as client:
        # Check if server is alive first
        try:
            client.get("/")
        except httpx.ConnectError:
            print(f"❌ Error: Server not found at {BASE_URL}. Is it running?")
            sys.exit(1)

        print("🚀 Starting API Tests...\n" + "-"*30)

        # 1. Root Check
        print("🔍 Testing Root (Initial)...", end=" ", flush=True)
        res = client.get("/")
        assert "Fuck you Mate" in res.text
        print("✅")

        # 2. Text Upload
        print("📤 Testing File Upload (Valid)...", end=" ", flush=True)
        files = {'file': ('test.txt', b"Hello World", 'text/plain')}
        res = client.post("/upload", files=files)
        assert res.status_code == 200
        print("✅")

        # 3. Binary Upload Denial
        print("🚫 Testing Binary Block...", end=" ", flush=True)
        bad_files = {'file': ('bad.bin', b'\x80\x81', 'application/octet-stream')}
        res = client.post("/upload", files=bad_files)
        assert "only accept text files" in res.json()["msg"]
        print("✅")

        # 4. File List
        print("📋 Testing File List Retrieval...", end=" ", flush=True)
        res = client.get("/see_file_list")
        assert "test.txt" in res.json()
        print("✅")

        # 5. Serve File
        print("📄 Testing File Download...", end=" ", flush=True)
        res = client.get("/see_files_uploaded/test.txt")
        assert res.text == "Hello World"
        print("✅")

        # 6. 404 Fallback
        print("❓ Testing Missing File...", end=" ", flush=True)
        res = client.get("/see_files_uploaded/ghost.txt")
        assert "File not found" in res.text
        print("✅")

        # 7. Report Submission
        print("📊 Testing Report Posting...", end=" ", flush=True)
        res = client.post("/report", json={"error": "debug"})
        assert res.json()["success"] is True
        print("✅")

        # 8. Root State Change
        print("🔄 Testing Root (Post-Report)...", end=" ", flush=True)
        res = client.get("/")
        assert "debug" in res.text
        print("✅")

        print("-"*30 + "\n🎉 All tests passed successfully!")

if __name__ == "__main__":
    test_flow()
