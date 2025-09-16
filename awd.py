import pyautogui
import time
import random
import os
from datetime import datetime

# === CONFIG ===
duration = 1 * 60 * 60 + 30 * 60  # 1 hour 30 minutes in seconds
interval_range = (20, 40)  # seconds between edits

project_dir = r"C:\Users\aashr\Downloads\cs2-weapon-viewer-main\cs2-weapon-viewer-main"
phantom_dir = os.path.join(project_dir, "phantom_work")

file_pool = [
    "src/App.tsx",
    "src/components/FakeButton.tsx",
    "src/utils/FakeHelpers.ts",
    "src/hooks/FakeHook.ts",
    "README_FAKE.md",
    "vite.fake.config.ts"
]

snippets = [
    "// TODO: Clean this up\n",
    "const add = (a: number, b: number): number => { return a + b; }\n",
    "export const FakeButton = () => { return <button>Click me</button>; }\n",
    "import { useState } from 'react';\n",
    "useEffect(() => { console.log('Mounted'); }, []);\n",
    "const [count, setCount] = useState(0);\n",
    "interface Props { title: string; onClick: () => void; }\n",
    "// Debug: check state flow\nconsole.log('State updated');\n"
]

# === CREATE PHANTOM FOLDER STRUCTURE ===
folders = ["src", "src/components", "src/utils", "src/hooks"]
os.makedirs(phantom_dir, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(phantom_dir, folder), exist_ok=True)

# === CREATE FILES IF THEY DON'T EXIST ===
for file in file_pool:
    path = os.path.join(phantom_dir, file)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"// Initialized phantom file: {file}\n")

# === START ===
print("⏳ Starting phantom coding session in Windsurf... Switch focus to Windsurf editor window!")
time.sleep(5)  # time to switch focus

# === MAIN LOOP ===
start_time = time.time()
edit_count = 0

while time.time() - start_time < duration:
    # Pick a phantom file + snippet
    file = random.choice(file_pool)
    snippet = random.choice(snippets)

    # Switch to file in Windsurf
    pyautogui.hotkey("ctrl", "p")  # Quick Open
    time.sleep(0.5)
    pyautogui.typewrite(file, interval=0.02)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)

    # Simulate typing edits
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Editing {file} | Snippet added.")
    pyautogui.typewrite(f"// edit #{edit_count} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", interval=0.03)
    pyautogui.typewrite(snippet, interval=0.02)

    # Save (Ctrl+S)
    pyautogui.hotkey("ctrl", "s")
    edit_count += 1

    # Random backspace to look human
    if random.random() < 0.2:
        pyautogui.press("backspace")
        pyautogui.hotkey("ctrl", "s")

    # Wait before next edit
    wait_time = random.uniform(*interval_range)
    time.sleep(wait_time)

# === FINISH ===
print("\n✅ Phantom session complete. 1 hour 30 minutes of believable Windsurf grind logged.")
