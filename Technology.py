from EcoSpold01Base import *

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)
    
class TTechnology(GeneratedsSuper):
    """TTechnology -- Contains a description of the technology for which flow data have been collected. Free text can be used. Pictures, graphs and tables are not allowed. The text should cover information necessary to identify the properties and particularities of the technology(ies) underlying the process data.
    text -- Describes the technological properties of the unit process. If the process comprises several subprocesses, the corresponding technologies should be reported as well. Professional nomenclature should be used for the description.
    The description helps the user to judge the technical suitability of the process dataset for his or her application (purpose).
    No graphs, figures or tables are allowed in this text field.
    It should be stated if data for certain elementary flows or intermediate product flows are derived from different technology.
    
    """
    subclass = None
    superclass = None
    def __init__(self, text=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = ""
        self.text = _cast(None, text)
        self.text_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TTechnology)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TTechnology.subclass:
            return TTechnology.subclass(*args_, **kwargs_)
        else:
            return TTechnology(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text
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
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"', name_='TTechnology', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TTechnology')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TTechnology':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TTechnology')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TTechnology', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TTechnology'):
        if self.text is not None and 'text' not in already_processed:
            already_processed.add('text')
            outfile.write(' text=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.text), input_name='text')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"', name_='TTechnology', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('text', node)
        if value is not None and 'text' not in already_processed:
            already_processed.add('text')
            self.text = value
            self.validate_TString32000(self.text)    # validate type TString32000
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TTechnology