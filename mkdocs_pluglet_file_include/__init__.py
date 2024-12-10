import re

# https://github.com/rust-lang/mdBook/blob/master/src/utils/string.rs#L27-L28
ANCHOR_START = r"ANCHOR:\s*(?P<anchor_name>[\w_-]+)"
ANCHOR_END = r"ANCHOR_END:\s*(?P<anchor_name>[\w_-]+)"


def _find_content(file_lines, anchor_id, remove_prefix=None):
    anchor_found = False
    saved_content = []

    for l in file_lines:
        match re.search(ANCHOR_START, l):
            case None:
                match re.search(ANCHOR_END, l):
                    case None:
                        if anchor_found:
                            saved_content.append(
                                l.removeprefix(remove_prefix) if remove_prefix else l
                            )
                    case x:
                        anchor = m.group(0)
                        anchor_value = anchor.split(": ")[1]
                        if anchor_value == anchor_id:
                            break
            case m:
                anchor = m.group(0)
                anchor_value = anchor.split(": ")[1]
                if anchor_value == anchor_id:
                    anchor_found = True
    return "\n".join(saved_content)


def define_env(env):
    @env.macro
    def include_with_anchor(fname, anchor_id, remove_prefix=None):
        with open(fname) as f:
            data = f.read()

        return _find_content(data.split("\n"), anchor_id, remove_prefix)
