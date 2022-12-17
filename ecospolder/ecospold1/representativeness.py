import sys
sys.path.append('../')
from ecospold_base import *

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class Representativeness(EcospoldBase):
    """Representativeness -- Contains information about the fraction of the relevant market supplied by the product/service described in the dataset. Information about market share, production volume (in the ecoinvent quality network: also consumption volume in the market area) and information about how data have been sampled.
    percent -- Indicates the share in market supply in the geographical area indicated of the product/service at issue.
    If data representative for a process operated in one country is used for another country's process, the entry should be '0'. The representativity for the original country is reported under 'extrapolations'.
    productionVolume -- Indicates the market area consumption volume (NOT necessarily identical with the production volume) in the geographical area indicated of the product/service at issue.
    The market volume should be given in absolute terms per year and in common units. It is related to the time period specified elsewhere.
    samplingProcedure -- Indicates the sampling procedure applied for quantifying the exchanges. It should be reported whether the sampling procedure for particular elementary and intermediate product flows differ from the general procedure. Possible problems in combining different sampling procedures should be mentioned.
    extrapolations -- Describes extrapolations of data from another time period, another geographical area or another technology and the way these extrapolations have been carried out.
    It should be reported whether different extrapolations have been done on the level of individual exchanges.
    If data representative for a pr
    ocess operated in one country is used for another country's process, its original representativity can be indicated here.
    Changes in mean values due to extrapolations may also be reported here.
    uncertaintyAdjustments -- For datasets where the additional uncertainty from lacking representativeness has been included in the quantified uncertainty values ('minValue' and 'maxValue'), thus raising the value in 'percent' of the dataset to 100%, this field also reports the original representativeness, the additional uncertainty and the procedure by which it was assessed or calculated.

    """

    def __init__(
        self,
        percent=None,
        productionVolume=None,
        samplingProcedure=None,
        extrapolations=None,
        uncertaintyAdjustments=None,
        collector=None,
        **kwargs
    ):
        self.collector = collector
        self.elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.percent = _cast(float, percent)
        self.productionVolume = _cast(None, productionVolume)
        self.samplingProcedure = _cast(None, samplingProcedure)
        self.extrapolations = _cast(None, extrapolations)
        self.uncertaintyAdjustments = _cast(None, uncertaintyAdjustments)

    def validate_percentType(self, value):
        # Validate type percentType, a restriction on TPercent.
        if (
            value is not None
            and Validate_simpletypes
            and self.collector is not None
        ):
            if not isinstance(value, float):
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (float)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value > 100.0:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on percentType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if not self.validate_simple_patterns(
                self.validate_percentType_patterns_, value
            ):
                self.collector.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_percentType_patterns_,
                    )
                )

    validate_percentType_patterns_ = [["^(\\d{1,3}\\.\\d)$"]]

    def validate_TString80(self, value):
        # Validate type TString80, a restriction on xsd:string.
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
            if len(value) > 80:
                lineno = self.get_node_lineno()
                self.collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString80'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

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
        name="Representativeness",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("Representativeness")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Representativeness":
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
            outfile,
            level,
            already_processed,
            namespaceprefix,
            name="Representativeness",
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Representativeness",
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
        name="Representativeness",
    ):
        if self.percent is not None and "percent" not in already_processed:
            already_processed.add("percent")
            outfile.write(" percent=%s" % (quote_attrib(self.percent),))
        if (
            self.productionVolume is not None
            and "productionVolume" not in already_processed
        ):
            already_processed.add("productionVolume")
            outfile.write(
                " productionVolume=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.productionVolume),
                            input_name="productionVolume",
                        )
                    ),
                )
            )
        if (
            self.samplingProcedure is not None
            and "samplingProcedure" not in already_processed
        ):
            already_processed.add("samplingProcedure")
            outfile.write(
                " samplingProcedure=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.samplingProcedure),
                            input_name="samplingProcedure",
                        )
                    ),
                )
            )
        if (
            self.extrapolations is not None
            and "extrapolations" not in already_processed
        ):
            already_processed.add("extrapolations")
            outfile.write(
                " extrapolations=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.extrapolations),
                            input_name="extrapolations",
                        )
                    ),
                )
            )
        if (
            self.uncertaintyAdjustments is not None
            and "uncertaintyAdjustments" not in already_processed
        ):
            already_processed.add("uncertaintyAdjustments")
            outfile.write(
                " uncertaintyAdjustments=%s"
                % (
                    self.encode(
                        self.format_string(
                            quote_attrib(self.uncertaintyAdjustments),
                            input_name="uncertaintyAdjustments",
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
        name="Representativeness",
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
        value = find_attr_value("percent", node)
        if value is not None and "percent" not in already_processed:
            already_processed.add("percent")
            value = self.parse_float(value, node, "percent")
            self.percent = value
            self.validate_percentType(self.percent)  # validate type percentType
        value = find_attr_value("productionVolume", node)
        if value is not None and "productionVolume" not in already_processed:
            already_processed.add("productionVolume")
            self.productionVolume = value
            self.validate_TString80(self.productionVolume)  # validate type TString80
        value = find_attr_value("samplingProcedure", node)
        if value is not None and "samplingProcedure" not in already_processed:
            already_processed.add("samplingProcedure")
            self.samplingProcedure = value
            self.validate_TString32000(
                self.samplingProcedure
            )  # validate type TString32000
        value = find_attr_value("extrapolations", node)
        if value is not None and "extrapolations" not in already_processed:
            already_processed.add("extrapolations")
            self.extrapolations = value
            self.validate_TString32000(
                self.extrapolations
            )  # validate type TString32000
        value = find_attr_value("uncertaintyAdjustments", node)
        if value is not None and "uncertaintyAdjustments" not in already_processed:
            already_processed.add("uncertaintyAdjustments")
            self.uncertaintyAdjustments = value
            self.validate_TString32000(
                self.uncertaintyAdjustments
            )  # validate type TString32000

    def _buildChildren(
        self, child_, node, nodeName, fromsubclass=False, collector=None
    ):
        pass


# end class Representativeness
