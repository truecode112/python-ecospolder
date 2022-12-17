import sys
sys.path.append('../')
from ecospold_base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class DataEntryBy(EcospoldBase):
    """DataEntryBy -- Contains information about the person that entered data in the database or transformed data into the format of the ecoinvent (or any other) quality network.
    person -- ID number for the person that prepared the dataset and enters the dataset into the database. It must correspond to an ID number of a person listed in the respective dataset.
    qualityNetwork -- Indicates a project team that works on the database. The information is used, e.g., for restricting the accessibility of dataset information to one particular quality network. The code used is: 1=ecoinvent

    """

    def __init__(
        self, person=None, qualityNetwork=None, collector=None, **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.person = _cast(int, person)
        self.qualityNetwork = _cast(int, qualityNetwork)

    def validate_TIndexNumber(self, value):
        # Validate type TIndexNumber, a restriction on xsd:int.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, int):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 1:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TIndexNumber'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def _hasContent(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="DataEntryBy",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("DataEntryBy")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "DataEntryBy":
            name = self.original_tagname
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix,
                name,
                namespacedef and " " + namespacedef or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix, name="DataEntryBy"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="DataEntryBy",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="DataEntryBy",
    ):
        if self.person is not None and "person" not in already_processed:
            already_processed.add("person")
            outfile.write(
                ' person="%s"'
                % self.format_integer(self.person, input_name="person")
            )
        if (
            self.qualityNetwork is not None
            and "qualityNetwork" not in already_processed
        ):
            already_processed.add("qualityNetwork")
            outfile.write(
                ' qualityNetwork="%s"'
                % self.format_integer(
                    self.qualityNetwork, input_name="qualityNetwork"
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="DataEntryBy",
        fromsubclass=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, collector=None):
        self.collector = collector
        if SaveElementTreeNode:
            self.elementtree_node = node
        already_processed = set()
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName, collector=collector)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value("person", node)
        if value is not None and "person" not in already_processed:
            already_processed.add("person")
            self.person = self.parse_integer(value, node, "person")
            self.validate_TIndexNumber(self.person)  # validate type TIndexNumber
        value = find_attr_value("qualityNetwork", node)
        if value is not None and "qualityNetwork" not in already_processed:
            already_processed.add("qualityNetwork")
            self.qualityNetwork = self.parse_integer(value, node, "qualityNetwork")

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class DataEntryBy
