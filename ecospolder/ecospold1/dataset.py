
import sys
sys.path.append('../')

from ecospold_base import *
from flow_data import FlowData
from meta_information import MetaInformation


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class Dataset(EcospoldBase):
    """Dataset -- contains information about one individual unit process (or terminated system). Information is divided into metaInformation and flowData.
    metaInformation -- meta information contains information about the process (its name, (functional) unit, classification, technology, geography, time, etc.), about modelling assumptions and validation details and about dataset administration (version number, kind of dataset, language).
    flowData -- contains information about inputs and outputs (to and from nature as well as to and from technosphere) and information about allocation (flows to be allocated, co-products to be allocated to, allocation factors).

    """

    def __init__(
        self,
        number=None,
        internalSchemaVersion=None,
        generator=None,
        timestamp=None,
        validCompanyCodes=None,
        validRegionalCodes=None,
        validCategories=None,
        validUnits=None,
        metaInformation=None,
        flowData=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.number = _cast(int, number)
        self.internalSchemaVersion = _cast(None, internalSchemaVersion)
        self.generator = _cast(None, generator)
        if isinstance(timestamp, BaseStrType):
            initvalue = date_t.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        else:
            initvalue = timestamp
        self.timestamp = initvalue
        self.validCompanyCodes = _cast(None, validCompanyCodes)
        self.validRegionalCodes = _cast(None, validRegionalCodes)
        self.validCategories = _cast(None, validCategories)
        self.validUnits = _cast(None, validUnits)
        self.metaInformation = metaInformation
        if flowData is None:
            self.flowData = []
        else:
            self.flowData = flowData

    def validate_TIndexNumber(self, value):
        # Validate type es:TIndexNumber, a restriction on xsd:int.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, int):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 1:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TIndexNumber'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_TString255(self, value):
        # Validate type es:TString255, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 255:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString255'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def _hasContent(self):
        if self.metaInformation is not None or self.flowData:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="Dataset",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("Dataset")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Dataset":
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
            outfile, level, already_processed, namespaceprefix, name="Dataset"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Dataset",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="Dataset"
    ):
        if self.number is not None and "number" not in already_processed:
            already_processed.add("number")
            outfile.write(
                ' number="%s"'
                % self.format_integer(self.number, input_name="number")
            )
        if (
            self.internalSchemaVersion is not None
            and "internalSchemaVersion" not in already_processed
        ):
            already_processed.add("internalSchemaVersion")
            outfile.write(
                " internalSchemaVersion=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.internalSchemaVersion),
                            input_name="internalSchemaVersion",
                        )
                    ),
                )
            )
        if self.generator is not None and "generator" not in already_processed:
            already_processed.add("generator")
            outfile.write(
                " generator=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.generator), input_name="generator"
                        )
                    ),
                )
            )
        if self.timestamp is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            outfile.write(
                ' timestamp="%s"'
                % self.format_datetime(self.timestamp, input_name="timestamp")
            )
        if (
            self.validCompanyCodes is not None
            and "validCompanyCodes" not in already_processed
        ):
            already_processed.add("validCompanyCodes")
            outfile.write(
                " validCompanyCodes=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.validCompanyCodes),
                            input_name="validCompanyCodes",
                        )
                    ),
                )
            )
        if (
            self.validRegionalCodes is not None
            and "validRegionalCodes" not in already_processed
        ):
            already_processed.add("validRegionalCodes")
            outfile.write(
                " validRegionalCodes=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.validRegionalCodes),
                            input_name="validRegionalCodes",
                        )
                    ),
                )
            )
        if (
            self.validCategories is not None
            and "validCategories" not in already_processed
        ):
            already_processed.add("validCategories")
            outfile.write(
                " validCategories=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.validCategories),
                            input_name="validCategories",
                        )
                    ),
                )
            )
        if self.validUnits is not None and "validUnits" not in already_processed:
            already_processed.add("validUnits")
            outfile.write(
                " validUnits=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.validUnits), input_name="validUnits"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="Dataset",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.metaInformation is not None:
            self.metaInformation.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="metaInformation",
                pretty_print=pretty_print,
            )
        for flowData_item in self.flowData:
            flowData_item.export(
                outfile,
                level,
                namespaceprefix,
                namespacedef="",
                name="flowData",
                pretty_print=pretty_print,
            )

    def build(self, node, collector=None):
        self.collector = collector
        if SaveElementTreeNode:
            self.elementtree_node = node
        already_processed = set()
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName, collector=collector)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value("number", node)
        if value is not None and "number" not in already_processed:
            already_processed.add("number")
            self.number = self.parse_integer(value, node, "number")
            self.validate_TIndexNumber(self.number)  # validate type TIndexNumber
        value = find_attr_value("internalSchemaVersion", node)
        if value is not None and "internalSchemaVersion" not in already_processed:
            already_processed.add("internalSchemaVersion")
            self.internalSchemaVersion = value
        value = find_attr_value("generator", node)
        if value is not None and "generator" not in already_processed:
            already_processed.add("generator")
            self.generator = value
            self.validate_TString255(self.generator)  # validate type TString255
        value = find_attr_value("timestamp", node)
        if value is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            try:
                self.timestamp = self.parse_datetime(value)
            except ValueError as exp:
                raise ValueError("Bad date-time attribute (timestamp): %s" % exp)
        value = find_attr_value("validCompanyCodes", node)
        if value is not None and "validCompanyCodes" not in already_processed:
            already_processed.add("validCompanyCodes")
            self.validCompanyCodes = value
        value = find_attr_value("validRegionalCodes", node)
        if value is not None and "validRegionalCodes" not in already_processed:
            already_processed.add("validRegionalCodes")
            self.validRegionalCodes = value
        value = find_attr_value("validCategories", node)
        if value is not None and "validCategories" not in already_processed:
            already_processed.add("validCategories")
            self.validCategories = value
        value = find_attr_value("validUnits", node)
        if value is not None and "validUnits" not in already_processed:
            already_processed.add("validUnits")
            self.validUnits = value

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        if nodeName == "metaInformation":
            obj = MetaInformation(parent_object=self)
            obj.build(child_, collector=collector)
            self.metaInformation = obj
            obj.original_tagname = "metaInformation"
        elif nodeName == "flowData":
            obj = FlowData(parent_object=self)
            obj.build(child_, collector=collector)
            self.flowData.append(obj)
            obj.original_tagname = "flowData"


# end class Dataset
