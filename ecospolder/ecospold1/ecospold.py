from dataset import Dataset
import sys
sys.path.append('../')
from ecospold_base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class EcoSpold(EcospoldBase):
    """EcoSpold -- the data (exchange) format of the ECOINVENT quality network.
    dataset -- a dataset describes LCI related information of a unit process or a terminated system comprising metaInformation (description of the process) and flowData (quantified inputs and outputs and allocation factors, if any).

    """

    def __init__(
        self,
        validationId=None,
        validationStatus=None,
        dataset=None,
        gds_collector=None,
        **kwargs
    ):
        self.gds_collector = gds_collector
        self.gds_elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.validationId = _cast(int, validationId)
        self.validationStatus = _cast(None, validationStatus)
        if dataset is None:
            self.dataset = []
        else:
            self.dataset = dataset

    def _hasContent(self):
        if self.dataset:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="EcoSpold",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("EcoSpold")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "EcoSpold":
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
            outfile, level, already_processed, namespaceprefix, name="EcoSpold"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="EcoSpold",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="EcoSpold"
    ):
        if self.validationId is not None and "validationId" not in already_processed:
            already_processed.add("validationId")
            outfile.write(
                ' validationId="%s"'
                % self.gds_format_integer(self.validationId, input_name="validationId")
            )
        if (
            self.validationStatus is not None
            and "validationStatus" not in already_processed
        ):
            already_processed.add("validationStatus")
            outfile.write(
                " validationStatus=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.validationStatus),
                            input_name="validationStatus",
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="EcoSpold",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        for dataset_item in self.dataset:
            dataset_item.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="dataset",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector=None):
        self.gds_collector = gds_collector
        if SaveElementTreeNode:
            self.gds_elementtree_node = node
        already_processed = set()
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName, gds_collector=gds_collector)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value("validationId", node)
        if value is not None and "validationId" not in already_processed:
            already_processed.add("validationId")
            self.validationId = self.gds_parse_integer(value, node, "validationId")
        value = find_attr_value("validationStatus", node)
        if value is not None and "validationStatus" not in already_processed:
            already_processed.add("validationStatus")
            self.validationStatus = value

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, gds_collector=None
    ):
        if nodeName == "dataset":
            obj = Dataset(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.dataset.append(obj)
            obj.original_tagname = "dataset"


# end class EcoSpold
