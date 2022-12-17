from data_entry_by import DataEntryBy
from data_generator_and_publication import DataGeneratorAndPublication
import sys
sys.path.append('../')
from ecospold_base import *
from person import Person


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class AdministrativeInformation(EcospoldBase):

    """AdministrativeInformation -- Contains information about the person that compiled and entered the dataset in the database and about kind of publication and the accessibility of the dataset.
    dataEntryBy -- Contains information about the person and the quality network the person belongs to.
    dataGeneratorAndPublication -- Contains information about the generator of the dataset in the database, whether the dataset has been published (and how) and about copyright and the accessibility of the dataset (public or restricted to ETH domain, ECOINVENT, or a particular institute of ECOINVENT.
    person -- Contains a list of persons with their addresses.

    """

    ##############################################
    ### AdministrativeInformation Constructor ###
    ##############################################

    def __init__(
        self,
        dataEntryBy=None,
        dataGeneratorAndPublication=None,
        person=None,
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.dataEntryBy = dataEntryBy
        self.dataEntryBy_nsprefix_ = ""
        self.dataGeneratorAndPublication = dataGeneratorAndPublication
        self.dataGeneratorAndPublication_nsprefix_ = ""
        if person is None:
            self.person = []
        else:
            self.person = person
        self.person_nsprefix_ = ""

    def _hasContent(self):
        if (
            self.dataEntryBy is not None
            or self.dataGeneratorAndPublication is not None
            or self.person
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
        name_="AdministrativeInformation",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("AdministrativeInformation")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "AdministrativeInformation":
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
            name_="AdministrativeInformation",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="AdministrativeInformation",
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
        name_="AdministrativeInformation",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="AdministrativeInformation",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.dataEntryBy is not None:
            namespaceprefix_ = (
                self.dataEntryBy_nsprefix_ + ":"
                if (UseCapturedNS_ and self.dataEntryBy_nsprefix_)
                else ""
            )
            self.dataEntryBy.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="dataEntryBy",
                pretty_print=pretty_print,
            )
        if self.dataGeneratorAndPublication is not None:
            namespaceprefix_ = (
                self.dataGeneratorAndPublication_nsprefix_ + ":"
                if (UseCapturedNS_ and self.dataGeneratorAndPublication_nsprefix_)
                else ""
            )
            self.dataGeneratorAndPublication.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="dataGeneratorAndPublication",
                pretty_print=pretty_print,
            )
        for person_ in self.person:
            namespaceprefix_ = (
                self.person_nsprefix_ + ":"
                if (UseCapturedNS_ and self.person_nsprefix_)
                else ""
            )
            person_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="person",
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
        if nodeName_ == "dataEntryBy":
            obj_ = DataEntryBy(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataEntryBy = obj_
            obj_.original_tagname_ = "dataEntryBy"
        elif nodeName_ == "dataGeneratorAndPublication":
            obj_ = DataGeneratorAndPublication(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataGeneratorAndPublication = obj_
            obj_.original_tagname_ = "dataGeneratorAndPublication"
        elif nodeName_ == "person":
            obj_ = Person(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.person.append(obj_)
            obj_.original_tagname_ = "person"



# end class AdministrativeInformation
