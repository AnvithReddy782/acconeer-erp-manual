# scripts/push_to_github.py
import subprocess
import os

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate('protocol=https\nhost=github.com\nusername=AnvithReddy782\n\n')

token = ''
for line in out.splitlines():
    if line.startswith('password='):
        token = line.split('=', 1)[1]

if not token:
    print('Error: Token not found from git credential manager')
    exit(1)

auth_url = f'https://x-access-token:{token}@github.com/AnvithReddy782/acconeer-erp-manual.git'
repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

subprocess.run(['git', '-C', repo_dir, 'remote', 'set-url', 'origin', auth_url], check=True)
print('Authenticated remote URL set. Pushing to GitHub...')

res = subprocess.run(['git', '-C', repo_dir, 'push', 'origin', 'main'], capture_output=True, text=True)
print('Push stdout:', res.stdout)
print('Push stderr:', res.stderr)
print('Return code:', res.returncode)

# Sanitize remote URL back to clean HTTPS
safe_url = 'https://github.com/AnvithReddy782/acconeer-erp-manual.git'
subprocess.run(['git', '-C', repo_dir, 'remote', 'set-url', 'origin', safe_url], check=True)
print('Sanitized origin URL back to standard HTTPS.')
