from EcoSpold01Base import *

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

class TSource(GeneratedsSuper):
    """TSource -- Contains information about author(s), title, kind of publication, place of publication, name of editors (if any), etc..
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
    subclass = None
    superclass = None
    def __init__(self, number=None, sourceType='0', firstAuthor=None, additionalAuthors=None, year=None, title=None, pageNumbers=None, nameOfEditors=None, titleOfAnthology=None, placeOfPublications=None, publisher=None, journal=None, volumeNo=None, issueNo=None, text=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = ""
        self.number = _cast(int, number)
        self.number_nsprefix_ = None
        self.sourceType = _cast(int, sourceType)
        self.sourceType_nsprefix_ = None
        self.firstAuthor = _cast(None, firstAuthor)
        self.firstAuthor_nsprefix_ = None
        self.additionalAuthors = _cast(None, additionalAuthors)
        self.additionalAuthors_nsprefix_ = None
        self.year = _cast(None, year)
        self.year_nsprefix_ = None
        self.title = _cast(None, title)
        self.title_nsprefix_ = None
        self.pageNumbers = _cast(None, pageNumbers)
        self.pageNumbers_nsprefix_ = None
        self.nameOfEditors = _cast(None, nameOfEditors)
        self.nameOfEditors_nsprefix_ = None
        self.titleOfAnthology = _cast(None, titleOfAnthology)
        self.titleOfAnthology_nsprefix_ = None
        self.placeOfPublications = _cast(None, placeOfPublications)
        self.placeOfPublications_nsprefix_ = None
        self.publisher = _cast(None, publisher)
        self.publisher_nsprefix_ = None
        self.journal = _cast(None, journal)
        self.journal_nsprefix_ = None
        self.volumeNo = _cast(int, volumeNo)
        self.volumeNo_nsprefix_ = None
        self.issueNo = _cast(None, issueNo)
        self.issueNo_nsprefix_ = None
        self.text = _cast(None, text)
        self.text_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSource)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSource.subclass:
            return TSource.subclass(*args_, **kwargs_)
        else:
            return TSource(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_number(self):
        return self.number
    def set_number(self, number):
        self.number = number
    def get_sourceType(self):
        return self.sourceType
    def set_sourceType(self, sourceType):
        self.sourceType = sourceType
    def get_firstAuthor(self):
        return self.firstAuthor
    def set_firstAuthor(self, firstAuthor):
        self.firstAuthor = firstAuthor
    def get_additionalAuthors(self):
        return self.additionalAuthors
    def set_additionalAuthors(self, additionalAuthors):
        self.additionalAuthors = additionalAuthors
    def get_year(self):
        return self.year
    def set_year(self, year):
        self.year = year
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def get_pageNumbers(self):
        return self.pageNumbers
    def set_pageNumbers(self, pageNumbers):
        self.pageNumbers = pageNumbers
    def get_nameOfEditors(self):
        return self.nameOfEditors
    def set_nameOfEditors(self, nameOfEditors):
        self.nameOfEditors = nameOfEditors
    def get_titleOfAnthology(self):
        return self.titleOfAnthology
    def set_titleOfAnthology(self, titleOfAnthology):
        self.titleOfAnthology = titleOfAnthology
    def get_placeOfPublications(self):
        return self.placeOfPublications
    def set_placeOfPublications(self, placeOfPublications):
        self.placeOfPublications = placeOfPublications
    def get_publisher(self):
        return self.publisher
    def set_publisher(self, publisher):
        self.publisher = publisher
    def get_journal(self):
        return self.journal
    def set_journal(self, journal):
        self.journal = journal
    def get_volumeNo(self):
        return self.volumeNo
    def set_volumeNo(self, volumeNo):
        self.volumeNo = volumeNo
    def get_issueNo(self):
        return self.issueNo
    def set_issueNo(self, issueNo):
        self.issueNo = issueNo
    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text
    def validate_TIndexNumber(self, value):
        # Validate type TIndexNumber, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TIndexNumber' % {"value": value, "lineno": lineno} )
                result = False
    def validate_sourceTypeType(self, value):
        # Validate type sourceTypeType, a restriction on xsd:integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on sourceTypeType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on sourceTypeType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_TString40(self, value):
        # Validate type TString40, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString40' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TString255(self, value):
        # Validate type TString255, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString255' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TString32000(self, value):
        # Validate type TString32000, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString32000' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_pageNumbersType(self, value):
        # Validate type pageNumbersType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on pageNumbersType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_volumeNoType(self, value):
        # Validate type volumeNoType, a restriction on xsd:integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_volumeNoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_volumeNoType_patterns_, ))
    validate_volumeNoType_patterns_ = [['^(\\d{1,3})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"', name_='TSource', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSource')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TSource':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSource')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSource', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TSource'):
        if self.number is not None and 'number' not in already_processed:
            already_processed.add('number')
            outfile.write(' number="%s"' % self.gds_format_integer(self.number, input_name='number'))
        if self.sourceType != 0 and 'sourceType' not in already_processed:
            already_processed.add('sourceType')
            outfile.write(' sourceType="%s"' % self.gds_format_integer(self.sourceType, input_name='sourceType'))
        if self.firstAuthor is not None and 'firstAuthor' not in already_processed:
            already_processed.add('firstAuthor')
            outfile.write(' firstAuthor=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.firstAuthor), input_name='firstAuthor')), ))
        if self.additionalAuthors is not None and 'additionalAuthors' not in already_processed:
            already_processed.add('additionalAuthors')
            outfile.write(' additionalAuthors=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.additionalAuthors), input_name='additionalAuthors')), ))
        if self.year is not None and 'year' not in already_processed:
            already_processed.add('year')
            outfile.write(' year=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.year), input_name='year')), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.title), input_name='title')), ))
        if self.pageNumbers is not None and 'pageNumbers' not in already_processed:
            already_processed.add('pageNumbers')
            outfile.write(' pageNumbers=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pageNumbers), input_name='pageNumbers')), ))
        if self.nameOfEditors is not None and 'nameOfEditors' not in already_processed:
            already_processed.add('nameOfEditors')
            outfile.write(' nameOfEditors=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.nameOfEditors), input_name='nameOfEditors')), ))
        if self.titleOfAnthology is not None and 'titleOfAnthology' not in already_processed:
            already_processed.add('titleOfAnthology')
            outfile.write(' titleOfAnthology=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.titleOfAnthology), input_name='titleOfAnthology')), ))
        if self.placeOfPublications is not None and 'placeOfPublications' not in already_processed:
            already_processed.add('placeOfPublications')
            outfile.write(' placeOfPublications=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.placeOfPublications), input_name='placeOfPublications')), ))
        if self.publisher is not None and 'publisher' not in already_processed:
            already_processed.add('publisher')
            outfile.write(' publisher=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.publisher), input_name='publisher')), ))
        if self.journal is not None and 'journal' not in already_processed:
            already_processed.add('journal')
            outfile.write(' journal=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.journal), input_name='journal')), ))
        if self.volumeNo is not None and 'volumeNo' not in already_processed:
            already_processed.add('volumeNo')
            outfile.write(' volumeNo="%s"' % self.gds_format_integer(self.volumeNo, input_name='volumeNo'))
        if self.issueNo is not None and 'issueNo' not in already_processed:
            already_processed.add('issueNo')
            outfile.write(' issueNo=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.issueNo), input_name='issueNo')), ))
        if self.text is not None and 'text' not in already_processed:
            already_processed.add('text')
            outfile.write(' text=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.text), input_name='text')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"', name_='TSource', fromsubclass_=False, pretty_print=True):
        pass
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
        value = find_attr_value_('number', node)
        if value is not None and 'number' not in already_processed:
            already_processed.add('number')
            self.number = self.gds_parse_integer(value, node, 'number')
            self.validate_TIndexNumber(self.number)    # validate type TIndexNumber
        value = find_attr_value_('sourceType', node)
        if value is not None and 'sourceType' not in already_processed:
            already_processed.add('sourceType')
            self.sourceType = self.gds_parse_integer(value, node, 'sourceType')
            self.validate_sourceTypeType(self.sourceType)    # validate type sourceTypeType
        value = find_attr_value_('firstAuthor', node)
        if value is not None and 'firstAuthor' not in already_processed:
            already_processed.add('firstAuthor')
            self.firstAuthor = value
            self.validate_TString40(self.firstAuthor)    # validate type TString40
        value = find_attr_value_('additionalAuthors', node)
        if value is not None and 'additionalAuthors' not in already_processed:
            already_processed.add('additionalAuthors')
            self.additionalAuthors = value
            self.validate_TString255(self.additionalAuthors)    # validate type TString255
        value = find_attr_value_('year', node)
        if value is not None and 'year' not in already_processed:
            already_processed.add('year')
            self.year = value
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_TString32000(self.title)    # validate type TString32000
        value = find_attr_value_('pageNumbers', node)
        if value is not None and 'pageNumbers' not in already_processed:
            already_processed.add('pageNumbers')
            self.pageNumbers = value
            self.validate_pageNumbersType(self.pageNumbers)    # validate type pageNumbersType
        value = find_attr_value_('nameOfEditors', node)
        if value is not None and 'nameOfEditors' not in already_processed:
            already_processed.add('nameOfEditors')
            self.nameOfEditors = value
            self.validate_TString40(self.nameOfEditors)    # validate type TString40
        value = find_attr_value_('titleOfAnthology', node)
        if value is not None and 'titleOfAnthology' not in already_processed:
            already_processed.add('titleOfAnthology')
            self.titleOfAnthology = value
            self.validate_TString255(self.titleOfAnthology)    # validate type TString255
        value = find_attr_value_('placeOfPublications', node)
        if value is not None and 'placeOfPublications' not in already_processed:
            already_processed.add('placeOfPublications')
            self.placeOfPublications = value
            self.validate_TString40(self.placeOfPublications)    # validate type TString40
        value = find_attr_value_('publisher', node)
        if value is not None and 'publisher' not in already_processed:
            already_processed.add('publisher')
            self.publisher = value
            self.validate_TString40(self.publisher)    # validate type TString40
        value = find_attr_value_('journal', node)
        if value is not None and 'journal' not in already_processed:
            already_processed.add('journal')
            self.journal = value
            self.validate_TString40(self.journal)    # validate type TString40
        value = find_attr_value_('volumeNo', node)
        if value is not None and 'volumeNo' not in already_processed:
            already_processed.add('volumeNo')
            self.volumeNo = self.gds_parse_integer(value, node, 'volumeNo')
            self.validate_volumeNoType(self.volumeNo)    # validate type volumeNoType
        value = find_attr_value_('issueNo', node)
        if value is not None and 'issueNo' not in already_processed:
            already_processed.add('issueNo')
            self.issueNo = value
            self.validate_TString40(self.issueNo)    # validate type TString40
        value = find_attr_value_('text', node)
        if value is not None and 'text' not in already_processed:
            already_processed.add('text')
            self.text = value
            self.validate_TString32000(self.text)    # validate type TString32000
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TSource