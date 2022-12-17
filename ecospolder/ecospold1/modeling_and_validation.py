from ..ecospold_base import *
from representativeness import Representativeness
from source import Source
from validation import Validation


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


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
        anytypeobjs_=None,
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.representativeness = representativeness
        self.representativeness_nsprefix_ = ""
        if source is None:
            self.source = []
        else:
            self.source = source
        self.source_nsprefix_ = ""
        self.validation = validation
        self.validation_nsprefix_ = ""
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ModelingAndValidation
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ModelingAndValidation.subclass:
            return ModelingAndValidation.subclass(*args_, **kwargs_)
        else:
            return ModelingAndValidation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def _hasContent(self):
        if (
            self.representativeness is not None
            or self.source
            or self.validation is not None
            or self.anytypeobjs_
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
        name_="ModelingAndValidation",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ModelingAndValidation")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ModelingAndValidation":
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
            name_="ModelingAndValidation",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ModelingAndValidation",
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
        name_="ModelingAndValidation",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="ModelingAndValidation",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.representativeness is not None:
            namespaceprefix_ = (
                self.representativeness_nsprefix_ + ":"
                if (UseCapturedNS_ and self.representativeness_nsprefix_)
                else ""
            )
            self.representativeness.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="representativeness",
                pretty_print=pretty_print,
            )
        for source_ in self.source:
            namespaceprefix_ = (
                self.source_nsprefix_ + ":"
                if (UseCapturedNS_ and self.source_nsprefix_)
                else ""
            )
            source_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="source",
                pretty_print=pretty_print,
            )
        if self.validation is not None:
            namespaceprefix_ = (
                self.validation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.validation_nsprefix_)
                else ""
            )
            self.validation.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="validation",
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
        if nodeName_ == "representativeness":
            obj_ = Representativeness.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.representativeness = obj_
            obj_.original_tagname_ = "representativeness"
        elif nodeName_ == "source":
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.source.append(obj_)
            obj_.original_tagname_ = "source"
        elif nodeName_ == "validation":
            obj_ = Validation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.validation = obj_
            obj_.original_tagname_ = "validation"
        else:
            content_ = self.gds_build_any(child_, "ModelingAndValidation")
            self.anytypeobjs_.append(content_)


# end class ModelingAndValidation
