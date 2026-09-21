"""Unit tests for Katoolin core functionality."""
import pytest
from katoolin import repo_manager, installer


def test_add_repositories(tmp_path):
    sources_file = tmp_path / "sources.list"
    sources_file.write_text("deb http://archive.ubuntu.com/ubuntu focal main\n")

    repo_manager.add_repositories(str(sources_file))
    content = sources_file.read_text()

    assert "kali-rolling" in content
    assert "kali-bleeding-edge" in content


def test_remove_repositories(tmp_path):
    sources_file = tmp_path / "sources.list"
    initial_content = (
        "deb http://archive.ubuntu.com/ubuntu focal main\n"
        "# Kali linux repositories | Added by Katoolin\n"
        "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"
        "deb http://repo.kali.org/kali kali-bleeding-edge main\n"
    )
    sources_file.write_text(initial_content)

    repo_manager.remove_repositories(str(sources_file))
    content = sources_file.read_text()

    assert "kali-rolling" not in content
    assert "kali-bleeding-edge" not in content
    assert "archive.ubuntu.com" in content


def test_view_repositories(tmp_path):
    sources_file = tmp_path / "sources.list"
    sources_file.write_text("deb http://test.repo/kali main\n")

    content = repo_manager.view_repositories(str(sources_file))
    assert "test.repo" in content


def test_installer_validation():
    with pytest.raises(ValueError):
        installer.install_package("")
    with pytest.raises(ValueError):
        installer.install_package(None)
