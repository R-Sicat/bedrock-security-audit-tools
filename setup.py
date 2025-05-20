from setuptools import setup, find_packages

setup(
    name='security_agent',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'zapcli',
        # Add other Python dependencies here
    ],
    entry_points={
        'console_scripts': [
            'security-agent=security_agent.agent:main',
        ],
    },
    author='Rohmer Jay Sicat',
    description='Automated security scanning agent using Lynis, Trivy, and ZAP.',
    url='https://github.com/R-Sicat/bedrock-security-audit-tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
