
from EcoSpold01Base import *
from ReferenceFunction import TReferenceFunction
from Geography import TGeography
from Technology import TTechnology
from TimePeriod import TTimePeriod
from DataSetInformation import TDataSetInformation

class TProcessInformation(GeneratedsSuper):
    """TProcessInformation -- Contains content-related metainformation for the unit process.
    referenceFunction -- Comprises information which identifies and characterises one particular dataset (=unit process or system terminated).
    geography -- Describes the geographic area for which the dataset is supposed to be valid. It is the supply region (not the production region) of the product service at issue. It helps the user to judge the geographical suitability of the process (or impact category) dataset for his or her application (purpose).
    technology -- Describes the technological properties of the unit process. It helps the user to judge the technical suitability of the process dataset for his or her application (purpose).
    timePeriod -- Characterises the temporal properties of the unit process (or system terminated) at issue. It helps the user to judge the temporal suitability of the process dataset for his or her application (purpose).
    dataSetInformation -- Contains administrative information about the dataset (version number, language and localLanguage used).
    
    """
    def __init__(self, referenceFunction=None, geography=None, technology=None, timePeriod=None, dataSetInformation=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.referenceFunction = referenceFunction
        self.referenceFunction_nsprefix_ = ""
        self.geography = geography
        self.geography_nsprefix_ = ""
        self.technology = technology
        self.technology_nsprefix_ = ""
        self.timePeriod = timePeriod
        self.timePeriod_nsprefix_ = ""
        self.dataSetInformation = dataSetInformation
        self.dataSetInformation_nsprefix_ = ""
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TProcessInformation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TProcessInformation.subclass:
            return TProcessInformation.subclass(*args_, **kwargs_)
        else:
            return TProcessInformation(*args_, **kwargs_)
    factory = staticmethod(factory)

    def _hasContent(self):
        if (
            self.referenceFunction is not None or
            self.geography is not None or
            self.technology is not None or
            self.timePeriod is not None or
            self.dataSetInformation is not None or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TProcessInformation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TProcessInformation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TProcessInformation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TProcessInformation')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TProcessInformation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TProcessInformation'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TProcessInformation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.referenceFunction is not None:
            namespaceprefix_ = self.referenceFunction_nsprefix_ + ':' if (UseCapturedNS_ and self.referenceFunction_nsprefix_) else ''
            self.referenceFunction.export(outfile, level, namespaceprefix_, namespacedef_='', name_='referenceFunction', pretty_print=pretty_print)
        if self.geography is not None:
            namespaceprefix_ = self.geography_nsprefix_ + ':' if (UseCapturedNS_ and self.geography_nsprefix_) else ''
            self.geography.export(outfile, level, namespaceprefix_, namespacedef_='', name_='geography', pretty_print=pretty_print)
        if self.technology is not None:
            namespaceprefix_ = self.technology_nsprefix_ + ':' if (UseCapturedNS_ and self.technology_nsprefix_) else ''
            self.technology.export(outfile, level, namespaceprefix_, namespacedef_='', name_='technology', pretty_print=pretty_print)
        if self.timePeriod is not None:
            namespaceprefix_ = self.timePeriod_nsprefix_ + ':' if (UseCapturedNS_ and self.timePeriod_nsprefix_) else ''
            self.timePeriod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='timePeriod', pretty_print=pretty_print)
        if self.dataSetInformation is not None:
            namespaceprefix_ = self.dataSetInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.dataSetInformation_nsprefix_) else ''
            self.dataSetInformation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataSetInformation', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'referenceFunction':
            obj_ = TReferenceFunction.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.referenceFunction = obj_
            obj_.original_tagname_ = 'referenceFunction'
        elif nodeName_ == 'geography':
            obj_ = TGeography.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.geography = obj_
            obj_.original_tagname_ = 'geography'
        elif nodeName_ == 'technology':
            obj_ = TTechnology.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.technology = obj_
            obj_.original_tagname_ = 'technology'
        elif nodeName_ == 'timePeriod':
            obj_ = TTimePeriod.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.timePeriod = obj_
            obj_.original_tagname_ = 'timePeriod'
        elif nodeName_ == 'dataSetInformation':
            obj_ = TDataSetInformation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataSetInformation = obj_
            obj_.original_tagname_ = 'dataSetInformation'
        else:
            content_ = self.gds_build_any(child_, 'TProcessInformation')
            self.anytypeobjs_.append(content_)
# end class TProcessInformation