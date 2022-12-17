import sys
sys.path.append('../')

from ecospold_base import *

from allocation import Allocation
from exchange import Exchange


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class FlowData(EcospoldBase):
    """FlowData -- Contains information about inputs and outputs (to and from nature as well as to and from technosphere) and information about allocation (flows to be allocated, co-products to be allocated to, allocation factors).
    exchange -- comprises all inputs and outputs (both elementary flows and intermediate product flows) registered in a unit process.
    allocation -- comprises all referenceToInputOutput.

    """

    def __init__(
        self,
        exchange=None,
        allocation=None,
        gds_collector=None,
        **kwargs
    ):
        self.gds_collector = gds_collector
        self.gds_elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        if exchange is None:
            self.exchange = []
        else:
            self.exchange = exchange
        if allocation is None:
            self.allocation = []
        else:
            self.allocation = allocation

    def _hasContent(self):
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
        imported_ns_def = GenerateDSNamespaceDefs.get("FlowData")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
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
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix, name="FlowData"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
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

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="FlowData"
    ):
        pass

    def _exportChildren(
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
        pass

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, gds_collector=None
    ):
        if nodeName == "exchange":
            obj = Exchange(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.exchange.append(obj)
            obj.original_tagname = "exchange"
        elif nodeName == "allocation":
            obj = Allocation(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.allocation.append(obj)
            obj.original_tagname = "allocation"


# end class FlowData
