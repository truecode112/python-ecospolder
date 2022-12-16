from EcoSpold01Base import *
from DataSet import TDataset

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

class TEcoSpold(GeneratedsSuper):
    """TEcoSpold -- the data (exchange) format of the ECOINVENT quality network.
    dataset -- a dataset describes LCI related information of a unit process or a terminated system comprising metaInformation (description of the process) and flowData (quantified inputs and outputs and allocation factors, if any).
    
    """
    def __init__(self, validationId=None, validationStatus=None, dataset=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.validationId = _cast(int, validationId)
        self.validationId_nsprefix_ = None
        self.validationStatus = _cast(None, validationStatus)
        self.validationStatus_nsprefix_ = None
        if dataset is None:
            self.dataset = []
        else:
            self.dataset = dataset
        self.dataset_nsprefix_ = ""
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        return TEcoSpold(*args_, **kwargs_)
    factory = staticmethod(factory)
    
    def _hasContent(self):
        if (
            self.dataset or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TEcoSpold', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TEcoSpold')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TEcoSpold':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TEcoSpold')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TEcoSpold', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TEcoSpold'):
        if self.validationId is not None and 'validationId' not in already_processed:
            already_processed.add('validationId')
            outfile.write(' validationId="%s"' % self.gds_format_integer(self.validationId, input_name='validationId'))
        if self.validationStatus is not None and 'validationStatus' not in already_processed:
            already_processed.add('validationStatus')
            outfile.write(' validationStatus=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.validationStatus), input_name='validationStatus')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TEcoSpold', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for dataset_ in self.dataset:
            namespaceprefix_ = self.dataset_nsprefix_ + ':' if (UseCapturedNS_ and self.dataset_nsprefix_) else ''
            dataset_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataset', pretty_print=pretty_print)
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
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
        value = find_attr_value_('validationId', node)
        if value is not None and 'validationId' not in already_processed:
            already_processed.add('validationId')
            self.validationId = self.gds_parse_integer(value, node, 'validationId')
        value = find_attr_value_('validationStatus', node)
        if value is not None and 'validationStatus' not in already_processed:
            already_processed.add('validationStatus')
            self.validationStatus = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'dataset':
            obj_ = TDataset.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataset.append(obj_)
            obj_.original_tagname_ = 'dataset'
        else:
            content_ = self.gds_build_any(child_, 'TEcoSpold')
            self.anytypeobjs_.append(content_)
# end class TEcoSpold