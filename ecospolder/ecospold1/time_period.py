from ..ecospold_base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


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
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.dataValidForEntirePeriod = _cast(bool, dataValidForEntirePeriod)
        self.dataValidForEntirePeriod_nsprefix_ = None
        self.text = _cast(None, text)
        self.text_nsprefix_ = None
        self.startYear = startYear
        self.startYear_nsprefix_ = None
        self.startYearMonth = startYearMonth
        self.startYearMonth_nsprefix_ = None
        if isinstance(startDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(startDate, "%Y-%m-%d").date()
        else:
            initvalue_ = startDate
        self.startDate = initvalue_
        self.startDate_nsprefix_ = None
        self.endYear = endYear
        self.endYear_nsprefix_ = None
        self.endYearMonth = endYearMonth
        self.endYearMonth_nsprefix_ = None
        if isinstance(endDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(endDate, "%Y-%m-%d").date()
        else:
            initvalue_ = endDate
        self.endDate = initvalue_
        self.endDate_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, TimePeriod)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimePeriod.subclass:
            return TimePeriod.subclass(*args_, **kwargs_)
        else:
            return TimePeriod(*args_, **kwargs_)

    factory = staticmethod(factory)

    def validate_TString32000(self, value):
        # Validate type TString32000, a restriction on xsd:string.
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
            if len(value) > 32000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString32000'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def _hasContent(self):
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
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="TimePeriod",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("TimePeriod")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "TimePeriod":
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
            outfile, level, already_processed, namespaceprefix_, name_="TimePeriod"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="TimePeriod",
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
        name_="TimePeriod",
    ):
        if (
            self.dataValidForEntirePeriod is not None
            and "dataValidForEntirePeriod" not in already_processed
        ):
            already_processed.add("dataValidForEntirePeriod")
            outfile.write(
                ' dataValidForEntirePeriod="%s"'
                % self.gds_format_boolean(
                    self.dataValidForEntirePeriod, input_name="dataValidForEntirePeriod"
                )
            )
        if self.text is not None and "text" not in already_processed:
            already_processed.add("text")
            outfile.write(
                " text=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.text), input_name="text"
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
        name_="TimePeriod",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.startYear is not None:
            namespaceprefix_ = (
                self.startYear_nsprefix_ + ":"
                if (UseCapturedNS_ and self.startYear_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sstartYear>%s</%sstartYear>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.startYear), input_name="startYear"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.startYearMonth is not None:
            namespaceprefix_ = (
                self.startYearMonth_nsprefix_ + ":"
                if (UseCapturedNS_ and self.startYearMonth_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sstartYearMonth>%s</%sstartYearMonth>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.startYearMonth), input_name="startYearMonth"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.startDate is not None:
            namespaceprefix_ = (
                self.startDate_nsprefix_ + ":"
                if (UseCapturedNS_ and self.startDate_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sstartDate>%s</%sstartDate>%s"
                % (
                    namespaceprefix_,
                    self.gds_format_date(self.startDate, input_name="startDate"),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.endYear is not None:
            namespaceprefix_ = (
                self.endYear_nsprefix_ + ":"
                if (UseCapturedNS_ and self.endYear_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sendYear>%s</%sendYear>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.endYear), input_name="endYear"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.endYearMonth is not None:
            namespaceprefix_ = (
                self.endYearMonth_nsprefix_ + ":"
                if (UseCapturedNS_ and self.endYearMonth_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sendYearMonth>%s</%sendYearMonth>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.endYearMonth), input_name="endYearMonth"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.endDate is not None:
            namespaceprefix_ = (
                self.endDate_nsprefix_ + ":"
                if (UseCapturedNS_ and self.endDate_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sendDate>%s</%sendDate>%s"
                % (
                    namespaceprefix_,
                    self.gds_format_date(self.endDate, input_name="endDate"),
                    namespaceprefix_,
                    eol_,
                )
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
        value = find_attr_value_("dataValidForEntirePeriod", node)
        if value is not None and "dataValidForEntirePeriod" not in already_processed:
            already_processed.add("dataValidForEntirePeriod")
            if value in ("true", "1"):
                self.dataValidForEntirePeriod = True
            elif value in ("false", "0"):
                self.dataValidForEntirePeriod = False
            else:
                raise_parse_error(node, "Bad boolean attribute")
        value = find_attr_value_("text", node)
        if value is not None and "text" not in already_processed:
            already_processed.add("text")
            self.text = value
            self.validate_TString32000(self.text)  # validate type TString32000

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "startYear":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "startYear")
            value_ = self.gds_validate_string(value_, node, "startYear")
            self.startYear = value_
            self.startYear_nsprefix_ = child_.prefix
        elif nodeName_ == "startYearMonth":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "startYearMonth")
            value_ = self.gds_validate_string(value_, node, "startYearMonth")
            self.startYearMonth = value_
            self.startYearMonth_nsprefix_ = child_.prefix
        elif nodeName_ == "startDate":
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.startDate = dval_
            self.startDate_nsprefix_ = child_.prefix
        elif nodeName_ == "endYear":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "endYear")
            value_ = self.gds_validate_string(value_, node, "endYear")
            self.endYear = value_
            self.endYear_nsprefix_ = child_.prefix
        elif nodeName_ == "endYearMonth":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "endYearMonth")
            value_ = self.gds_validate_string(value_, node, "endYearMonth")
            self.endYearMonth = value_
            self.endYearMonth_nsprefix_ = child_.prefix
        elif nodeName_ == "endDate":
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.endDate = dval_
            self.endDate_nsprefix_ = child_.prefix


# end class TimePeriod
