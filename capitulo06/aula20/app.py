import subprocess

cmd = ["ping", "127.0.0.1", "-c", "4"]
proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf_8")

print(proc)
print(proc.args)
print(proc.stderr)
print(proc.stdout)
print(proc.returncode)
