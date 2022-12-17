
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
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.number = _cast(int, number)
        self.number_nsprefix_ = None
        self.internalSchemaVersion = _cast(None, internalSchemaVersion)
        self.internalSchemaVersion_nsprefix_ = None
        self.generator = _cast(None, generator)
        self.generator_nsprefix_ = None
        if isinstance(timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        else:
            initvalue_ = timestamp
        self.timestamp = initvalue_
        self.validCompanyCodes = _cast(None, validCompanyCodes)
        self.validCompanyCodes_nsprefix_ = None
        self.validRegionalCodes = _cast(None, validRegionalCodes)
        self.validRegionalCodes_nsprefix_ = None
        self.validCategories = _cast(None, validCategories)
        self.validCategories_nsprefix_ = None
        self.validUnits = _cast(None, validUnits)
        self.validUnits_nsprefix_ = None
        self.metaInformation = metaInformation
        self.metaInformation_nsprefix_ = ""
        if flowData is None:
            self.flowData = []
        else:
            self.flowData = flowData
        self.flowData_nsprefix_ = ""

    def validate_TIndexNumber(self, value):
        # Validate type es:TIndexNumber, a restriction on xsd:int.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TIndexNumber'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_TString255(self, value):
        # Validate type es:TString255, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
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
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="Dataset",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Dataset")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Dataset":
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
            outfile, level, already_processed, namespaceprefix_, name_="Dataset"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Dataset",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Dataset"
    ):
        if self.number is not None and "number" not in already_processed:
            already_processed.add("number")
            outfile.write(
                ' number="%s"'
                % self.gds_format_integer(self.number, input_name="number")
            )
        if (
            self.internalSchemaVersion is not None
            and "internalSchemaVersion" not in already_processed
        ):
            already_processed.add("internalSchemaVersion")
            outfile.write(
                " internalSchemaVersion=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
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
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.generator), input_name="generator"
                        )
                    ),
                )
            )
        if self.timestamp is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            outfile.write(
                ' timestamp="%s"'
                % self.gds_format_datetime(self.timestamp, input_name="timestamp")
            )
        if (
            self.validCompanyCodes is not None
            and "validCompanyCodes" not in already_processed
        ):
            already_processed.add("validCompanyCodes")
            outfile.write(
                " validCompanyCodes=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
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
                    self.gds_encode(
                        self.gds_format_string(
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
                    self.gds_encode(
                        self.gds_format_string(
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
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.validUnits), input_name="validUnits"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="Dataset",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.metaInformation is not None:
            namespaceprefix_ = (
                self.metaInformation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.metaInformation_nsprefix_)
                else ""
            )
            self.metaInformation.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="metaInformation",
                pretty_print=pretty_print,
            )
        for flowData_ in self.flowData:
            namespaceprefix_ = (
                self.flowData_nsprefix_ + ":"
                if (UseCapturedNS_ and self.flowData_nsprefix_)
                else ""
            )
            flowData_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="flowData",
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
        value = find_attr_value_("number", node)
        if value is not None and "number" not in already_processed:
            already_processed.add("number")
            self.number = self.gds_parse_integer(value, node, "number")
            self.validate_TIndexNumber(self.number)  # validate type TIndexNumber
        value = find_attr_value_("internalSchemaVersion", node)
        if value is not None and "internalSchemaVersion" not in already_processed:
            already_processed.add("internalSchemaVersion")
            self.internalSchemaVersion = value
        value = find_attr_value_("generator", node)
        if value is not None and "generator" not in already_processed:
            already_processed.add("generator")
            self.generator = value
            self.validate_TString255(self.generator)  # validate type TString255
        value = find_attr_value_("timestamp", node)
        if value is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            try:
                self.timestamp = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError("Bad date-time attribute (timestamp): %s" % exp)
        value = find_attr_value_("validCompanyCodes", node)
        if value is not None and "validCompanyCodes" not in already_processed:
            already_processed.add("validCompanyCodes")
            self.validCompanyCodes = value
        value = find_attr_value_("validRegionalCodes", node)
        if value is not None and "validRegionalCodes" not in already_processed:
            already_processed.add("validRegionalCodes")
            self.validRegionalCodes = value
        value = find_attr_value_("validCategories", node)
        if value is not None and "validCategories" not in already_processed:
            already_processed.add("validCategories")
            self.validCategories = value
        value = find_attr_value_("validUnits", node)
        if value is not None and "validUnits" not in already_processed:
            already_processed.add("validUnits")
            self.validUnits = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "metaInformation":
            obj_ = MetaInformation(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metaInformation = obj_
            obj_.original_tagname_ = "metaInformation"
        elif nodeName_ == "flowData":
            obj_ = FlowData(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.flowData.append(obj_)
            obj_.original_tagname_ = "flowData"
        else:
            content_ = self.gds_build_any(child_, "Dataset")
            self.anytypeobjs_.append(content_)


# end class Dataset
