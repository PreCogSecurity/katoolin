"""Repository manager for Katoolin."""
import os

KALI_REPO_LINES = [
    "# Kali linux repositories | Added by Katoolin\n",
    ("deb http://http.kali.org/kali "
     "kali-rolling main contrib non-free\n"),
    "deb http://repo.kali.org/kali kali-bleeding-edge main\n",
]


def add_repositories(sources_path="/etc/apt/sources.list"):
    """Appends Kali repositories to sources.list."""
    content = "".join(KALI_REPO_LINES)
    with open(sources_path, "a") as f:
        f.write("\n" + content)
    return True


def remove_repositories(sources_path="/etc/apt/sources.list"):
    """Removes Kali repositories from sources.list."""
    if not os.path.exists(sources_path):
        return False
    with open(sources_path, "r") as fin:
        lines = fin.readlines()

    filtered_lines = []
    comment = "# Kali linux repositories | Added by Katoolin"
    for line in lines:
        if line not in KALI_REPO_LINES and line.strip() != comment:
            filtered_lines.append(line)

    with open(sources_path, "w") as fout:
        fout.writelines(filtered_lines)
    return True


def view_repositories(sources_path="/etc/apt/sources.list"):
    """Reads and returns sources.list contents."""
    if not os.path.exists(sources_path):
        return ""
    with open(sources_path, "r") as f:
        return f.read()
