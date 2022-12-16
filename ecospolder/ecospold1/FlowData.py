from Allocation import TAllocation
from EcoSpold01Base import *
from Exchange import TExchange


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class TFlowData(GeneratedsSuper):
    """TFlowData -- Contains information about inputs and outputs (to and from nature as well as to and from technosphere) and information about allocation (flows to be allocated, co-products to be allocated to, allocation factors).
    exchange -- comprises all inputs and outputs (both elementary flows and intermediate product flows) registered in a unit process.
    allocation -- comprises all referenceToInputOutput.

    """

    def __init__(
        self,
        exchange=None,
        allocation=None,
        anytypeobjs_=None,
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if exchange is None:
            self.exchange = []
        else:
            self.exchange = exchange
        self.exchange_nsprefix_ = None
        if allocation is None:
            self.allocation = []
        else:
            self.allocation = allocation
        self.allocation_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_

    def factory(*args_, **kwargs_):
        return TFlowData(*args_, **kwargs_)

    factory = staticmethod(factory)

    def _hasContent(self):
        if self.exchange or self.allocation or self.anytypeobjs_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="TFlowData",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("TFlowData")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "TFlowData":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="TFlowData"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="TFlowData",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="TFlowData"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="TFlowData",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for exchange_ in self.exchange:
            namespaceprefix_ = (
                self.exchange_nsprefix_ + ":"
                if (UseCapturedNS_ and self.exchange_nsprefix_)
                else ""
            )
            exchange_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="exchange",
                pretty_print=pretty_print,
            )
        for allocation_ in self.allocation:
            namespaceprefix_ = (
                self.allocation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.allocation_nsprefix_)
                else ""
            )
            allocation_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="allocation",
                pretty_print=pretty_print,
            )
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write("\n")

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "exchange":
            obj_ = TExchange.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.exchange.append(obj_)
            obj_.original_tagname_ = "exchange"
        elif nodeName_ == "allocation":
            obj_ = TAllocation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.allocation.append(obj_)
            obj_.original_tagname_ = "allocation"
        else:
            content_ = self.gds_build_any(child_, "TFlowData")
            self.anytypeobjs_.append(content_)


# end class TFlowData
