import re

# https://github.com/rust-lang/mdBook/blob/master/src/utils/string.rs#L27-L28
ANCHOR_START = r"ANCHOR:\s*(?P<anchor_name>[\w_-]+)"
ANCHOR_END = r"ANCHOR_END:\s*(?P<anchor_name>[\w_-]+)"

def define_env(env):
    @env.macro
    def include_with_anchor(fname, anchor_id):
        with open(fname) as f:
            data = f.read()

        anchor_found = False
        saved_content = []

        for l in data.split('\n'):
            match re.search(ANCHOR_START, l):
                case None:
                    match re.search(ANCHOR_END, l):
                        case None:
                            if anchor_found:
                                saved_content.append(l)
                        case x:
                            anchor = m.group(0)
                            anchor_value = anchor.split(': ')[1]
                            if anchor_value == anchor_id:
                                break
                case m: 
                    anchor = m.group(0)
                    anchor_value = anchor.split(': ')[1]
                    if anchor_value == anchor_id:
                        anchor_found = True
        return '\n'.join(saved_content)
