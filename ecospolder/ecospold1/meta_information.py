from administrative_information import AdministrativeInformation
import sys
sys.path.append('../')
from ecospold_base import *
from modeling_and_validation import ModelingAndValidation
from process_information import ProcessInformation


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
        collector=None,
        **kwargs
    ) -> None:
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.processInformation = processInformation
        self.modellingAndValidation = modellingAndValidation
        self.administrativeInformation = administrativeInformation

    def hasContent(self) -> bool:
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
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="MetaInformation",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "MetaInformation":
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
            outfile,
            level,
            already_processed,
            namespaceprefix,
            name="MetaInformation",
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="MetaInformation",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="MetaInformation",
    ):
        pass

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="MetaInformation",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.processInformation is not None:
            self.processInformation.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="processInformation",
                pretty_print=pretty_print,
            )
        if self.modellingAndValidation is not None:
            self.modellingAndValidation.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="modellingAndValidation",
                pretty_print=pretty_print,
            )
        if self.administrativeInformation is not None:
            self.administrativeInformation.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="administrativeInformation",
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
        if nodeName == "processInformation":
            obj = ProcessInformation(parent_object=self)
            obj.build(child_, collector=collector)
            self.processInformation = obj
            obj.original_tagname = "processInformation"
        elif nodeName == "modellingAndValidation":
            obj = ModelingAndValidation(parent_object=self)
            obj.build(child_, collector=collector)
            self.modellingAndValidation = obj
            obj.original_tagname = "modellingAndValidation"
        elif nodeName == "administrativeInformation":
            obj = AdministrativeInformation(parent_object=self)
            obj.build(child_, collector=collector)
            self.administrativeInformation = obj
            obj.original_tagname = "administrativeInformation"


# end class MetaInformation
