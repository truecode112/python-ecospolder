import sys
sys.path.append('../')

from ecospold_base import *

from allocation import Allocation
from exchange import Exchange


class FlowData(EcospoldBase):
    """FlowData -- Contains information about inputs and outputs (to and from nature as well as to and from technosphere) and information about allocation (flows to be allocated, co-products to be allocated to, allocation factors).
    exchange -- comprises all inputs and outputs (both elementary flows and intermediate product flows) registered in a unit process.
    allocation -- comprises all referenceToInputOutput.

    """

    def __init__(
        self,
        exchange=None,
        allocation=None,
        collector=None,
        **kwargs
    ) -> None:
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.exchange = [] if exchange is None else exchange
        self.allocation = [] if allocation is None else allocation

    def hasContent(self) -> bool:
        if self.exchange or self.allocation:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="FlowData",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "FlowData":
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
            outfile, level, already_processed, namespaceprefix, name="FlowData"
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="FlowData",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="FlowData"
    ):
        pass

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="FlowData",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        for exchange_item in self.exchange:
            exchange_item.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="exchange",
                pretty_print=pretty_print,
            )
        for allocation_item in self.allocation:
            allocation_item.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="allocation",
                pretty_print=pretty_print,
            )

    def build(self, node, collector=None):
        self.collector = collector
        if SaveElementTreeNode:
            self.elementtree_node = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName, collector=collector)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        pass

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        if nodeName == "exchange":
            obj = Exchange(parent_object=self)
            obj.build(child_, collector=collector)
            self.exchange.append(obj)
            obj.original_tagname = "exchange"
        elif nodeName == "allocation":
            obj = Allocation(parent_object=self)
            obj.build(child_, collector=collector)
            self.allocation.append(obj)
            obj.original_tagname = "allocation"


# end class FlowData
