import pytest
import mkdocs_pluglet_file_include


def test_basic_usage():
    assert (
        mkdocs_pluglet_file_include._find_content(
            ["# ANCHOR: test", "content", "# ANCHOR_END: test"], anchor_id="test"
        )
        == "content"
    )


def test_basic_multi_line_usage():
    assert (
        mkdocs_pluglet_file_include._find_content(
            ["# ANCHOR: test", "content", "more", "# ANCHOR_END: test"],
            anchor_id="test",
        )
        == "content\nmore"
    )


def test_basic_multi_anchor():
    assert mkdocs_pluglet_file_include._find_content(
        [
            "# ANCHOR: test",
            "# ANCHOR: another_test",
            "content",
            "# ANCHOR_END: another_test",
            "outside_content",
            "# ANCHOR_END: test",
        ],
        anchor_id="test",
    ) == "\n".join(["content", "outside_content"])


def test_stripping_lines():
    assert (
        mkdocs_pluglet_file_include._find_content(
            ["# ANCHOR: test", "  content", "# ANCHOR_END: test"],
            anchor_id="test",
            remove_prefix="  ",
        )
        == "content"
    )


def test_stripping_mutilple_lines():
    assert mkdocs_pluglet_file_include._find_content(
        [
            "# ANCHOR: test",
            "  indented: yes",
            "    content: true",
            "# ANCHOR_END: test",
        ],
        anchor_id="test",
        remove_prefix="  ",
    ) == "\n".join(["indented: yes", "  content: true"])
