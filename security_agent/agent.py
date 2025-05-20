import subprocess

def run_lynis():
    subprocess.run(['sudo', 'lynis', 'audit', 'system', '--quick'], check=True)

def run_trivy():
    subprocess.run(['trivy', 'fs', '--severity', 'HIGH,CRITICAL', '--format', 'json', '-o', 'trivy-report.json', '.'], check=True)

def run_zap():
    subprocess.run(['zap-cli', 'start'], check=True)
    subprocess.run(['zap-cli', 'open-url', 'http://localhost'], check=True)
    subprocess.run(['zap-cli', 'spider', 'http://localhost'], check=True)
    subprocess.run(['zap-cli', 'active-scan', 'http://localhost'], check=True)
    subprocess.run(['zap-cli', 'report', '-o', 'zap-report.html', '-f', 'html'], check=True)
    subprocess.run(['zap-cli', 'shutdown'], check=True)

def main():
    run_lynis()
    run_trivy()
    run_zap()
