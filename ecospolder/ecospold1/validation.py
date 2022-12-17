import sys
sys.path.append('../')
from ecospold_base import *

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
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.proofReadingDetails = _cast(None, proofReadingDetails)
        self.proofReadingValidator = _cast(int, proofReadingValidator)
        self.otherDetails = _cast(None, otherDetails)

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
        name="Validation",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("Validation")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Validation":
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
            outfile, level, already_processed, namespaceprefix, name="Validation"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Validation",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix="",
        name="Validation",
    ):
        if (
            self.proofReadingDetails is not None
            and "proofReadingDetails" not in already_processed
        ):
            already_processed.add("proofReadingDetails")
            outfile.write(
                " proofReadingDetails=%s"
                % (
                    self.encode(
                        self.format_string(
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
                % self.format_integer(
                    self.proofReadingValidator, input_name="proofReadingValidator"
                )
            )
        if self.otherDetails is not None and "otherDetails" not in already_processed:
            already_processed.add("otherDetails")
            outfile.write(
                " otherDetails=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.otherDetails), input_name="otherDetails"
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
        name="Validation",
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
        value = find_attr_value("proofReadingDetails", node)
        if value is not None and "proofReadingDetails" not in already_processed:
            already_processed.add("proofReadingDetails")
            self.proofReadingDetails = value
            self.validate_TString32000(
                self.proofReadingDetails
            )  # validate type TString32000
        value = find_attr_value("proofReadingValidator", node)
        if value is not None and "proofReadingValidator" not in already_processed:
            already_processed.add("proofReadingValidator")
            self.proofReadingValidator = self.parse_integer(
                value, node, "proofReadingValidator"
            )
            self.validate_TIndexNumber(
                self.proofReadingValidator
            )  # validate type TIndexNumber
        value = find_attr_value("otherDetails", node)
        if value is not None and "otherDetails" not in already_processed:
            already_processed.add("otherDetails")
            self.otherDetails = value
            self.validate_TString32000(self.otherDetails)  # validate type TString32000

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class Validation
