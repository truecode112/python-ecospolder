from ..ecospold_base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class Validation(EcospoldBase):
    """Validation -- Contains information about who carried out the critical review and about the main results and conclusions of the review and the recommendations made.
    proofReadingDetails -- Contains the comment of the reviewer of the dataset. For the ecoinvent quality network the review text should cover the following items: 1. completeness and transparency of the documentation, 2. conformity with the ecoinvent quality guidelines, 3. plausibility of the data (unit process elementary and intermediate product flows), 4. completeness regarding elementary and intermediate product flows, 5. mathematical correctness. The review is limited to sample audits (not covering each and every figure).
    proofReadingValidator -- Indicates the person who carried out the review. ID number must correspond to an ID number of a person listed in the respective dataset.
    otherDetails -- Contains further information from the review process, especially comments received from third parties once the dataset has been published.

    """

    def __init__(
        self,
        proofReadingDetails=None,
        proofReadingValidator=None,
        otherDetails=None,
        gds_collector_=None,
        **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = ""
        self.proofReadingDetails = _cast(None, proofReadingDetails)
        self.proofReadingDetails_nsprefix_ = None
        self.proofReadingValidator = _cast(int, proofReadingValidator)
        self.proofReadingValidator_nsprefix_ = None
        self.otherDetails = _cast(None, otherDetails)
        self.otherDetails_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Validation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Validation.subclass:
            return Validation.subclass(*args_, **kwargs_)
        else:
            return Validation(*args_, **kwargs_)

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

    def validate_TIndexNumber(self, value):
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

    def _hasContent(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name_="Validation",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Validation")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Validation":
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
            outfile, level, already_processed, namespaceprefix_, name_="Validation"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Validation",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="Validation",
    ):
        if (
            self.proofReadingDetails is not None
            and "proofReadingDetails" not in already_processed
        ):
            already_processed.add("proofReadingDetails")
            outfile.write(
                " proofReadingDetails=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.proofReadingDetails),
                            input_name="proofReadingDetails",
                        )
                    ),
                )
            )
        if (
            self.proofReadingValidator is not None
            and "proofReadingValidator" not in already_processed
        ):
            already_processed.add("proofReadingValidator")
            outfile.write(
                ' proofReadingValidator="%s"'
                % self.gds_format_integer(
                    self.proofReadingValidator, input_name="proofReadingValidator"
                )
            )
        if self.otherDetails is not None and "otherDetails" not in already_processed:
            already_processed.add("otherDetails")
            outfile.write(
                " otherDetails=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.otherDetails), input_name="otherDetails"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_='xmlns:es="http://www.EcoInvent.org/EcoSpold01"',
        name_="Validation",
        fromsubclass_=False,
        pretty_print=True,
    ):
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
        value = find_attr_value_("proofReadingDetails", node)
        if value is not None and "proofReadingDetails" not in already_processed:
            already_processed.add("proofReadingDetails")
            self.proofReadingDetails = value
            self.validate_TString32000(
                self.proofReadingDetails
            )  # validate type TString32000
        value = find_attr_value_("proofReadingValidator", node)
        if value is not None and "proofReadingValidator" not in already_processed:
            already_processed.add("proofReadingValidator")
            self.proofReadingValidator = self.gds_parse_integer(
                value, node, "proofReadingValidator"
            )
            self.validate_TIndexNumber(
                self.proofReadingValidator
            )  # validate type TIndexNumber
        value = find_attr_value_("otherDetails", node)
        if value is not None and "otherDetails" not in already_processed:
            already_processed.add("otherDetails")
            self.otherDetails = value
            self.validate_TString32000(self.otherDetails)  # validate type TString32000

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


# end class Validation
