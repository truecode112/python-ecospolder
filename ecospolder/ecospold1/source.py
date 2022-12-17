import sys
sys.path.append('../')
from ecospold_base import *

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class Source(EcospoldBase):
    """Source -- Contains information about author(s), title, kind of publication, place of publication, name of editors (if any), etc..
    number -- ID number to identify the source within one dataset.
    sourceType -- Indicates the kind of source.
    The codes are: 0=Undefined (default). 1=Article. 2=Chapters in anthology. 3=Seperate publication. 4=Measurement on site. 5=Oral communication. 6=Personal written communication. 7=Questionnaries.
    firstAuthor -- Indicates the first author by surname and abbreviated name (e.g., Einstein A.). In case of measurement on site, oral communication, personal written communication and questionnaries ('sourceType'=4, 5, 6, 7) the name of the communicating person is mentioned here.
    Identifies the source together with 'title' and 'year'.
    additionalAuthors -- List of additional authors (surname and abbreviated name, e.g. Newton I.), separated by commas. 'Et al.' may be used, if more than five additonal authors contributed to the cited publication.
    year -- Indicates the year of publication and communication, respectively.
    Identifies the source together with 'firstAuthor' and 'title'.
    title -- Contains the complete title of the publication.
    Measurement on site: write "Measurement documentation of company XY".
    Oral communication: write "Oral communication, company XY".
    Personal written communication: write: "personal written communication, Mr./Mrs. XY, company Z".
    Questionnaires: write "Questionnaire, filled in by Mr./Mrs. XY, company Z".
    Identifies the source together with 'firstAuthor' and 'year'.
    pageNumbers -- If an article or a chapter in an anthology, list the relevant page numbers. In case of separate publications the total number of pages may be entered.
    nameOfEditors -- Contains the names of the editors (if any).
    titleOfAnthology -- If the publication is a chapter in an anthology, the title of the anthology is reported here.
    For the reports of the ecoinvent quality network 'Final report ecoinvent 2000' is written here.
    placeOfPublications -- Indicates the place(s) of publication. In case of measurements on site, oral communication, personal written communication or questionnaires, it is the location of the company which provided the information. If available via the web add the web-address.
    For the ECOINVENT final reports 'EMPA D
    ü
    bendorf' is written.
    publisher -- Lists the name of the publisher (if any).
    In case of the ecoinvent quality network it is the 'Swiss Centre for Life Cycle Inventories'.
    journal -- Indicates the name of the journal an article is published in.
    volumeNo -- Indicates the volume of the journal an article is published in.
    issueNo -- Indicates the issue number of the journal an article is published in.
    text -- Free text for additional description of the source. It may contain a brief summary of the publication and the kind of medium used (e.g. CD-ROM, hard copy)

    """

    def __init__(
        self,
        number=None,
        sourceType="0",
        firstAuthor=None,
        additionalAuthors=None,
        year=None,
        title=None,
        pageNumbers=None,
        nameOfEditors=None,
        titleOfAnthology=None,
        placeOfPublications=None,
        publisher=None,
        journal=None,
        volumeNo=None,
        issueNo=None,
        text=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.number = _cast(int, number)
        self.sourceType = _cast(int, sourceType)
        self.firstAuthor = _cast(None, firstAuthor)
        self.additionalAuthors = _cast(None, additionalAuthors)
        self.year = _cast(None, year)
        self.title = _cast(None, title)
        self.pageNumbers = _cast(None, pageNumbers)
        self.nameOfEditors = _cast(None, nameOfEditors)
        self.titleOfAnthology = _cast(None, titleOfAnthology)
        self.placeOfPublications = _cast(None, placeOfPublications)
        self.publisher = _cast(None, publisher)
        self.journal = _cast(None, journal)
        self.volumeNo = _cast(int, volumeNo)
        self.issueNo = _cast(None, issueNo)
        self.text = _cast(None, text)

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

    def validate_sourceTypeType(self, value):
        # Validate type sourceTypeType, a restriction on xsd:integer.
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
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on sourceTypeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 7:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on sourceTypeType'
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

    def validate_pageNumbersType(self, value):
        # Validate type pageNumbersType, a restriction on xsd:string.
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
            if len(value) > 15:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on pageNumbersType'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_volumeNoType(self, value):
        # Validate type volumeNoType, a restriction on xsd:integer.
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
            if not self.validate_simple_patterns(
                self.validate_volumeNoType_patterns_, value
            ):
                self.collector.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_volumeNoType_patterns_,
                    )
                )

    validate_volumeNoType_patterns_ = [["^(\\d{1,3})$"]]

    def _hasContent(self):
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
        name="Source",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("Source")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Source":
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
            outfile, level, already_processed, namespaceprefix, name="Source"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Source",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="Source"
    ):
        if self.number is not None and "number" not in already_processed:
            already_processed.add("number")
            outfile.write(
                ' number="%s"'
                % self.format_integer(self.number, input_name="number")
            )
        if self.sourceType != 0 and "sourceType" not in already_processed:
            already_processed.add("sourceType")
            outfile.write(
                ' sourceType="%s"'
                % self.format_integer(self.sourceType, input_name="sourceType")
            )
        if self.firstAuthor is not None and "firstAuthor" not in already_processed:
            already_processed.add("firstAuthor")
            outfile.write(
                " firstAuthor=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.firstAuthor), input_name="firstAuthor"
                        )
                    ),
                )
            )
        if (
            self.additionalAuthors is not None
            and "additionalAuthors" not in already_processed
        ):
            already_processed.add("additionalAuthors")
            outfile.write(
                " additionalAuthors=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.additionalAuthors),
                            input_name="additionalAuthors",
                        )
                    ),
                )
            )
        if self.year is not None and "year" not in already_processed:
            already_processed.add("year")
            outfile.write(
                " year=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.year), input_name="year"
                        )
                    ),
                )
            )
        if self.title is not None and "title" not in already_processed:
            already_processed.add("title")
            outfile.write(
                " title=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.title), input_name="title"
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
        if self.nameOfEditors is not None and "nameOfEditors" not in already_processed:
            already_processed.add("nameOfEditors")
            outfile.write(
                " nameOfEditors=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.nameOfEditors), input_name="nameOfEditors"
                        )
                    ),
                )
            )
        if (
            self.titleOfAnthology is not None
            and "titleOfAnthology" not in already_processed
        ):
            already_processed.add("titleOfAnthology")
            outfile.write(
                " titleOfAnthology=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.titleOfAnthology),
                            input_name="titleOfAnthology",
                        )
                    ),
                )
            )
        if (
            self.placeOfPublications is not None
            and "placeOfPublications" not in already_processed
        ):
            already_processed.add("placeOfPublications")
            outfile.write(
                " placeOfPublications=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.placeOfPublications),
                            input_name="placeOfPublications",
                        )
                    ),
                )
            )
        if self.publisher is not None and "publisher" not in already_processed:
            already_processed.add("publisher")
            outfile.write(
                " publisher=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.publisher), input_name="publisher"
                        )
                    ),
                )
            )
        if self.journal is not None and "journal" not in already_processed:
            already_processed.add("journal")
            outfile.write(
                " journal=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.journal), input_name="journal"
                        )
                    ),
                )
            )
        if self.volumeNo is not None and "volumeNo" not in already_processed:
            already_processed.add("volumeNo")
            outfile.write(
                ' volumeNo="%s"'
                % self.format_integer(self.volumeNo, input_name="volumeNo")
            )
        if self.issueNo is not None and "issueNo" not in already_processed:
            already_processed.add("issueNo")
            outfile.write(
                " issueNo=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.issueNo), input_name="issueNo"
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

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name="Source",
        fromsubclass=False,
        pretty_print=True,
    ):
        pass

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
        value = find_attr_value("sourceType", node)
        if value is not None and "sourceType" not in already_processed:
            already_processed.add("sourceType")
            self.sourceType = self.parse_integer(value, node, "sourceType")
            self.validate_sourceTypeType(
                self.sourceType
            )  # validate type sourceTypeType
        value = find_attr_value("firstAuthor", node)
        if value is not None and "firstAuthor" not in already_processed:
            already_processed.add("firstAuthor")
            self.firstAuthor = value
            self.validate_TString40(self.firstAuthor)  # validate type TString40
        value = find_attr_value("additionalAuthors", node)
        if value is not None and "additionalAuthors" not in already_processed:
            already_processed.add("additionalAuthors")
            self.additionalAuthors = value
            self.validate_TString255(self.additionalAuthors)  # validate type TString255
        value = find_attr_value("year", node)
        if value is not None and "year" not in already_processed:
            already_processed.add("year")
            self.year = value
        value = find_attr_value("title", node)
        if value is not None and "title" not in already_processed:
            already_processed.add("title")
            self.title = value
            self.validate_TString32000(self.title)  # validate type TString32000
        value = find_attr_value("pageNumbers", node)
        if value is not None and "pageNumbers" not in already_processed:
            already_processed.add("pageNumbers")
            self.pageNumbers = value
            self.validate_pageNumbersType(
                self.pageNumbers
            )  # validate type pageNumbersType
        value = find_attr_value("nameOfEditors", node)
        if value is not None and "nameOfEditors" not in already_processed:
            already_processed.add("nameOfEditors")
            self.nameOfEditors = value
            self.validate_TString40(self.nameOfEditors)  # validate type TString40
        value = find_attr_value("titleOfAnthology", node)
        if value is not None and "titleOfAnthology" not in already_processed:
            already_processed.add("titleOfAnthology")
            self.titleOfAnthology = value
            self.validate_TString255(self.titleOfAnthology)  # validate type TString255
        value = find_attr_value("placeOfPublications", node)
        if value is not None and "placeOfPublications" not in already_processed:
            already_processed.add("placeOfPublications")
            self.placeOfPublications = value
            self.validate_TString40(self.placeOfPublications)  # validate type TString40
        value = find_attr_value("publisher", node)
        if value is not None and "publisher" not in already_processed:
            already_processed.add("publisher")
            self.publisher = value
            self.validate_TString40(self.publisher)  # validate type TString40
        value = find_attr_value("journal", node)
        if value is not None and "journal" not in already_processed:
            already_processed.add("journal")
            self.journal = value
            self.validate_TString40(self.journal)  # validate type TString40
        value = find_attr_value("volumeNo", node)
        if value is not None and "volumeNo" not in already_processed:
            already_processed.add("volumeNo")
            self.volumeNo = self.parse_integer(value, node, "volumeNo")
            self.validate_volumeNoType(self.volumeNo)  # validate type volumeNoType
        value = find_attr_value("issueNo", node)
        if value is not None and "issueNo" not in already_processed:
            already_processed.add("issueNo")
            self.issueNo = value
            self.validate_TString40(self.issueNo)  # validate type TString40
        value = find_attr_value("text", node)
        if value is not None and "text" not in already_processed:
            already_processed.add("text")
            self.text = value
            self.validate_TString32000(self.text)  # validate type TString32000

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class Source
