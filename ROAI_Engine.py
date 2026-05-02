import google.generativeai as genai
import subprocess
import os
import hashlib

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_logic():
    prompt = "Give me a short, complex C++ function with random variable names. ONLY code, no text."
    try:
        response = model.generate_content(prompt)
        return response.text.strip().replace("```cpp", "").replace("```", "")
    except:
        return "void x_null() { int z = 99; }"

def build_master_version(v_num):
    print(f"[*] ROAI Master: Finalizing Version {v_num}...")
    ai_logic = get_ai_logic()
    cpp_file = f"final_v{v_num}.cpp"
    exe_file = f"ROAI_Master_v{v_num}.exe"

    source_code = f"""
#include <windows.h>

{ai_logic}

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrev, LPSTR lpCmd, int nShow) {{
    
    ShellExecute(0, 0, "https://www.google.com", 0, 0, SW_SHOW);
    
    return 0;
}}"""

    with open(cpp_file, "w", encoding="utf-8") as f:
        f.write(source_code)

    try:
        subprocess.run(["g++", cpp_file, "-o", exe_file, "-mwindows", "-lshell32"], check=True)
        print(f"[+] DONE: {exe_file} created successfully.")
        os.remove(cpp_file) 
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    print("--- ROAI MASTER DEPLOYMENT ---")
    for i in range(1, 3):
        build_master_version(i)
    print("--- PROJECT COMPLETE ---")
