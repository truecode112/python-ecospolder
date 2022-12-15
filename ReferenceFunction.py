from EcoSpold01Base import *

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

class TReferenceFunction(GeneratedsSuper):
    """TReferenceFunction -- Contains the identifying information of a dataset including name (english and german), unit, classification (category, subCategory), etc..
    datasetRelatesToProduct -- Indicates whether the dataset relates to a process/service or not.
    In the ecoinvent quality network the value required is 'yes' for unit processes and multioutput processes and 'no' for elementary flows and impact categories.
    name -- Name of the unit process, elementary flow or impact category.
    For unit processes and system terminated name is used as the identifying entry together with unit, location and infrastructureProcess (yes/no). The process name is structured as follows (quality guidelines of ecoinvent 2000): 1. Name of product/service, production process or worked product, level of processing; 2. additional descriptions, separated by comma: sum formula, site of production or provenience, company, imports included or not; 3. Location in the value added chain (at plant, at regional storehouse), or destination (for wastes: to sanitary landfill, to municipal incineration) always using "at" and "to", respectively.
    For elementary flows name, unit, category and subCategory are used as the discriminating elements. The nomenclature of the SETAC WG 'Data quality and data availability' is used for elementary flows as far as possible.
    For impact categories, name, location, unit, category and subCategory are used as discriminating elements. The naming of impact categories takes pattern from the corresponding original publication.
    English is the default language in the ecoinvent quality network.
    localName -- see 'name' for explanations.
    German is the default local language in the ecoinvent quality network.
    infrastructureProcess -- Indicates whether the process is an investment or an operation process. Investment processes are for instance building of a nuclear power plant, a road, docks, construction of production machinery which deliver as the output a nuclear power plant, a km road, one seaport, and production machinery respectively. It is used as a discriminating element for the identification of processes.
    Not applicable for elementary flows and impact categories.
    amount -- Indicates the amount of reference flow (product/service, elementary flow, impact category).
    Within the ecoinvent quality network the amount of the reference flow always equals 1.
    unit -- For unit processes (and systems terminated) it is the unit to which all inputs and outputs of the unit process are related to (functional unit).
    For elementary flows it is the unit in which exhanges are reported.
    For impact categories, it is the unit in which characterisation, damage or weighting factors are expressed.
    SI-units are preferred. The units are always expressed in English language.
    category -- Category is used to structure the content of the database (together with SubCategory). It is not required for the identification of a process (processes in different categories/subCategories may therefore not be named identically). But it is required for the identification of elementary flows and impact categories. Categories are administrated centrally.
    English is the default language in the ecoinvent quality network.
    subCategory -- SubCategory is used to further structure the content of the database (together with category). It is not required for the identification of a process (processes in different categories/subCategories may therefore not be named identically). But it is required for the identification of elementary flows and impact categories. SubCategories are administrated centrally.
    English is the default language in the ecoinvent quality network.
    localCategory -- See category for explanations. German is the default local language in the ecoinvent quality network.
    localSubCategory -- See subCategory for explanations. German is the default local language in the ecoinvent quality network.
    includedProcesses -- Contains a description of the (sub-)processes which are combined to form one unit process (e.g., 'operation of heating system' including operation of boiler unit, regulation unit and circulation pumps). Such combination may be necessary because of lack of detailedness in available data or because of data confidentiality. As far as possible and feasible, data should however be reported on the level of detail it has been received.
    Not applicable for elementary flows and impact categories.
    generalComment -- Free text for general information about the dataset. It may contain information about:
    - the intended application of the dataset
    - information sources used
    - data selection principles
    -  modelling choices (exclusion of intermediate product flows, processes, allocation if done before entering into database).
    infrastructureIncluded -- Indicates whether the unit process imported into the database on the basis of an LCI result (received as cumulative mass- and energy-flows, hence, no LCI results will be calculated for such processes) has included infrastructure processes or not. For all other unit process raw data data sets this data field is empty.
    After calculation of LCI results in ecoinvent, the data field is filled in according to the fact, whether or not infrastructure has been including during the calculation.
    Not applicable for elementary flows and impact categories.
    CASNumber -- Indicates the number according to the Chemical Abstract Service (CAS). The Format of the CAS-number: 000000-00-0, where the first string of digits needs not to be complete (i.e. less than six digits are admitted).
    Not applicable for impact categories.
    statisticalClassification -- Contains the EU-classification system (NACE code). For the first edition of the ecoinvent database this data field will not be used.
    Not applicable for elementary flows and impact categories.
    formula -- Chemical formula (e.g. sum formula) may be entered. No graphs are allowed to represent chemical formulas.
    Not applicable for impact categories.
    synonym -- Synonyms for the name, localName. In the Excel editor they are separated by two slashes ('//').
    Synonyms are a subset of referenceFunction. 0..n entries are allowed with a max. length of 80 each.
    
    """
    def __init__(self, datasetRelatesToProduct=None, name=None, localName=None, infrastructureProcess=None, amount=None, unit=None, category=None, subCategory=None, localCategory=None, localSubCategory=None, includedProcesses=None, generalComment=None, infrastructureIncluded=True, CASNumber=None, statisticalClassification=None, formula=None, synonym=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.datasetRelatesToProduct = _cast(bool, datasetRelatesToProduct)
        self.datasetRelatesToProduct_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.localName = _cast(None, localName)
        self.localName_nsprefix_ = None
        self.infrastructureProcess = _cast(bool, infrastructureProcess)
        self.infrastructureProcess_nsprefix_ = None
        self.amount = _cast(float, amount)
        self.amount_nsprefix_ = None
        self.unit = _cast(None, unit)
        self.unit_nsprefix_ = None
        self.category = _cast(None, category)
        self.category_nsprefix_ = None
        self.subCategory = _cast(None, subCategory)
        self.subCategory_nsprefix_ = None
        self.localCategory = _cast(None, localCategory)
        self.localCategory_nsprefix_ = None
        self.localSubCategory = _cast(None, localSubCategory)
        self.localSubCategory_nsprefix_ = None
        self.includedProcesses = _cast(None, includedProcesses)
        self.includedProcesses_nsprefix_ = None
        self.generalComment = _cast(None, generalComment)
        self.generalComment_nsprefix_ = None
        self.infrastructureIncluded = _cast(bool, infrastructureIncluded)
        self.infrastructureIncluded_nsprefix_ = None
        self.CASNumber = _cast(None, CASNumber)
        self.CASNumber_nsprefix_ = None
        self.statisticalClassification = _cast(int, statisticalClassification)
        self.statisticalClassification_nsprefix_ = None
        self.formula = _cast(None, formula)
        self.formula_nsprefix_ = None
        if synonym is None:
            self.synonym = []
        else:
            self.synonym = synonym
        self.synonym_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TReferenceFunction)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TReferenceFunction.subclass:
            return TReferenceFunction.subclass(*args_, **kwargs_)
        else:
            return TReferenceFunction(*args_, **kwargs_)
    factory = staticmethod(factory)

    def validate_TString80(self, value):
        result = True
        # Validate type TString80, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 80:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString80' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TFloatNumber(self, value):
        # Validate type TFloatNumber, a restriction on xsd:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TUnit(self, value):
        # Validate type TUnit, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TUnit' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TCategoryName(self, value):
        # Validate type TCategoryName, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCategoryName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TCategoryName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
    def validate_CASNumberType(self, value):
        # Validate type CASNumberType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CASNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CASNumberType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CASNumberType_patterns_, ))
    validate_CASNumberType_patterns_ = [['^(\\d{1,6}-\\d{2,2}-\\d)$']]
    def validate_statisticalClassificationType(self, value):
        # Validate type statisticalClassificationType, a restriction on xsd:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_statisticalClassificationType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_statisticalClassificationType_patterns_, ))
    validate_statisticalClassificationType_patterns_ = [['^(\\d{1,8})$']]
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
    def _hasContent(self):
        if (
            self.synonym
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TReferenceFunction', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TReferenceFunction')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TReferenceFunction':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TReferenceFunction')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TReferenceFunction', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TReferenceFunction'):
        if self.datasetRelatesToProduct is not None and 'datasetRelatesToProduct' not in already_processed:
            already_processed.add('datasetRelatesToProduct')
            outfile.write(' datasetRelatesToProduct="%s"' % self.gds_format_boolean(self.datasetRelatesToProduct, input_name='datasetRelatesToProduct'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.localName is not None and 'localName' not in already_processed:
            already_processed.add('localName')
            outfile.write(' localName=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.localName), input_name='localName')), ))
        if self.infrastructureProcess is not None and 'infrastructureProcess' not in already_processed:
            already_processed.add('infrastructureProcess')
            outfile.write(' infrastructureProcess="%s"' % self.gds_format_boolean(self.infrastructureProcess, input_name='infrastructureProcess'))
        if self.amount is not None and 'amount' not in already_processed:
            already_processed.add('amount')
            outfile.write(' amount="%s"' % self.gds_format_double(self.amount, input_name='amount'))
        if self.unit is not None and 'unit' not in already_processed:
            already_processed.add('unit')
            outfile.write(' unit=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.unit), input_name='unit')), ))
        if self.category is not None and 'category' not in already_processed:
            already_processed.add('category')
            outfile.write(' category=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.category), input_name='category')), ))
        if self.subCategory is not None and 'subCategory' not in already_processed:
            already_processed.add('subCategory')
            outfile.write(' subCategory=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.subCategory), input_name='subCategory')), ))
        if self.localCategory is not None and 'localCategory' not in already_processed:
            already_processed.add('localCategory')
            outfile.write(' localCategory=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.localCategory), input_name='localCategory')), ))
        if self.localSubCategory is not None and 'localSubCategory' not in already_processed:
            already_processed.add('localSubCategory')
            outfile.write(' localSubCategory=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.localSubCategory), input_name='localSubCategory')), ))
        if self.includedProcesses is not None and 'includedProcesses' not in already_processed:
            already_processed.add('includedProcesses')
            outfile.write(' includedProcesses=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.includedProcesses), input_name='includedProcesses')), ))
        if self.generalComment is not None and 'generalComment' not in already_processed:
            already_processed.add('generalComment')
            outfile.write(' generalComment=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.generalComment), input_name='generalComment')), ))
        if not self.infrastructureIncluded and 'infrastructureIncluded' not in already_processed:
            already_processed.add('infrastructureIncluded')
            outfile.write(' infrastructureIncluded="%s"' % self.gds_format_boolean(self.infrastructureIncluded, input_name='infrastructureIncluded'))
        if self.CASNumber is not None and 'CASNumber' not in already_processed:
            already_processed.add('CASNumber')
            outfile.write(' CASNumber=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.CASNumber), input_name='CASNumber')), ))
        if self.statisticalClassification is not None and 'statisticalClassification' not in already_processed:
            already_processed.add('statisticalClassification')
            outfile.write(' statisticalClassification="%s"' % self.gds_format_integer(self.statisticalClassification, input_name='statisticalClassification'))
        if self.formula is not None and 'formula' not in already_processed:
            already_processed.add('formula')
            outfile.write(' formula=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.formula), input_name='formula')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TReferenceFunction', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for synonym_ in self.synonym:
            namespaceprefix_ = self.synonym_nsprefix_ + ':' if (UseCapturedNS_ and self.synonym_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssynonym>%s</%ssynonym>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(synonym_), input_name='synonym')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('datasetRelatesToProduct', node)
        if value is not None and 'datasetRelatesToProduct' not in already_processed:
            already_processed.add('datasetRelatesToProduct')
            if value in ('true', '1'):
                self.datasetRelatesToProduct = True
            elif value in ('false', '0'):
                self.datasetRelatesToProduct = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
            self.validate_TString80(self.name)    # validate type TString80
        value = find_attr_value_('localName', node)
        if value is not None and 'localName' not in already_processed:
            already_processed.add('localName')
            self.localName = value
            self.validate_TString80(self.localName)    # validate type TString80
        value = find_attr_value_('infrastructureProcess', node)
        if value is not None and 'infrastructureProcess' not in already_processed:
            already_processed.add('infrastructureProcess')
            if value in ('true', '1'):
                self.infrastructureProcess = True
            elif value in ('false', '0'):
                self.infrastructureProcess = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('amount', node)
        if value is not None and 'amount' not in already_processed:
            already_processed.add('amount')
            value = self.gds_parse_double(value, node, 'amount')
            self.amount = value
            self.validate_TFloatNumber(self.amount)    # validate type TFloatNumber
        value = find_attr_value_('unit', node)
        if value is not None and 'unit' not in already_processed:
            already_processed.add('unit')
            self.unit = value
            self.validate_TUnit(self.unit)    # validate type TUnit
        value = find_attr_value_('category', node)
        if value is not None and 'category' not in already_processed:
            already_processed.add('category')
            self.category = value
            self.validate_TCategoryName(self.category)    # validate type TCategoryName
        value = find_attr_value_('subCategory', node)
        if value is not None and 'subCategory' not in already_processed:
            already_processed.add('subCategory')
            self.subCategory = value
            self.validate_TCategoryName(self.subCategory)    # validate type TCategoryName
        value = find_attr_value_('localCategory', node)
        if value is not None and 'localCategory' not in already_processed:
            already_processed.add('localCategory')
            self.localCategory = value
            self.validate_TCategoryName(self.localCategory)    # validate type TCategoryName
        value = find_attr_value_('localSubCategory', node)
        if value is not None and 'localSubCategory' not in already_processed:
            already_processed.add('localSubCategory')
            self.localSubCategory = value
            self.validate_TCategoryName(self.localSubCategory)    # validate type TCategoryName
        value = find_attr_value_('includedProcesses', node)
        if value is not None and 'includedProcesses' not in already_processed:
            already_processed.add('includedProcesses')
            self.includedProcesses = value
            self.validate_TString32000(self.includedProcesses)    # validate type TString32000
        value = find_attr_value_('generalComment', node)
        if value is not None and 'generalComment' not in already_processed:
            already_processed.add('generalComment')
            self.generalComment = value
            self.validate_TString32000(self.generalComment)    # validate type TString32000
        value = find_attr_value_('infrastructureIncluded', node)
        if value is not None and 'infrastructureIncluded' not in already_processed:
            already_processed.add('infrastructureIncluded')
            if value in ('true', '1'):
                self.infrastructureIncluded = True
            elif value in ('false', '0'):
                self.infrastructureIncluded = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('CASNumber', node)
        if value is not None and 'CASNumber' not in already_processed:
            already_processed.add('CASNumber')
            self.CASNumber = value
            self.validate_CASNumberType(self.CASNumber)    # validate type CASNumberType
        value = find_attr_value_('statisticalClassification', node)
        if value is not None and 'statisticalClassification' not in already_processed:
            already_processed.add('statisticalClassification')
            self.statisticalClassification = self.gds_parse_integer(value, node, 'statisticalClassification')
            self.validate_statisticalClassificationType(self.statisticalClassification)    # validate type statisticalClassificationType
        value = find_attr_value_('formula', node)
        if value is not None and 'formula' not in already_processed:
            already_processed.add('formula')
            self.formula = value
            self.validate_TString40(self.formula)    # validate type TString40
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'synonym':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'synonym')
            value_ = self.gds_validate_string(value_, node, 'synonym')
            self.synonym.append(value_)
            self.synonym_nsprefix_ = child_.prefix
            # validate type TString80
            self.validate_TString80(self.synonym[-1])
# end class TReferenceFunction
