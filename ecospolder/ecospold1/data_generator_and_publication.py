import sys
sys.path.append('../')
from ecospold_base import *



class DataGeneratorAndPublication(EcospoldBase):
    """DataGeneratorAndPublication -- Contains information about who compiled for and entered data into the database. Furthermore contains information about kind of publication underlying the dataset and the accessibility of the dataset.
    person -- ID number for the person that generated the dataset. It must correspond to an ID number of a person listed in the respective dataset.
    dataPublishedIn -- Indicates whether the dataset has been published (not, partly, entirely).
    The codes are: 0=Data as such not published (default). 1=The data of some unit processes or subsystems are published. 2=Data has been published entirely in 'referenceToPublishedSource'.
    Within the ecoinvent quality network all datasets are published in the series of ecoinvent reports.
    referenceToPublishedSource -- ID number for the report in which the dataset is documented. It must correspond to an ID number of a source listed in the respective dataset.
    copyright -- Indicates whether or not a copyright exists. '1' (Yes) or '0' (No) should be entered correspondingly.
    accessRestrictedTo -- Indicates possible access restrictions for the dataset.
    The codes used are: 0=Public. 1=ETH Domain. 2=ecoinvent 2000. 3=Institute.
    If access is restricted to a particular institute, 'companyCode' and 'countryCode' indicates the institute that has access to the data.
    accessRestrictedTo=0: all information can be accessed by everybody
    accessRestrictedTo=1, 2: ecoinvent clients have access to LCI results but not to unit process raw data. Members of the ecoinvent quality network (ecoinvent centre) have access to all information.
    accessRestrictedTo=3: The ecoinvent administrator has full access to information. Via the web only LCI results are accessible (for ecoinvent clients and for members of the ecoinvent centre.
    companyCode -- 7 letter code with which organisations/institutes that co-operate within one of the database quality networks (see also 'qualityNetwork') are characterised and identified. 'countryCode' is required additionally.
    Only required and allowed if access to the dataset is restricted to a particular institute within the ecoinvent quality network.
    countryCode -- 2 letter ISO-country codes are used to indicate the country where organisations/institutes are located which co-operate within one of the database quality networks (see also 'qualityNetwork').
    Only required and allowed if access to the dataset is restricted to a particular institute within the ecoinvent quality network.
    pageNumbers -- Indicates the page numbers in the publication where the table with the unit process raw data, and the characterisation, damage or weighting factors of the impact category, respectively are documented.

    """

    def __init__(
        self,
        person=None,
        dataPublishedIn="0",
        referenceToPublishedSource=None,
        copyright=None,
        accessRestrictedTo=None,
        companyCode=None,
        countryCode=None,
        pageNumbers=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.person = cast_value_with_type(int, person)
        self.dataPublishedIn = cast_value_with_type(int, dataPublishedIn)
        self.referenceToPublishedSource = cast_value_with_type(int, referenceToPublishedSource)
        self.copyright = cast_value_with_type(bool, copyright)
        self.accessRestrictedTo = cast_value_with_type(int, accessRestrictedTo)
        self.companyCode = cast_value_with_type(None, companyCode)
        self.countryCode = cast_value_with_type(None, countryCode)
        self.pageNumbers = cast_value_with_type(None, pageNumbers)

    def validate_TIndexNumber(self, value):
        # Validate type TIndexNumber, a restriction on xsd:int.
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

    def validate_dataPublishedInType(self, value):
        # Validate type dataPublishedInType, a restriction on xsd:integer.
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
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on dataPublishedInType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 2:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on dataPublishedInType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_accessRestrictedToType(self, value):
        # Validate type accessRestrictedToType, a restriction on xsd:integer.
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
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on accessRestrictedToType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 3:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on accessRestrictedToType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_TCompanyCode(self, value):
        # Validate type TCompanyCode, a restriction on xsd:string.
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
            if len(value) > 7:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCompanyCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_ISOCountryCode(self, value):
        # Validate type ISOCountryCode, a restriction on xsd:string.
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
                "AF",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BA",
                "BW",
                "BV",
                "BR",
                "IO",
                "BN",
                "BG",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CG",
                "CK",
                "CR",
                "CI",
                "HR",
                "CU",
                "CY",
                "CZ",
                "DK",
                "DJ",
                "DM",
                "DO",
                "TP",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "FX",
                "GF",
                "PF",
                "TF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GP",
                "GU",
                "GT",
                "GN",
                "GW",
                "GY",
                "HT",
                "HM",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IL",
                "IT",
                "JM",
                "JP",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KP",
                "KR",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MK",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MQ",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "AN",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "NF",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "RE",
                "RO",
                "RU",
                "RW",
                "KN",
                "LC",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "SC",
                "SL",
                "SG",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "ES",
                "LK",
                "SH",
                "PM",
                "SD",
                "SR",
                "SJ",
                "SZ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UM",
                "UY",
                "UZ",
                "VU",
                "VA",
                "VE",
                "VN",
                "VG",
                "VI",
                "WF",
                "EH",
                "YE",
                "CS",
                "CD",
                "ZM",
                "ZW",
            ]
            if value not in enumerations:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ISOCountryCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
            if len(value) != 2:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on ISOCountryCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TString30(self, value):
        # Validate type TString30, a restriction on xsd:string.
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
            if len(value) > 30:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString30'
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
        name="DataGeneratorAndPublication",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if (
            self.original_tagname is not None
            and name == "DataGeneratorAndPublication"
        ):
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
            name="DataGeneratorAndPublication",
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="DataGeneratorAndPublication",
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
        name="DataGeneratorAndPublication",
    ):
        if self.person is not None and "person" not in already_processed:
            already_processed.add("person")
            outfile.write(
                ' person="%s"'
                % self.format_integer(self.person, input_name="person")
            )
        if self.dataPublishedIn != 0 and "dataPublishedIn" not in already_processed:
            already_processed.add("dataPublishedIn")
            outfile.write(
                ' dataPublishedIn="%s"'
                % self.format_integer(
                    self.dataPublishedIn, input_name="dataPublishedIn"
                )
            )
        if (
            self.referenceToPublishedSource is not None
            and "referenceToPublishedSource" not in already_processed
        ):
            already_processed.add("referenceToPublishedSource")
            outfile.write(
                ' referenceToPublishedSource="%s"'
                % self.format_integer(
                    self.referenceToPublishedSource,
                    input_name="referenceToPublishedSource",
                )
            )
        if self.copyright is not None and "copyright" not in already_processed:
            already_processed.add("copyright")
            outfile.write(
                ' copyright="%s"'
                % self.format_boolean(self.copyright, input_name="copyright")
            )
        if (
            self.accessRestrictedTo is not None
            and "accessRestrictedTo" not in already_processed
        ):
            already_processed.add("accessRestrictedTo")
            outfile.write(
                ' accessRestrictedTo="%s"'
                % self.format_integer(
                    self.accessRestrictedTo, input_name="accessRestrictedTo"
                )
            )
        if self.companyCode is not None and "companyCode" not in already_processed:
            already_processed.add("companyCode")
            outfile.write(
                " companyCode=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.companyCode), input_name="companyCode"
                        )
                    ),
                )
            )
        if self.countryCode is not None and "countryCode" not in already_processed:
            already_processed.add("countryCode")
            outfile.write(
                " countryCode=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.countryCode), input_name="countryCode"
                        )
                    ),
                )
            )
        if self.pageNumbers is not None and "pageNumbers" not in already_processed:
            already_processed.add("pageNumbers")
            outfile.write(
                " pageNumbers=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.pageNumbers), input_name="pageNumbers"
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
        name="DataGeneratorAndPublication",
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
        value = find_attr_value("person", node)
        if value is not None and "person" not in already_processed:
            already_processed.add("person")
            self.person = self.parse_integer(value, node, "person")
            self.validate_TIndexNumber(self.person)  # validate type TIndexNumber
        value = find_attr_value("dataPublishedIn", node)
        if value is not None and "dataPublishedIn" not in already_processed:
            already_processed.add("dataPublishedIn")
            self.dataPublishedIn = self.parse_integer(
                value, node, "dataPublishedIn"
            )
            self.validate_dataPublishedInType(
                self.dataPublishedIn
            )  # validate type dataPublishedInType
        value = find_attr_value("referenceToPublishedSource", node)
        if value is not None and "referenceToPublishedSource" not in already_processed:
            already_processed.add("referenceToPublishedSource")
            self.referenceToPublishedSource = self.parse_integer(
                value, node, "referenceToPublishedSource"
            )
            self.validate_TIndexNumber(
                self.referenceToPublishedSource
            )  # validate type TIndexNumber
        value = find_attr_value("copyright", node)
        if value is not None and "copyright" not in already_processed:
            already_processed.add("copyright")
            if value in ("true", "1"):
                self.copyright = True
            elif value in ("false", "0"):
                self.copyright = False
            else:
                raise_parse_error(node, "Bad boolean attribute")
        value = find_attr_value("accessRestrictedTo", node)
        if value is not None and "accessRestrictedTo" not in already_processed:
            already_processed.add("accessRestrictedTo")
            self.accessRestrictedTo = self.parse_integer(
                value, node, "accessRestrictedTo"
            )
            self.validate_accessRestrictedToType(
                self.accessRestrictedTo
            )  # validate type accessRestrictedToType
        value = find_attr_value("companyCode", node)
        if value is not None and "companyCode" not in already_processed:
            already_processed.add("companyCode")
            self.companyCode = value
            self.validate_TCompanyCode(self.companyCode)  # validate type TCompanyCode
        value = find_attr_value("countryCode", node)
        if value is not None and "countryCode" not in already_processed:
            already_processed.add("countryCode")
            self.countryCode = value
            self.validate_ISOCountryCode(
                self.countryCode
            )  # validate type ISOCountryCode
        value = find_attr_value("pageNumbers", node)
        if value is not None and "pageNumbers" not in already_processed:
            already_processed.add("pageNumbers")
            self.pageNumbers = value
            self.validate_TString30(self.pageNumbers)  # validate type TString30

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class DataGeneratorAndPublication
