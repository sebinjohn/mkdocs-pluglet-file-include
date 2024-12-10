# mkdocs-pluglet-file-include

> Include a file with anchor in mkdocs

This is a
[pluglet](https://github.com/fralau/mkdocs_macros_plugin#using-pluglets) which
defines a macro to include file contents using jinja2 template in
[mkdocs](https://www.mkdocs.org/)

In order for this to work, [mkdocs macros
plugin](https://github.com/fralau/mkdocs_macros_plugin) must be installed and
defined.

## Why it exists

I saw a really useful feature in `mdbook`
[here](https://rust-lang.github.io/mdBook/format/mdbook.html#including-portions-of-a-file)
which essentially let you include a portion of the file into your web page.

A similar functionality is provided by
[this](https://github.com/mondeja/mkdocs-include-markdown-plugin) plugin. But it
didn't seem to remove anchors tags when there are multiple of them defined in a
file.

This pluglet bridges that gap.

## Setup

> This pluglet requires python 3.10. Support for other versions may be added.

```
pip install mkdocs-macros-plugin
pip install mkdocs-pluglet-file-include
```

update your `mkdocs.yaml` file with

```yaml
plugins:
  - search
  - macros:
      modules:
        - mkdocs_pluglet_file_include
```

## Usage

To include a portion of a file use

```
{{include_with_anchor('<file-name>', '<anchor name>'[, strip_prefix='<optional prefix>'])}}
```

> [!TIP]
> `strip_prefix` is an optional parameter that can strip a prefix from each line of the resulting content. This is
> useful if, for example, you have indented content that you wish to present unindented.

## Example

File with sections defined (use the ANCHOR and ANCHOR_END keyword)

```
$ cat inc.txt
ANCHOR: begin
1. Item 1
2. Item 2
# ANCHOR: a
3. Item 3
4. Item 4
# ANCHOR_END: a
# ANCHOR_END: begin
```

File that includes contenets between anchors.

```
cat included.txt

Example: Include selected lines.

{{include_with_anchor('inc.txt', 'a')}}

Example: Include all lines.

{{include_with_anchor('inc.txt', 'begin')}}
```

After running mkdocs build, the resulting page would look like

```
Example: Include selected lines.

3. Item 3
4. Item 4

Example: Include all lines.

1. Item 1
2. Item 2
3. Item 3
4. Item 4
```
