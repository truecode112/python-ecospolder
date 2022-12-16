from EcoSpold01Base import *

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)
    
class TDataEntryBy(GeneratedsSuper):
    """TDataEntryBy -- Contains information about the person that entered data in the database or transformed data into the format of the ecoinvent (or any other) quality network.
    person -- ID number for the person that prepared the dataset and enters the dataset into the database. It must correspond to an ID number of a person listed in the respective dataset.
    qualityNetwork -- Indicates a project team that works on the database. The information is used, e.g., for restricting the accessibility of dataset information to one particular quality network. The code used is: 1=ecoinvent
    
    """
    def __init__(self, person=None, qualityNetwork=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = ""
        self.person = _cast(int, person)
        self.person_nsprefix_ = None
        self.qualityNetwork = _cast(int, qualityNetwork)
        self.qualityNetwork_nsprefix_ = None
        
    def factory(*args_, **kwargs_):
        return TDataEntryBy(*args_, **kwargs_)

    factory = staticmethod(factory)
    
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
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"', name_='TDataEntryBy', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TDataEntryBy')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TDataEntryBy':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TDataEntryBy')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TDataEntryBy', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TDataEntryBy'):
        if self.person is not None and 'person' not in already_processed:
            already_processed.add('person')
            outfile.write(' person="%s"' % self.gds_format_integer(self.person, input_name='person'))
        if self.qualityNetwork is not None and 'qualityNetwork' not in already_processed:
            already_processed.add('qualityNetwork')
            outfile.write(' qualityNetwork="%s"' % self.gds_format_integer(self.qualityNetwork, input_name='qualityNetwork'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"', name_='TDataEntryBy', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('person', node)
        if value is not None and 'person' not in already_processed:
            already_processed.add('person')
            self.person = self.gds_parse_integer(value, node, 'person')
            self.validate_TIndexNumber(self.person)    # validate type TIndexNumber
        value = find_attr_value_('qualityNetwork', node)
        if value is not None and 'qualityNetwork' not in already_processed:
            already_processed.add('qualityNetwork')
            self.qualityNetwork = self.gds_parse_integer(value, node, 'qualityNetwork')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TDataEntryBy