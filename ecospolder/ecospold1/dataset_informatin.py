import sys
sys.path.append('../')
from ecospold_base import *


class DatasetInformation(EcospoldBase):
    """DatasetInformation -- Contains the administrative information about the dataset at issue: type of dataset (unit process, elementary flow, impact category, multi-output process) timestamp, version and internalVersion number as well as language and localLanguage code.
    type -- Indicates the kind of data that is represented by this dataset.
    The code is: 0=System non-terminated. 1=Unit process. 2=System terminated. 3=Elementary flow. 4=Impact category.5=Multioutput process.
    'Unit process' contains the description of processes and their direct (in situ) elementary flows (emissions and resource consumption) and intermediate product flows (demand for energy carriers, waste treatment and transport services, working materials, etc.), so-called unit process raw data. Data that arrives at the ecoinvent database in the form of life cycle inventory results are nevertheless classified as unit process.
    'System non-terminated' is not used in the ecoinvent quality network.
    'System terminated' contains the cumulative elementary flows (i.e. the life cycle inventory result) of a unit process. This code is only used for datasets calculated within the ecoinvent database (LCI results).
    'Elementary flow' contains the definition of pollutants and of resources.
    'Impact category' contains the definition of the characterisation, damage or weighting factors of life cycle impact assessment methods.
    'Multioutput process' is a special kind of unit process, which delivers more than one product/service output.
    impactAssessmentResult -- Indicates whether or not (yes/no) the dataset contains the results of an impact assessment applied on unit processes (unit process raw data) or terminated systems (LCI results).
    timestamp -- Automatically generated date when dataset is created.
    version -- The ecoinvent version number is used as follows: with a major update (e.g. every second year) the version number is increased by one (1.00, 2.00, etc.). The digits after the decimal point (e.g., 1.01, 1.02, etc.) are used for minor updates (corrected errors) within the period of two major updates. The version number is placed manually.
    internalVersion -- The internalVersion number is used to discern different versions during the working period until the dataset is entered into the database). The internalVersion is generated automatically with each change made in the dataset or related file.
    energyValues -- Indicates the way energy values are used and applied in the dataset. The codes are: 0=Undefined. 1=Net values. 2=Gross values.
    This data field is by default set to 0 and not actively used in ecoinvent quality network.
    languageCode -- 2 letter ISO language codes are used. Default language is English. Lower case letters are used.
    localLanguageCode -- 2 letter ISO language codes are used. Default localLanguage is German. Lower case letters are used.

    """

    def __init__(
        self,
        type=None,
        impactAssessmentResult=None,
        timestamp=None,
        version=None,
        internalVersion=None,
        energyValues=None,
        languageCode="en",
        localLanguageCode="de",
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.type = cast_value_with_type(int, type)
        self.impactAssessmentResult = cast_value_with_type(bool, impactAssessmentResult)
        if isinstance(timestamp, BaseStrType):
            initvalue = date_t.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        else:
            initvalue = timestamp
        self.timestamp = initvalue
        self.version = cast_value_with_type(float, version)
        self.internalVersion = cast_value_with_type(float, internalVersion)
        self.energyValues = cast_value_with_type(int, energyValues)
        self.languageCode = cast_value_with_type(None, languageCode)
        self.localLanguageCode = cast_value_with_type(None, localLanguageCode)

    def validate_typeType(self, value):
        # Validate type typeType, a restriction on xsd:integer.
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
            if value < 0:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on typeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 5:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on typeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_versionType(self, value):
        # Validate type versionType, a restriction on xsd:float.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, float):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (float)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if not self.validate_simple_patterns(
                self.validate_versionType_patterns_, value
            ):
                self.collector.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_versionType_patterns_,
                    )
                )

    validate_versionType_patterns_ = [["^(\\d{1,2} ?\\.?\\d{0,2})$"]]

    def validate_internalVersionType(self, value):
        # Validate type internalVersionType, a restriction on xsd:float.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, float):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (float)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if not self.validate_simple_patterns(
                self.validate_internalVersionType_patterns_, value
            ):
                self.collector.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_internalVersionType_patterns_,
                    )
                )

    validate_internalVersionType_patterns_ = [["^(\\d{1,2}\\.\\d{1,2})$"]]

    def validate_energyValuesType(self, value):
        # Validate type energyValuesType, a restriction on xsd:integer.
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
            if value < 0:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on energyValuesType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 2:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on energyValuesType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_ISOLanguageCode(self, value):
        # Validate type ISOLanguageCode, a restriction on xsd:string.
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
            value = value
            enumerations = [
                "ab",
                "aa",
                "af",
                "sq",
                "am",
                "ar",
                "hy",
                "as",
                "ay",
                "az",
                "ba",
                "eu",
                "bn",
                "dz",
                "bh",
                "bi",
                "br",
                "bg",
                "my",
                "be",
                "km",
                "ca",
                "zh",
                "co",
                "hr",
                "cs",
                "da",
                "nl",
                "en",
                "eo",
                "et",
                "fo",
                "fa",
                "fj",
                "fi",
                "fr",
                "fy",
                "gl",
                "ka",
                "de",
                "el",
                "kl",
                "gn",
                "gu",
                "ha",
                "iw",
                "he",
                "hi",
                "hu",
                "is",
                "in",
                "id",
                "ia",
                "ie",
                "iu",
                "ik",
                "ga",
                "it",
                "ja",
                "jw",
                "kn",
                "ks",
                "kk",
                "rw",
                "ky",
                "rn",
                "ko",
                "ku",
                "lo",
                "la",
                "lv",
                "ln",
                "lt",
                "mk",
                "mg",
                "ms",
                "ml",
                "mt",
                "gv",
                "mi",
                "mr",
                "mo",
                "mn",
                "na",
                "ne",
                "no",
                "oc",
                "or",
                "om",
                "ps",
                "pl",
                "pt",
                "pa",
                "qu",
                "rm",
                "ro",
                "ru",
                "sm",
                "sg",
                "sa",
                "gd",
                "sr",
                "sh",
                "st",
                "tn",
                "sn",
                "sd",
                "si",
                "ss",
                "sk",
                "sl",
                "so",
                "es",
                "su",
                "sw",
                "sv",
                "tl",
                "tg",
                "ta",
                "tt",
                "te",
                "th",
                "bo",
                "ti",
                "to",
                "ts",
                "tr",
                "tk",
                "tw",
                "ug",
                "uk",
                "ur",
                "uz",
                "vi",
                "vo",
                "cy",
                "wo",
                "xh",
                "ji",
                "yi",
                "yo",
                "zu",
            ]
            if value not in enumerations:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ISOLanguageCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
            if len(value) != 2:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on ISOLanguageCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def hasContent(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="DatasetInformation",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "DatasetInformation":
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
            name="DatasetInformation",
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="DatasetInformation",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="DatasetInformation",
    ):
        if self.type is not None and "type" not in already_processed:
            already_processed.add("type")
            outfile.write(
                ' type="%s"' % self.format_integer(self.type, input_name="type")
            )
        if (
            self.impactAssessmentResult is not None
            and "impactAssessmentResult" not in already_processed
        ):
            already_processed.add("impactAssessmentResult")
            outfile.write(
                ' impactAssessmentResult="%s"'
                % self.format_boolean(
                    self.impactAssessmentResult, input_name="impactAssessmentResult"
                )
            )
        if self.timestamp is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            outfile.write(
                ' timestamp="%s"'
                % self.format_datetime(self.timestamp, input_name="timestamp")
            )
        if self.version is not None and "version" not in already_processed:
            already_processed.add("version")
            outfile.write(
                ' version="%s"'
                % self.format_float(self.version, input_name="version")
            )
        if (
            self.internalVersion is not None
            and "internalVersion" not in already_processed
        ):
            already_processed.add("internalVersion")
            outfile.write(
                ' internalVersion="%s"'
                % self.format_float(
                    self.internalVersion, input_name="internalVersion"
                )
            )
        if self.energyValues is not None and "energyValues" not in already_processed:
            already_processed.add("energyValues")
            outfile.write(
                ' energyValues="%s"'
                % self.format_integer(self.energyValues, input_name="energyValues")
            )
        if self.languageCode != "en" and "languageCode" not in already_processed:
            already_processed.add("languageCode")
            outfile.write(
                " languageCode=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.languageCode), input_name="languageCode"
                        )
                    ),
                )
            )
        if (
            self.localLanguageCode != "de"
            and "localLanguageCode" not in already_processed
        ):
            already_processed.add("localLanguageCode")
            outfile.write(
                " localLanguageCode=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.localLanguageCode),
                            input_name="localLanguageCode",
                        )
                    ),
                )
            )

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="DatasetInformation",
        fromsubclass=False,
        pretty_print=True,
    ):
        pass

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
        value = find_attr_value("type", node)
        if value is not None and "type" not in already_processed:
            already_processed.add("type")
            self.type = self.parse_integer(value, node, "type")
            self.validate_typeType(self.type)  # validate type typeType
        value = find_attr_value("impactAssessmentResult", node)
        if value is not None and "impactAssessmentResult" not in already_processed:
            already_processed.add("impactAssessmentResult")
            if value in ("true", "1"):
                self.impactAssessmentResult = True
            elif value in ("false", "0"):
                self.impactAssessmentResult = False
            else:
                raise_parse_error(node, "Bad boolean attribute")
        value = find_attr_value("timestamp", node)
        if value is not None and "timestamp" not in already_processed:
            already_processed.add("timestamp")
            try:
                self.timestamp = self.parse_datetime(value)
            except ValueError as exp:
                raise ValueError("Bad date-time attribute (timestamp): %s" % exp)
        value = find_attr_value("version", node)
        if value is not None and "version" not in already_processed:
            already_processed.add("version")
            value = self.parse_float(value, node, "version")
            self.version = value
            self.validate_versionType(self.version)  # validate type versionType
        value = find_attr_value("internalVersion", node)
        if value is not None and "internalVersion" not in already_processed:
            already_processed.add("internalVersion")
            value = self.parse_float(value, node, "internalVersion")
            self.internalVersion = value
            self.validate_internalVersionType(
                self.internalVersion
            )  # validate type internalVersionType
        value = find_attr_value("energyValues", node)
        if value is not None and "energyValues" not in already_processed:
            already_processed.add("energyValues")
            self.energyValues = self.parse_integer(value, node, "energyValues")
            self.validate_energyValuesType(
                self.energyValues
            )  # validate type energyValuesType
        value = find_attr_value("languageCode", node)
        if value is not None and "languageCode" not in already_processed:
            already_processed.add("languageCode")
            self.languageCode = value
            self.validate_ISOLanguageCode(
                self.languageCode
            )  # validate type ISOLanguageCode
        value = find_attr_value("localLanguageCode", node)
        if value is not None and "localLanguageCode" not in already_processed:
            already_processed.add("localLanguageCode")
            self.localLanguageCode = value
            self.validate_ISOLanguageCode(
                self.localLanguageCode
            )  # validate type ISOLanguageCode

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class DatasetInformation
