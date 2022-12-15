from EcoSpold01Base import *
from DataEntryBy import TDataEntryBy
from DataGeneratorAndPublication import TDataGeneratorAndPublication
from Person import TPerson

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

class TAdministrativeInformation(GeneratedsSuper):

    """TAdministrativeInformation -- Contains information about the person that compiled and entered the dataset in the database and about kind of publication and the accessibility of the dataset.
    dataEntryBy -- Contains information about the person and the quality network the person belongs to.
    dataGeneratorAndPublication -- Contains information about the generator of the dataset in the database, whether the dataset has been published (and how) and about copyright and the accessibility of the dataset (public or restricted to ETH domain, ECOINVENT, or a particular institute of ECOINVENT.
    person -- Contains a list of persons with their addresses.
    
    """

    subclass = None
    superclass = None
    def __init__(self, dataEntryBy=None, dataGeneratorAndPublication=None, person=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.dataEntryBy = dataEntryBy
        self.dataEntryBy_nsprefix_ = ""
        self.dataGeneratorAndPublication = dataGeneratorAndPublication
        self.dataGeneratorAndPublication_nsprefix_ = ""
        if person is None:
            self.person = []
        else:
            self.person = person
        self.person_nsprefix_ = ""
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        return TAdministrativeInformation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_dataEntryBy(self):
        return self.dataEntryBy
    def set_dataEntryBy(self, dataEntryBy):
        self.dataEntryBy = dataEntryBy
    def get_dataGeneratorAndPublication(self):
        return self.dataGeneratorAndPublication
    def set_dataGeneratorAndPublication(self, dataGeneratorAndPublication):
        self.dataGeneratorAndPublication = dataGeneratorAndPublication
    def get_person(self):
        return self.person
    def set_person(self, person):
        self.person = person
    def add_person(self, value):
        self.person.append(value)
    def insert_person_at(self, index, value):
        self.person.insert(index, value)
    def replace_person_at(self, index, value):
        self.person[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def _hasContent(self):
        if (
            self.dataEntryBy is not None or
            self.dataGeneratorAndPublication is not None or
            self.person or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TAdministrativeInformation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TAdministrativeInformation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TAdministrativeInformation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TAdministrativeInformation')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TAdministrativeInformation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TAdministrativeInformation'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ', name_='TAdministrativeInformation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dataEntryBy is not None:
            namespaceprefix_ = self.dataEntryBy_nsprefix_ + ':' if (UseCapturedNS_ and self.dataEntryBy_nsprefix_) else ''
            self.dataEntryBy.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataEntryBy', pretty_print=pretty_print)
        if self.dataGeneratorAndPublication is not None:
            namespaceprefix_ = self.dataGeneratorAndPublication_nsprefix_ + ':' if (UseCapturedNS_ and self.dataGeneratorAndPublication_nsprefix_) else ''
            self.dataGeneratorAndPublication.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataGeneratorAndPublication', pretty_print=pretty_print)
        for person_ in self.person:
            namespaceprefix_ = self.person_nsprefix_ + ':' if (UseCapturedNS_ and self.person_nsprefix_) else ''
            person_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='person', pretty_print=pretty_print)
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
        if nodeName_ == 'dataEntryBy':
            obj_ = TDataEntryBy.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataEntryBy = obj_
            obj_.original_tagname_ = 'dataEntryBy'
        elif nodeName_ == 'dataGeneratorAndPublication':
            obj_ = TDataGeneratorAndPublication.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataGeneratorAndPublication = obj_
            obj_.original_tagname_ = 'dataGeneratorAndPublication'
        elif nodeName_ == 'person':
            obj_ = TPerson.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.person.append(obj_)
            obj_.original_tagname_ = 'person'
        else:
            content_ = self.gds_build_any(child_, 'TAdministrativeInformation')
            self.anytypeobjs_.append(content_)
# end class TAdministrativeInformation    