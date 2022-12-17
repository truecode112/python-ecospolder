import sys
sys.path.append('../')
from ecospold_base import *

try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
import datetime as datetime_

from ecospold import EcoSpold

from lxml import etree as etre

ClassesMapping = {}


USAGE_TEXT = """
Usage: python EcoSpold01Process.py <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = tag_pattern.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = ClassesMapping.get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    """Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    """
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = " ".join(
        ['xmlns:{}="{}"'.format(prefix, uri) for prefix, uri in nsmap.items()]
    )
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    collector = CollectorClass()
    parser = None
    doc = parsexml(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    rootTag = "ecospold"
    rootClass = EcoSpold
    rootObj = EcoSpold()
    rootObj.build(rootNode, collector=collector)

    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name=rootTag, namespacedef=namespacedefs, pretty_print=True
        )
    if print_warnings and len(collector.get_messages()) > 0:
        separator = ("-" * 50) + "\n"
        sys.stderr.write(separator)
        sys.stderr.write(
            "----- Warnings -- count: {} -----\n".format(
                len(collector.get_messages()),
            )
        )
        collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == "__main__":
    main()
