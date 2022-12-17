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
        gds_collector=None,
        **kwargs
    ):
        self.gds_collector = gds_collector
        self.gds_elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.dataEntryBy = dataEntryBy
        self.dataGeneratorAndPublication = dataGeneratorAndPublication
        if person is None:
            self.person = []
        else:
            self.person = person

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
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="AdministrativeInformation",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("AdministrativeInformation")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "AdministrativeInformation":
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
            outfile,
            level,
            already_processed,
            namespaceprefix,
            name="AdministrativeInformation",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="AdministrativeInformation",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="AdministrativeInformation",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="AdministrativeInformation",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.dataEntryBy is not None:
            self.dataEntryBy.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="dataEntryBy",
                pretty_print=pretty_print,
            )
        if self.dataGeneratorAndPublication is not None:
            self.dataGeneratorAndPublication.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="dataGeneratorAndPublication",
                pretty_print=pretty_print,
            )
        for one_person in self.person:
            one_person.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="person",
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
        if nodeName == "dataEntryBy":
            obj = DataEntryBy(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.dataEntryBy = obj
            obj.original_tagname = "dataEntryBy"
        elif nodeName == "dataGeneratorAndPublication":
            obj = DataGeneratorAndPublication(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.dataGeneratorAndPublication = obj
            obj.original_tagname = "dataGeneratorAndPublication"
        elif nodeName == "person":
            obj = Person(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.person.append(obj)
            obj.original_tagname = "person"



# end class AdministrativeInformation
