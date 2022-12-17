from administrative_information import AdministrativeInformation
import sys
sys.path.append('../')
from ecospold_base import *
from modeling_and_validation import ModelingAndValidation
from process_information import ProcessInformation


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class MetaInformation(EcospoldBase):
    """MetaInformation -- Contains information about the process (its name, (functional) unit, classification, technology, geography, time, etc.), about modelling assumptions and validation details and about dataset administration (version number, kind of dataset, language).
    processInformation -- Contains content-related metainformation for the unit process.
    modellingAndValidation -- Contains metainformation about how unit processes are modelled and about the review/validation of the dataset.
    administrativeInformation -- Contains the administrative information about the dataset at issue: type of dataset (unit process, elementary flow, impact category, multi-output process) timestamp, version and internalVersion number as well as language and localLanguage code.

    """

    def __init__(
        self,
        processInformation=None,
        modellingAndValidation=None,
        administrativeInformation=None,
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.processInformation = processInformation
        self.processInformation_nsprefix_ = ""
        self.modellingAndValidation = modellingAndValidation
        self.modellingAndValidation_nsprefix_ = ""
        self.administrativeInformation = administrativeInformation
        self.administrativeInformation_nsprefix_ = ""

    def _hasContent(self):
        if (
            self.processInformation is not None
            or self.modellingAndValidation is not None
            or self.administrativeInformation is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="MetaInformation",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("MetaInformation")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "MetaInformation":
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
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="MetaInformation",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="MetaInformation",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="MetaInformation",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="MetaInformation",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.processInformation is not None:
            namespaceprefix_ = (
                self.processInformation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.processInformation_nsprefix_)
                else ""
            )
            self.processInformation.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="processInformation",
                pretty_print=pretty_print,
            )
        if self.modellingAndValidation is not None:
            namespaceprefix_ = (
                self.modellingAndValidation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.modellingAndValidation_nsprefix_)
                else ""
            )
            self.modellingAndValidation.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="modellingAndValidation",
                pretty_print=pretty_print,
            )
        if self.administrativeInformation is not None:
            namespaceprefix_ = (
                self.administrativeInformation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.administrativeInformation_nsprefix_)
                else ""
            )
            self.administrativeInformation.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="administrativeInformation",
                pretty_print=pretty_print,
            )

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
        if nodeName_ == "processInformation":
            obj_ = ProcessInformation(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.processInformation = obj_
            obj_.original_tagname_ = "processInformation"
        elif nodeName_ == "modellingAndValidation":
            obj_ = ModelingAndValidation(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.modellingAndValidation = obj_
            obj_.original_tagname_ = "modellingAndValidation"
        elif nodeName_ == "administrativeInformation":
            obj_ = AdministrativeInformation(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.administrativeInformation = obj_
            obj_.original_tagname_ = "administrativeInformation"


# end class MetaInformation
