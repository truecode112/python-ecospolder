from dataset_informatin import DatasetInformation
import sys
sys.path.append('../')
from ecospold_base import *
from geography import Geography
from reference_function import ReferenceFunction
from technology import Technology
from time_period import TimePeriod


class ProcessInformation(EcospoldBase):
    """ProcessInformation -- Contains content-related metainformation for the unit process.
    referenceFunction -- Comprises information which identifies and characterises one particular dataset (=unit process or system terminated).
    geography -- Describes the geographic area for which the dataset is supposed to be valid. It is the supply region (not the production region) of the product service at issue. It helps the user to judge the geographical suitability of the process (or impact category) dataset for his or her application (purpose).
    technology -- Describes the technological properties of the unit process. It helps the user to judge the technical suitability of the process dataset for his or her application (purpose).
    timePeriod -- Characterises the temporal properties of the unit process (or system terminated) at issue. It helps the user to judge the temporal suitability of the process dataset for his or her application (purpose).
    dataSetInformation -- Contains administrative information about the dataset (version number, language and localLanguage used).

    """

    def __init__(
        self,
        referenceFunction=None,
        geography=None,
        technology=None,
        timePeriod=None,
        dataSetInformation=None,
        gds_collector=None,
        **kwargs
    ):
        self.gds_collector = gds_collector
        self.gds_elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.referenceFunction = referenceFunction
        self.geography = geography
        self.technology = technology
        self.timePeriod = timePeriod
        self.dataSetInformation = dataSetInformation

    def _hasContent(self):
        if (
            self.referenceFunction is not None
            or self.geography is not None
            or self.technology is not None
            or self.timePeriod is not None
            or self.dataSetInformation is not None
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
        name="ProcessInformation",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("ProcessInformation")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "ProcessInformation":
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
            name="ProcessInformation",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="ProcessInformation",
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
        name="ProcessInformation",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="ProcessInformation",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.referenceFunction is not None:
            self.referenceFunction.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="referenceFunction",
                pretty_print=pretty_print,
            )
        if self.geography is not None:
            self.geography.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="geography",
                pretty_print=pretty_print,
            )
        if self.technology is not None:
            self.technology.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="technology",
                pretty_print=pretty_print,
            )
        if self.timePeriod is not None:
            self.timePeriod.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="timePeriod",
                pretty_print=pretty_print,
            )
        if self.dataSetInformation is not None:
            self.dataSetInformation.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="dataSetInformation",
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
        if nodeName == "referenceFunction":
            obj = ReferenceFunction(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.referenceFunction = obj
            obj.original_tagname = "referenceFunction"
        elif nodeName == "geography":
            obj = Geography(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.geography = obj
            obj.original_tagname = "geography"
        elif nodeName == "technology":
            obj = Technology(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.technology = obj
            obj.original_tagname = "technology"
        elif nodeName == "timePeriod":
            obj = TimePeriod(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.timePeriod = obj
            obj.original_tagname = "timePeriod"
        elif nodeName == "dataSetInformation":
            obj = DatasetInformation(parent_object=self)
            obj.build(child_, gds_collector=gds_collector)
            self.dataSetInformation = obj
            obj.original_tagname = "dataSetInformation"


# end class ProcessInformation
