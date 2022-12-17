import sys
sys.path.append('../')
from ecospold_base import *
from representativeness import Representativeness
from source import Source
from validation import Validation

class ModelingAndValidation(EcospoldBase):
    """ModelingAndValidation -- Contains metaInformation about how unit processes are modelled and about the review/validation of the dataset.
    representativeness -- Contains information about the representativeness of the unit process data (meta information and flow data).
    source -- Lists and describes the sources where the dataset is documented (final report in the ECOINVENT quality network series).
    validation -- Contains information about the reviewers' comments on the dataset content.

    """

    def __init__(
        self,
        representativeness=None,
        source=None,
        validation=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.representativeness = representativeness
        if source is None:
            self.source = []
        else:
            self.source = source
        self.validation = validation

    def hasContent(self):
        if (
            self.representativeness is not None
            or self.source
            or self.validation is not None
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
        name="ModelingAndValidation",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "ModelingAndValidation":
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
            name="ModelingAndValidation",
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="ModelingAndValidation",
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
        name="ModelingAndValidation",
    ):
        pass

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="ModelingAndValidation",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.representativeness is not None:
            self.representativeness.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="representativeness",
                pretty_print=pretty_print,
            )
        for source_item in self.source:
            source_item.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="source",
                pretty_print=pretty_print,
            )
        if self.validation is not None:
            self.validation.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="validation",
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
        if nodeName == "representativeness":
            obj = Representativeness(parent_object=self)
            obj.build(child_, collector=collector)
            self.representativeness = obj
            obj.original_tagname = "representativeness"
        elif nodeName == "source":
            obj = Source(parent_object=self)
            obj.build(child_, collector=collector)
            self.source.append(obj)
            obj.original_tagname = "source"
        elif nodeName == "validation":
            obj = Validation(parent_object=self)
            obj.build(child_, collector=collector)
            self.validation = obj
            obj.original_tagname = "validation"


# end class ModelingAndValidation
