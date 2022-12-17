from dataset import Dataset
import sys
sys.path.append('../')
from ecospold_base import *


class EcoSpold(EcospoldBase):
    """EcoSpold -- the data (exchange) format of the ECOINVENT quality network.
    dataset -- a dataset describes LCI related information of a unit process or a terminated system comprising metaInformation (description of the process) and flowData (quantified inputs and outputs and allocation factors, if any).

    """

    def __init__(
        self,
        validationId=None,
        validationStatus=None,
        dataset=None,
        collector=None,
        **kwargs
    ) -> None:
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.validationId = cast_value_with_type(int, validationId)
        self.validationStatus = cast_value_with_type(None, validationStatus)
        self.dataset = [] if dataset is None else dataset

    def hasContent(self) -> bool:
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
    ) -> None:
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
        self.exportAttributes(
            outfile, level, already_processed, namespaceprefix, name="EcoSpold"
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
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

    def exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="EcoSpold"
    ) -> None:
        if self.validationId is not None and "validationId" not in already_processed:
            already_processed.add("validationId")
            outfile.write(
                ' validationId="%s"'
                % self.format_integer(self.validationId, input_name="validationId")
            )
        if (
            self.validationStatus is not None
            and "validationStatus" not in already_processed
        ):
            already_processed.add("validationStatus")
            outfile.write(
                " validationStatus=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.validationStatus),
                            input_name="validationStatus",
                        )
                    ),
                )
            )

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="EcoSpold",
        fromsubclass=False,
        pretty_print=True,
    ) -> None:
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

    def build(self, node, collector=None) -> None:
        self.collector = collector
        if SaveElementTreeNode:
            self.elementtree_node = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName, collector=collector)

    def buildAttributes(self, node, attrs, already_processed) -> None:
        value = find_attr_value("validationId", node)
        if value is not None and "validationId" not in already_processed:
            already_processed.add("validationId")
            self.validationId = self.parse_integer(value, node, "validationId")
        value = find_attr_value("validationStatus", node)
        if value is not None and "validationStatus" not in already_processed:
            already_processed.add("validationStatus")
            self.validationStatus = value

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ) -> None:
        if nodeName == "dataset":
            obj = Dataset(parent_object=self)
            obj.build(child_, collector=collector)
            self.dataset.append(obj)
            obj.original_tagname = "dataset"


# end class EcoSpold
