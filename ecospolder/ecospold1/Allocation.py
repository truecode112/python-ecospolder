from EcoSpold01Base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class TAllocation(GeneratedsSuper):
    """TAllocation -- Contains all information about allocation procedure, allocation parameters and allocation factors applied on a multi-output process.
    referenceToCoProduct -- Indicates the co-product output for which a particular allocation factor is valid. Additional information is required about the exchange on which the allocation factor is applied (see 'referenceToInputOutput').
    MultipleOccurences=Yes is only valid, if referenceFunction describes a multioutput process.
    allocationMethod -- Indicates the kind of allocation parameter chosen.
    The codes are: -1=Undefined (default). 0=Physical causality. 1=Economic causality. 2=Other method.
    'Other method' comprises in particular physical parameters (like mass, energy, exergy, etc.) and parameters other than economic.
    MultipleOccurences=Yes only valid, if referenceFunction describes a multioutput process.
    fraction -- Allocation factor, expressed as a fraction (in %), applied on one particular exchange for one particular co-product. The sum of the allocation factors applied on one particular exchange must add up to 100%.
    MultipleOccurences=Yes only valid, if referenceFunction describes a multioutput process.
    explanations -- Contains further information about the allocation procedure and the allocation parameter chosen. An eventual coincidence in allocation factors when comparing different allocation parameters (like physical and economic ones) may be reported here as well.
    referenceToInputOutput -- The data field is only required, if the reference function describes a multioutput process.
    Lists the relation(s) to which a certain allocation factor is applied.
    MultipleOccurrence=Yes on two levels: Firstly, the reference occurs per co-product and secondly, the reference occurs per input and output flows which are allocated to the co-products.

    """

    def __init__(
        self,
        referenceToCoProduct=None,
        allocationMethod="-1",
        fraction=None,
        explanations=None,
        referenceToInputOutput=None,
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.referenceToCoProduct = _cast(int, referenceToCoProduct)
        self.referenceToCoProduct_nsprefix_ = None
        self.allocationMethod = _cast(int, allocationMethod)
        self.allocationMethod_nsprefix_ = None
        self.fraction = _cast(float, fraction)
        self.fraction_nsprefix_ = None
        self.explanations = _cast(None, explanations)
        self.explanations_nsprefix_ = None
        if referenceToInputOutput is None:
            self.referenceToInputOutput = []
        else:
            self.referenceToInputOutput = referenceToInputOutput
        self.referenceToInputOutput_nsprefix_ = None

    def factory(*args_, **kwargs_):
        return TAllocation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def validate_TIndexNumber(self, value):
        result = True
        # Validate type TIndexNumber, a restriction on xsd:int.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TIndexNumber'
                    % {"value": value, "lineno": lineno}
                )
                result = False
        return result

    def validate_allocationMethodType(self, value):
        # Validate type allocationMethodType, a restriction on xsd:integer.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < -1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on allocationMethodType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on allocationMethodType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

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
        if self.referenceToInputOutput:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name_="TAllocation",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("TAllocation")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "TAllocation":
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
            outfile, level, already_processed, namespaceprefix_, name_="TAllocation"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="TAllocation",
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
        name_="TAllocation",
    ):
        if (
            self.referenceToCoProduct is not None
            and "referenceToCoProduct" not in already_processed
        ):
            already_processed.add("referenceToCoProduct")
            outfile.write(
                ' referenceToCoProduct="%s"'
                % self.gds_format_integer(
                    self.referenceToCoProduct, input_name="referenceToCoProduct"
                )
            )
        if self.allocationMethod != -1 and "allocationMethod" not in already_processed:
            already_processed.add("allocationMethod")
            outfile.write(
                ' allocationMethod="%s"'
                % self.gds_format_integer(
                    self.allocationMethod, input_name="allocationMethod"
                )
            )
        if self.fraction is not None and "fraction" not in already_processed:
            already_processed.add("fraction")
            outfile.write(
                ' fraction="%s"'
                % self.gds_format_float(self.fraction, input_name="fraction")
            )
        if self.explanations is not None and "explanations" not in already_processed:
            already_processed.add("explanations")
            outfile.write(
                " explanations=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.explanations), input_name="explanations"
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
        name_="TAllocation",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for referenceToInputOutput_ in self.referenceToInputOutput:
            namespaceprefix_ = (
                self.referenceToInputOutput_nsprefix_ + ":"
                if (UseCapturedNS_ and self.referenceToInputOutput_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sreferenceToInputOutput>%s</%sreferenceToInputOutput>%s"
                % (
                    namespaceprefix_,
                    self.gds_format_integer(
                        referenceToInputOutput_, input_name="referenceToInputOutput"
                    ),
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
        value = find_attr_value_("referenceToCoProduct", node)
        if value is not None and "referenceToCoProduct" not in already_processed:
            already_processed.add("referenceToCoProduct")
            self.referenceToCoProduct = self.gds_parse_integer(
                value, node, "referenceToCoProduct"
            )
            self.validate_TIndexNumber(
                self.referenceToCoProduct
            )  # validate type TIndexNumber
        value = find_attr_value_("allocationMethod", node)
        if value is not None and "allocationMethod" not in already_processed:
            already_processed.add("allocationMethod")
            self.allocationMethod = self.gds_parse_integer(
                value, node, "allocationMethod"
            )
            self.validate_allocationMethodType(
                self.allocationMethod
            )  # validate type allocationMethodType
        value = find_attr_value_("fraction", node)
        if value is not None and "fraction" not in already_processed:
            already_processed.add("fraction")
            value = self.gds_parse_float(value, node, "fraction")
            self.fraction = value
        value = find_attr_value_("explanations", node)
        if value is not None and "explanations" not in already_processed:
            already_processed.add("explanations")
            self.explanations = value
            self.validate_TString32000(self.explanations)  # validate type TString32000

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "referenceToInputOutput" and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, "referenceToInputOutput")
            ival_ = self.gds_validate_integer(ival_, node, "referenceToInputOutput")
            self.referenceToInputOutput.append(ival_)
            self.referenceToInputOutput_nsprefix_ = child_.prefix
            # validate type TIndexNumber
            self.validate_TIndexNumber(self.referenceToInputOutput[-1])


# end class TAllocation
