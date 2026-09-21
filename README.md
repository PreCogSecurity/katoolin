![katoolin](https://cloud.githubusercontent.com/assets/8742190/9415562/83397aae-4840-11e5-8f72-28dfffcc70a9.png)
# katoolin

Automatically install and manage Kali Linux tools on Debian/Ubuntu-based systems. Maintained and hardened by PreCog Security.

## Features
- Add Kali Linux repositories & GPG keys
- Remove Kali Linux repositories cleanly
- View sources.list contents
- Install Kali Linux tools and categories
- Fully modular Python 3 architecture with automated test suite

## Requirements
- Python >= 3.8
- Debian / Ubuntu / Kali Linux (tested on Ubuntu)
- Root / sudo privileges for repository management and tool installation

## Architecture
Katoolin is structured into modular components:
- `katoolin/cli.py`: Interactive command-line interface and menu system.
- `katoolin/repo_manager.py`: Safe parsing and management of `/etc/apt/sources.list`.
- `katoolin/installer.py`: Package installation and execution helper.
- `tests/`: Automated unit tests (`pytest`).

## Installation & Usage
```bash
sudo su
git clone https://github.com/PreCogSecurity/katoolin.git
cd katoolin
pip install .
sudo katoolin
```

## Running Tests
```bash
pip install -r requirements-dev.txt
pytest -v
```

## Warning
Before updating your system, please remove all Kali Linux repositories to avoid package conflicts or dependency issues.

## License
Distributed under the MIT License. See `LICENSE` for details.
