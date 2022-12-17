import sys
sys.path.append('../')
from ecospold_base import *
from lxml import etree as etre


class Person(EcospoldBase):
    """Person -- Used for the identification of members of the organisation / institute co-operating within a quality network (e.g., ecoinvent) referred to in the areas Validation, dataEntryBy and dataGeneratorAndPublication.
    number -- ID number is attributed to each person of an organisation/institute co-operating in a quality network such as ecoinvent. It is used to identify persons cited within one dataset.
    name -- Name and surname of the person working in an organisation/institute which is a member of the quality network.
    Identifies the person together with 'address' (#5803).
    address -- Complete address, including street, po-box (if applicable), zip-code, city, state (if applicable), country.
    Identifies the person together with 'name' (#5802).
    telephone -- Phone number including country and regional codes.
    telefax -- Fax number including country and regional codes.
    email -- Complete email address.
    companyCode -- 7 letter company code of the organisation/institute co-operating in a quality network.
    Identifies the co-operation partner together with the countryCode (#5808).
    countryCode -- 2 letter ISO-country code of the organisation/institute co-operating in a quality network.
    Identifying the co-operation partner together with the companyCode (#5807).

    """

    def __init__(
        self,
        number=None,
        name=None,
        address=None,
        telephone=None,
        telefax=None,
        email=None,
        companyCode=None,
        countryCode=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.number = cast_value_with_type(int, number)
        self.name = cast_value_with_type(None, name)
        self.address = cast_value_with_type(None, address)
        self.telephone = cast_value_with_type(None, telephone)
        self.telefax = cast_value_with_type(None, telefax)
        self.email = cast_value_with_type(None, email)
        self.companyCode = cast_value_with_type(None, companyCode)
        self.countryCode = cast_value_with_type(None, countryCode)

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

    def validate_TString40(self, value):
        # Validate type TString40, a restriction on xsd:string.
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
            if len(value) > 40:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString40'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TString255(self, value):
        # Validate type TString255, a restriction on xsd:string.
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

    def validate_TString80(self, value):
        # Validate type TString80, a restriction on xsd:string.
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
            if len(value) > 80:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString80'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
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
        namespacedef="",
        name="Person",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Person":
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
            outfile, level, already_processed, namespaceprefix, name="Person"
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Person",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="Person"
    ):
        if self.number is not None and "number" not in already_processed:
            already_processed.add("number")
            outfile.write(
                ' number="%s"'
                % self.format_integer(self.number, input_name="number")
            )
        if self.name is not None and "name" not in already_processed:
            already_processed.add("name")
            outfile.write(
                " name=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.name), input_name="name"
                        )
                    ),
                )
            )
        if self.address is not None and "address" not in already_processed:
            already_processed.add("address")
            outfile.write(
                " address=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.address), input_name="address"
                        )
                    ),
                )
            )
        if self.telephone is not None and "telephone" not in already_processed:
            already_processed.add("telephone")
            outfile.write(
                " telephone=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.telephone), input_name="telephone"
                        )
                    ),
                )
            )
        if self.telefax is not None and "telefax" not in already_processed:
            already_processed.add("telefax")
            outfile.write(
                " telefax=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.telefax), input_name="telefax"
                        )
                    ),
                )
            )
        if self.email is not None and "email" not in already_processed:
            already_processed.add("email")
            outfile.write(
                " email=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.email), input_name="email"
                        )
                    ),
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

    def exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef="",
        name="Person",
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
        value = find_attr_value("number", node)
        if value is not None and "number" not in already_processed:
            already_processed.add("number")
            self.number = self.parse_integer(value, node, "number")
            self.validate_TIndexNumber(self.number)  # validate type TIndexNumber
        value = find_attr_value("name", node)
        if value is not None and "name" not in already_processed:
            already_processed.add("name")
            self.name = value
            self.validate_TString40(self.name)  # validate type TString40
        value = find_attr_value("address", node)
        if value is not None and "address" not in already_processed:
            already_processed.add("address")
            self.address = value
            self.validate_TString255(self.address)  # validate type TString255
        value = find_attr_value("telephone", node)
        if value is not None and "telephone" not in already_processed:
            already_processed.add("telephone")
            self.telephone = value
            self.validate_TString40(self.telephone)  # validate type TString40
        value = find_attr_value("telefax", node)
        if value is not None and "telefax" not in already_processed:
            already_processed.add("telefax")
            self.telefax = value
            self.validate_TString40(self.telefax)  # validate type TString40
        value = find_attr_value("email", node)
        if value is not None and "email" not in already_processed:
            already_processed.add("email")
            self.email = value
            self.validate_TString80(self.email)  # validate type TString80
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

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class Person
