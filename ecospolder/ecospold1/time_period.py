import sys
sys.path.append('../')
from ecospold_base import *
import datetime

class TimePeriod(EcospoldBase):
    """TimePeriod -- Contains all possible date-formats applicable to describe start and end date of the time period for which the dataset is valid.
    dataValidForEntirePeriod -- Indicates whether or not the process data (elementary and intermediate product flows reported under flow data) are valid for the entire time period stated. If not, explanations may be given under 'text'.
    text -- Additional explanations concerning the temporal validity of the flow data reported. It may comprise information about:
    - how strong the temporal correlation is for the unit process at issue (e.g., are four year old data still adequate for the process operated today?),
    - why data is not valid for the entire period,
    - for which smaller periods data are valid,
    - whether for certain elementary and intermediate product flows a different time period is valid.
    The fact that data are based on forecasts should be reported under 'representativeness'.
    startYear -- Start date of the time period for which the dataset is valid, entered as year only.
    startYearMonth -- Start date of the time period for which the dataset is valid, entered as year and month.
    startDate -- Start date of the time period for which the dataset is valid, presented as a complete date (year-month-day).
    StartDate may as well be entered as year (0000) or year-month (0000-00) only. 2000 and 2000-01 means: from 01.01.2000.
    If it is only known that data is older than a certain data, 'startDate' is left blank.
    endYear -- End date of the time period for which the dataset is valid, entered as year only.
    endYearMonth -- End date of the time period for which the dataset is valid, entered as year and month.
    endDate -- End date of the time period for which the dataset is valid, presented as a complete date (year-month-day).
    EndDate may as well be entered as year (0000) or year-month (0000-00) only. 2000 and 2000-12 means: until 31.12.2000.

    """

    subclass = None
    superclass = None

    def __init__(
        self,
        dataValidForEntirePeriod=None,
        text=None,
        startYear=None,
        startYearMonth=None,
        startDate=None,
        endYear=None,
        endYearMonth=None,
        endDate=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.dataValidForEntirePeriod = cast_value_with_type(bool, dataValidForEntirePeriod)
        self.text = cast_value_with_type(None, text)
        self.startYear = startYear
        self.startYearMonth = startYearMonth
        if isinstance(startDate, BaseStrType):
            initvalue = datetime.strptime(startDate, "%Y-%m-%d").date()
        else:
            initvalue = startDate
        self.startDate = initvalue
        self.endYear = endYear
        self.endYearMonth = endYearMonth
        if isinstance(endDate, BaseStrType):
            initvalue = datetime.strptime(endDate, "%Y-%m-%d").date()
        else:
            initvalue = endDate
        self.endDate = initvalue

    def validate_TString32000(self, value):
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

    def hasContent(self):
        if (
            self.startYear is not None
            or self.startYearMonth is not None
            or self.startDate is not None
            or self.endYear is not None
            or self.endYearMonth is not None
            or self.endDate is not None
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
        name="TimePeriod",
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "TimePeriod":
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
            outfile, level, already_processed, namespaceprefix, name="TimePeriod"
        )
        if self.hasContent():
            outfile.write(">%s" % (eol,))
            self.exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="TimePeriod",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="TimePeriod",
    ):
        if (
            self.dataValidForEntirePeriod is not None
            and "dataValidForEntirePeriod" not in already_processed
        ):
            already_processed.add("dataValidForEntirePeriod")
            outfile.write(
                ' dataValidForEntirePeriod="%s"'
                % self.format_boolean(
                    self.dataValidForEntirePeriod, input_name="dataValidForEntirePeriod"
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
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="TimePeriod",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.startYear is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sstartYear>%s</%sstartYear>%s"
                % (
                    namespaceprefix,
                    self.encode(
                        self.format_string(
                            quote_xml(self.startYear), input_name="startYear"
                        )
                    ),
                    namespaceprefix,
                    eol,
                )
            )
        if self.startYearMonth is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sstartYearMonth>%s</%sstartYearMonth>%s"
                % (
                    namespaceprefix,
                    self.encode(
                        self.format_string(
                            quote_xml(self.startYearMonth), input_name="startYearMonth"
                        )
                    ),
                    namespaceprefix,
                    eol,
                )
            )
        if self.startDate is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sstartDate>%s</%sstartDate>%s"
                % (
                    namespaceprefix,
                    self.format_date(self.startDate, input_name="startDate"),
                    namespaceprefix,
                    eol,
                )
            )
        if self.endYear is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sendYear>%s</%sendYear>%s"
                % (
                    namespaceprefix,
                    self.encode(
                        self.format_string(
                            quote_xml(self.endYear), input_name="endYear"
                        )
                    ),
                    namespaceprefix,
                    eol,
                )
            )
        if self.endYearMonth is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sendYearMonth>%s</%sendYearMonth>%s"
                % (
                    namespaceprefix,
                    self.encode(
                        self.format_string(
                            quote_xml(self.endYearMonth), input_name="endYearMonth"
                        )
                    ),
                    namespaceprefix,
                    eol,
                )
            )
        if self.endDate is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sendDate>%s</%sendDate>%s"
                % (
                    namespaceprefix,
                    self.format_date(self.endDate, input_name="endDate"),
                    namespaceprefix,
                    eol,
                )
            )

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
        value = find_attr_value("dataValidForEntirePeriod", node)
        if value is not None and "dataValidForEntirePeriod" not in already_processed:
            already_processed.add("dataValidForEntirePeriod")
            if value in ("true", "1"):
                self.dataValidForEntirePeriod = True
            elif value in ("false", "0"):
                self.dataValidForEntirePeriod = False
            else:
                raise_parse_error(node, "Bad boolean attribute")
        value = find_attr_value("text", node)
        if value is not None and "text" not in already_processed:
            already_processed.add("text")
            self.text = value
            self.validate_TString32000(self.text)  # validate type TString32000

    def buildChildren(
        self, child, node, nodeName, fromsubclass=False, collector=None
    ):
        if nodeName == "startYear":
            value = child.text
            value = self.parse_string(value, node, "startYear")
            value = self.validate_string(value, node, "startYear")
            self.startYear = value
        elif nodeName == "startYearMonth":
            value = child.text
            value = self.parse_string(value, node, "startYearMonth")
            value = self.validate_string(value, node, "startYearMonth")
            self.startYearMonth = value
        elif nodeName == "startDate":
            sval = child.text
            dval = self.parse_date(sval)
            self.startDate = dval
        elif nodeName == "endYear":
            value = child.text
            value = self.parse_string(value, node, "endYear")
            value = self.validate_string(value, node, "endYear")
            self.endYear = value
        elif nodeName == "endYearMonth":
            value = child.text
            value = self.parse_string(value, node, "endYearMonth")
            value = self.validate_string(value, node, "endYearMonth")
            self.endYearMonth = value
        elif nodeName == "endDate":
            sval = child.text
            dval = self.parse_date(sval)
            self.endDate = dval



# end class TimePeriod
