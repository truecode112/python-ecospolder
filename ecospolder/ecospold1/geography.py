import sys
sys.path.append('../')
from ecospold_base import *

class Geography(EcospoldBase):
    """Geography -- Contains information about the geographic validity of the process. The region described with regional code and free text is the market area of the product / service at issue and not necessarily the place of production.
    location -- 7 letter regional code (capital letters). List of 2 letter ISO country codes extended by codes for regions, continents, market areas, and organisations and companies. The location code indicates the supply area of a product/service and the area of validity of impact assessment methods and impact categories, respectively. It does NOT necessarily coincide with the area/site of production or provenience. If supply and production area differ, production area is indicated in the name of the unit process.
    text -- Free text for further explanation. Text comprises additional aspects of the location, namely whether:
    - certain areas are exempted from the location indicated,
    - data are only valid for certain regions within the location indicated.
    - certain elementary flows or intermediate product flows are extrapolated from another geographical area than indicated.
    Extrapolations should be reported under 'representativeness'.

    """

    def __init__(self, location=None, text=None, collector=None, **kwargs) -> None:
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.location = cast_value_with_type(None, location)
        self.text = cast_value_with_type(None, text)

    def validate_TRegionalCode(self, value) -> bool:
        # Validate type TRegionalCode, a restriction on xsd:string.
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
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TRegionalCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TString32000(self, value) -> bool:
        # Validate type TString32000, a restriction on xsd:string.
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
            if len(value) > 32000:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString32000'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def hasContent(self) -> bool:
        return True

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="Geography",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Geography":
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
            outfile, level, already_processed, namespaceprefix, name="Geography"
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Geography",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="Geography"
    ):
        if self.location is not None and "location" not in already_processed:
            already_processed.add("location")
            outfile.write(
                " location=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.location), input_name="location"
                        )
                    ),
                )
            )
        if self.text is not None and "text" not in already_processed:
            already_processed.add("text")
            outfile.write(
                " text=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.text), input_name="text"
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
        name="Geography",
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
        value = find_attr_value("location", node)
        if value is not None and "location" not in already_processed:
            already_processed.add("location")
            self.location = value
            self.validate_TRegionalCode(self.location)  # validate type TRegionalCode
        value = find_attr_value("text", node)
        if value is not None and "text" not in already_processed:
            already_processed.add("text")
            self.text = value
            self.validate_TString32000(self.text)  # validate type TString32000

    def buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class Geography
