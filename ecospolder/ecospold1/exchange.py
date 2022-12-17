import sys
sys.path.append('../')

from ecospold_base import *


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class Exchange(EcospoldBase):
    """Exchange -- Comprises all inputs and outputs (both elementary flows and intermediate product flows) recorded in a unit process and its related information.
    number -- ID number used as an identifier of a particular exchange in a dataset.
    category -- Describes the category one particular exchange belongs to (in English language). Category and subCategory are required for elementary flows because they have a discriminative function.
    subCategory -- Describes the subCategory one particular exchange belongs to (in English language). Category and subCategory are required for elementary flows because they have a discriminative function.
    localCategory -- Describes the category one particular exchange belongs to (in German local language).See further explanations in 'category'.
    localSubCategory -- Describes the subCategory one particular exchange belongs to (in German local language).See further explanations in 'subCategory'.
    CASNumber -- Indicates the number according to the Chemical Abstract Service (CAS). The Format of the CAS-number: 000000-00-0, where the first string of digits needs not to be complete (i.e. less than six digits are admitted).
    name -- Name of the exchange (elementary flow or intermediate product flow) in English language. See 'name' in 'metaInformation/referenceFunction' for more explanations.
    location -- Market area information for the intermediate product/service flow. Location is defined by a 7 letter code written with capital letters. See 'metaInformation/referenceFunction' for more explanations.
    Information about the geographic area for which an impact assessment method is valid.
    Not applicable for elementary flows.
    unit -- Unit of the exchange (elementary flow or intermediate product flow). See 'metaInformation/referenceFunction' for more explanations.
    Unit of the elementary flow for which a characterisation, damage or weighting factor is determined.
    meanValue -- Mean amount of elementary flow or intermediate product flow.
    In case of triangular uncertainty distribution, the meanValue shall be calculated from the mostLikelyValue. The field mostLikelyValue (#3797) shall not be used in the ecoinvent quality network.
    uncertaintyType -- Defines the kind of uncertainty distribution applied on one particular exchange. Lognormal distribution is default, normal, triangular or uniform distribution may be chosen if appropriate.
    standardDeviation95 -- Defines the 2.5% and the 97.5% value for the uncertainty range with normal and lognormal distribution.
    For lognormal distribution the square of the geometric standard deviation (SDg^2) is entered. SDg^2 is dimensionless. MeanValue times SDg^2 equals the 97.5% value (=maxValue), meanvalue divided by SDg^2 equals the 2.5% value (=minValue).
    For normal distribution the double standard deviation (2*SD) is entered. 2*SD is given in the same unit like the meanValue. MeanValue plus 2*SD equals 97.5% value (=maxValue), meanValue minus 2*SD equals 2.5% value (=minValue).
    This data field remains empty when uniform or triangular uncertainty distribution is applied (uncertaintyType = 3 and 4, respectively).
    formula -- Chemical formula (e.g. sum formula) may be entered. No graphs are allowed to represent chemical formulas.
    referenceToSource -- An ID used in the area 'sources' of the respective dataset is required. It indicates the publication (of the ecoinvent quality network) where the unit process raw data at issue and the characterisation, damage or weighting factors of an impact category, respectively, are documented.
    pageNumbers -- The page numbers of the publication (of the ecoinvent quality network) where the exchanges of the unit process at issue are documented.
    generalComment -- A general comment can be made about each individual exchange (or characterisation, damage or weighting factor) of a particular unit process and impact category, respectively.
    It contains the string of code numbers of the ecoinvent uncertainty assessment (if pedigree matrix is applied) as well as further comments about the uncertainty assessment.
    The string of numbers of the uncertainty assessment describes (reliability, completeness, temporal correlation, geographical correlation, further technical correlation, sample size) and uses a score from 1 to 5. See methodology report for further information.
    localName -- Name of the exchange (or characterisation, damage or weighting factor) of a particular unit process and impact category, respectively (in German local language).
    infrastructureProcess -- Describes whether the intermediate product flow from or to the unit process is an infrastructure process or not.
    Not applicable to elementary flows.
    minValue -- Contains the minimum value for exchange data with a uniform or triangular distribution.
    In case of LCI results imported into the ecoinvent database, the 2.5% value is reported in this field.
    maxValue -- Contains the maximum value for exchange data with a uniform or triangular distribution.
    In case of LCI results imported into the ecoinvent database, the 97.5% value is reported in this field.
    mostLikelyValue -- In some cases the MostLikelyValue is available for exhange data with triangular distribution. However, do not use this field, but calculate the mean value, (minValue + mostLikelyValue +maxValue)/3, and enter it into the field "meanValue").
    inputGroup -- Indicates the kind of input flow.
    The codes are: 1=Materials/Fuels, 2=Electricity/Heat, 3=Services, 4=FromNature, 5=FromTechnosphere.
    Within the ecoinvent quality network, only 4 and 5 are actively used (any material, fuel, electricity, heat or service is classified as an input from technosphere).
    outputGroup -- Indicates the kind of output flow.
    The codes are: 0=ReferenceProduct, 1=Include avoided product system, 2=Allocated by product, 3=WasteToTreatment, 4=ToNature.
    The options 0, 2, and 4 are actively used in the ecoinvent quality network.
    Products of multioutput processes are classified as allocated by-products (2).
    Avoided product systems are modelled with a negative input from technosphere. WasteToTreatment are modelled like services (hence inputFromTechnosphere). Therefore codes '1' and '3' are not required.

    """

    def __init__(
        self,
        number=None,
        category=None,
        subCategory=None,
        localCategory=None,
        localSubCategory=None,
        CASNumber=None,
        name=None,
        location=None,
        unit=None,
        meanValue=None,
        uncertaintyType=None,
        standardDeviation95=None,
        formula=None,
        referenceToSource=None,
        pageNumbers=None,
        generalComment=None,
        localName=None,
        infrastructureProcess=None,
        minValue=None,
        maxValue=None,
        mostLikelyValue=None,
        inputGroup=None,
        outputGroup=None,
        gds_collector=None,
        **kwargs
    ):
        self.gds_collector = gds_collector
        self.gds_elementtree_node = None
        self.original_tagname = None
        self.parent_object = kwargs.get("parent_object")
        self.number = _cast(int, number)
        self.category = _cast(None, category)
        self.subCategory = _cast(None, subCategory)
        self.localCategory = _cast(None, localCategory)
        self.localSubCategory = _cast(None, localSubCategory)
        self.CASNumber = _cast(None, CASNumber)
        self.name = _cast(None, name)
        self.location = _cast(None, location)
        self.unit = _cast(None, unit)
        self.meanValue = _cast(float, meanValue)
        self.uncertaintyType = _cast(int, uncertaintyType)
        self.standardDeviation95 = _cast(float, standardDeviation95)
        self.formula = _cast(None, formula)
        self.referenceToSource = _cast(int, referenceToSource)
        self.pageNumbers = _cast(None, pageNumbers)
        self.generalComment = _cast(None, generalComment)
        self.localName = _cast(None, localName)
        self.infrastructureProcess = _cast(bool, infrastructureProcess)
        self.minValue = _cast(float, minValue)
        self.maxValue = _cast(float, maxValue)
        self.mostLikelyValue = _cast(float, mostLikelyValue)
        self.inputGroup = inputGroup
        self.validate_inputGroupType(self.inputGroup)
        self.outputGroup = outputGroup
        self.validate_outputGroupType(self.outputGroup)

    def validate_inputGroupType(self, value):
        result = True
        # Validate type inputGroupType, a restriction on xsd:integer.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on inputGroupType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 5:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on inputGroupType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
        return result

    def validate_outputGroupType(self, value):
        result = True
        # Validate type outputGroupType, a restriction on xsd:integer.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on outputGroupType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 4:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on outputGroupType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
        return result

    def validate_TIndexNumber(self, value):
        # Validate type TIndexNumber, a restriction on xsd:int.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TIndexNumber'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_TCategoryName(self, value):
        # Validate type TCategoryName, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCategoryName'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TCategoryName'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_CASNumberType1(self, value):
        # Validate type CASNumberType1, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) != 11:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on CASNumberType1'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
            if not self.gds_validate_simple_patterns(
                self.validate_CASNumberType1_patterns_, value
            ):
                self.gds_collector.add_message(
                    'Value "%s" does not match xsd pattern restrictions: %s'
                    % (
                        encode_str_2_3(value),
                        self.validate_CASNumberType1_patterns_,
                    )
                )

    validate_CASNumberType1_patterns_ = [["^(\\d{6,6}-\\d{2,2}-\\d)$"]]

    def validate_TString80(self, value):
        # Validate type TString80, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 80:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString80'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TRegionalCode(self, value):
        # Validate type TRegionalCode, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TRegionalCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TUnit(self, value):
        # Validate type TUnit, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TUnit'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TFloatNumber(self, value):
        # Validate type TFloatNumber, a restriction on xsd:double.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (float)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass

    def validate_uncertaintyTypeType(self, value):
        # Validate type uncertaintyTypeType, a restriction on xsd:integer.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on uncertaintyTypeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False
            if value > 4:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on uncertaintyTypeType'
                    % {"value": value, "lineno": lineno}
                )
                result = False

    def validate_TString40(self, value):
        # Validate type TString40, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString40'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TString30(self, value):
        # Validate type TString30, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString30'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def validate_TString32000(self, value):
        # Validate type TString32000, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes
            and self.gds_collector is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) > 32000:
                lineno = self.gds_get_node_lineno()
                self.gds_collector.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TString32000'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def _hasContent(self):
        if self.inputGroup is not None or self.outputGroup is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="Exchange",
        pretty_print=True,
    ):
        imported_ns_def = GenerateDSNamespaceDefs.get("Exchange")
        if imported_ns_def is not None:
            namespacedef = imported_ns_def
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.original_tagname is not None and name == "Exchange":
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
            outfile, level, already_processed, namespaceprefix, name="Exchange"
        )
        if self._hasContent():
            outfile.write(">%s" % (eol,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix,
                namespacedef,
                name="Exchange",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix, name, eol))
        else:
            outfile.write("/>%s" % (eol,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix="", name="Exchange"
    ):
        if self.number is not None and "number" not in already_processed:
            already_processed.add("number")
            outfile.write(
                ' number="%s"'
                % self.gds_format_integer(self.number, input_name="number")
            )
        if self.category is not None and "category" not in already_processed:
            already_processed.add("category")
            outfile.write(
                " category=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.category), input_name="category"
                        )
                    ),
                )
            )
        if self.subCategory is not None and "subCategory" not in already_processed:
            already_processed.add("subCategory")
            outfile.write(
                " subCategory=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.subCategory), input_name="subCategory"
                        )
                    ),
                )
            )
        if self.localCategory is not None and "localCategory" not in already_processed:
            already_processed.add("localCategory")
            outfile.write(
                " localCategory=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.localCategory), input_name="localCategory"
                        )
                    ),
                )
            )
        if (
            self.localSubCategory is not None
            and "localSubCategory" not in already_processed
        ):
            already_processed.add("localSubCategory")
            outfile.write(
                " localSubCategory=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.localSubCategory),
                            input_name="localSubCategory",
                        )
                    ),
                )
            )
        if self.CASNumber is not None and "CASNumber" not in already_processed:
            already_processed.add("CASNumber")
            outfile.write(
                " CASNumber=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.CASNumber), input_name="CASNumber"
                        )
                    ),
                )
            )
        if self.name is not None and "name" not in already_processed:
            already_processed.add("name")
            outfile.write(
                " name=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.name), input_name="name"
                        )
                    ),
                )
            )
        if self.location is not None and "location" not in already_processed:
            already_processed.add("location")
            outfile.write(
                " location=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.location), input_name="location"
                        )
                    ),
                )
            )
        if self.unit is not None and "unit" not in already_processed:
            already_processed.add("unit")
            outfile.write(
                " unit=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.unit), input_name="unit"
                        )
                    ),
                )
            )
        if self.meanValue is not None and "meanValue" not in already_processed:
            already_processed.add("meanValue")
            outfile.write(
                ' meanValue="%s"'
                % self.gds_format_double(self.meanValue, input_name="meanValue")
            )
        if (
            self.uncertaintyType is not None
            and "uncertaintyType" not in already_processed
        ):
            already_processed.add("uncertaintyType")
            outfile.write(
                ' uncertaintyType="%s"'
                % self.gds_format_integer(
                    self.uncertaintyType, input_name="uncertaintyType"
                )
            )
        if (
            self.standardDeviation95 is not None
            and "standardDeviation95" not in already_processed
        ):
            already_processed.add("standardDeviation95")
            outfile.write(
                ' standardDeviation95="%s"'
                % self.gds_format_double(
                    self.standardDeviation95, input_name="standardDeviation95"
                )
            )
        if self.formula is not None and "formula" not in already_processed:
            already_processed.add("formula")
            outfile.write(
                " formula=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.formula), input_name="formula"
                        )
                    ),
                )
            )
        if (
            self.referenceToSource is not None
            and "referenceToSource" not in already_processed
        ):
            already_processed.add("referenceToSource")
            outfile.write(
                ' referenceToSource="%s"'
                % self.gds_format_integer(
                    self.referenceToSource, input_name="referenceToSource"
                )
            )
        if self.pageNumbers is not None and "pageNumbers" not in already_processed:
            already_processed.add("pageNumbers")
            outfile.write(
                " pageNumbers=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.pageNumbers), input_name="pageNumbers"
                        )
                    ),
                )
            )
        if (
            self.generalComment is not None
            and "generalComment" not in already_processed
        ):
            already_processed.add("generalComment")
            outfile.write(
                " generalComment=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.generalComment),
                            input_name="generalComment",
                        )
                    ),
                )
            )
        if self.localName is not None and "localName" not in already_processed:
            already_processed.add("localName")
            outfile.write(
                " localName=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.localName), input_name="localName"
                        )
                    ),
                )
            )
        if (
            self.infrastructureProcess is not None
            and "infrastructureProcess" not in already_processed
        ):
            already_processed.add("infrastructureProcess")
            outfile.write(
                ' infrastructureProcess="%s"'
                % self.gds_format_boolean(
                    self.infrastructureProcess, input_name="infrastructureProcess"
                )
            )
        if self.minValue is not None and "minValue" not in already_processed:
            already_processed.add("minValue")
            outfile.write(
                ' minValue="%s"'
                % self.gds_format_double(self.minValue, input_name="minValue")
            )
        if self.maxValue is not None and "maxValue" not in already_processed:
            already_processed.add("maxValue")
            outfile.write(
                ' maxValue="%s"'
                % self.gds_format_double(self.maxValue, input_name="maxValue")
            )
        if (
            self.mostLikelyValue is not None
            and "mostLikelyValue" not in already_processed
        ):
            already_processed.add("mostLikelyValue")
            outfile.write(
                ' mostLikelyValue="%s"'
                % self.gds_format_double(
                    self.mostLikelyValue, input_name="mostLikelyValue"
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix="",
        namespacedef='xmlns:es="http://www.EcoInvent.org/EcoSpold01" xmlns:None="http://www.EcoInvent.org/EcoSpold01" ',
        name="Exchange",
        fromsubclass=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol = "\n"
        else:
            eol = ""
        if self.inputGroup is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sinputGroup>%s</%sinputGroup>%s"
                % (
                    namespaceprefix,
                    self.gds_format_integer(self.inputGroup, input_name="inputGroup"),
                    namespaceprefix,
                    eol,
                )
            )
        if self.outputGroup is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%soutputGroup>%s</%soutputGroup>%s"
                % (
                    namespaceprefix,
                    self.gds_format_integer(self.outputGroup, input_name="outputGroup"),
                    namespaceprefix,
                    eol,
                )
            )

    def build(self, node, gds_collector=None):
        self.gds_collector = gds_collector
        if SaveElementTreeNode:
            self.gds_elementtree_node = node
        already_processed = set()
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName = tag_pattern.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName, gds_collector=gds_collector)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value("number", node)
        if value is not None and "number" not in already_processed:
            already_processed.add("number")
            self.number = self.gds_parse_integer(value, node, "number")
            self.validate_TIndexNumber(self.number)  # validate type TIndexNumber
        value = find_attr_value("category", node)
        if value is not None and "category" not in already_processed:
            already_processed.add("category")
            self.category = value
            self.validate_TCategoryName(self.category)  # validate type TCategoryName
        value = find_attr_value("subCategory", node)
        if value is not None and "subCategory" not in already_processed:
            already_processed.add("subCategory")
            self.subCategory = value
            self.validate_TCategoryName(self.subCategory)  # validate type TCategoryName
        value = find_attr_value("localCategory", node)
        if value is not None and "localCategory" not in already_processed:
            already_processed.add("localCategory")
            self.localCategory = value
            self.validate_TCategoryName(
                self.localCategory
            )  # validate type TCategoryName
        value = find_attr_value("localSubCategory", node)
        if value is not None and "localSubCategory" not in already_processed:
            already_processed.add("localSubCategory")
            self.localSubCategory = value
            self.validate_TCategoryName(
                self.localSubCategory
            )  # validate type TCategoryName
        value = find_attr_value("CASNumber", node)
        if value is not None and "CASNumber" not in already_processed:
            already_processed.add("CASNumber")
            self.CASNumber = value
            self.validate_CASNumberType1(self.CASNumber)  # validate type CASNumberType1
        value = find_attr_value("name", node)
        if value is not None and "name" not in already_processed:
            already_processed.add("name")
            self.name = value
            self.validate_TString80(self.name)  # validate type TString80
        value = find_attr_value("location", node)
        if value is not None and "location" not in already_processed:
            already_processed.add("location")
            self.location = value
            self.validate_TRegionalCode(self.location)  # validate type TRegionalCode
        value = find_attr_value("unit", node)
        if value is not None and "unit" not in already_processed:
            already_processed.add("unit")
            self.unit = value
            self.validate_TUnit(self.unit)  # validate type TUnit
        value = find_attr_value("meanValue", node)
        if value is not None and "meanValue" not in already_processed:
            already_processed.add("meanValue")
            value = self.gds_parse_double(value, node, "meanValue")
            self.meanValue = value
            self.validate_TFloatNumber(self.meanValue)  # validate type TFloatNumber
        value = find_attr_value("uncertaintyType", node)
        if value is not None and "uncertaintyType" not in already_processed:
            already_processed.add("uncertaintyType")
            self.uncertaintyType = self.gds_parse_integer(
                value, node, "uncertaintyType"
            )
            self.validate_uncertaintyTypeType(
                self.uncertaintyType
            )  # validate type uncertaintyTypeType
        value = find_attr_value("standardDeviation95", node)
        if value is not None and "standardDeviation95" not in already_processed:
            already_processed.add("standardDeviation95")
            value = self.gds_parse_double(value, node, "standardDeviation95")
            self.standardDeviation95 = value
            self.validate_TFloatNumber(
                self.standardDeviation95
            )  # validate type TFloatNumber
        value = find_attr_value("formula", node)
        if value is not None and "formula" not in already_processed:
            already_processed.add("formula")
            self.formula = value
            self.validate_TString40(self.formula)  # validate type TString40
        value = find_attr_value("referenceToSource", node)
        if value is not None and "referenceToSource" not in already_processed:
            already_processed.add("referenceToSource")
            self.referenceToSource = self.gds_parse_integer(
                value, node, "referenceToSource"
            )
            self.validate_TIndexNumber(
                self.referenceToSource
            )  # validate type TIndexNumber
        value = find_attr_value("pageNumbers", node)
        if value is not None and "pageNumbers" not in already_processed:
            already_processed.add("pageNumbers")
            self.pageNumbers = value
            self.validate_TString30(self.pageNumbers)  # validate type TString30
        value = find_attr_value("generalComment", node)
        if value is not None and "generalComment" not in already_processed:
            already_processed.add("generalComment")
            self.generalComment = value
            self.validate_TString32000(
                self.generalComment
            )  # validate type TString32000
        value = find_attr_value("localName", node)
        if value is not None and "localName" not in already_processed:
            already_processed.add("localName")
            self.localName = value
            self.validate_TString80(self.localName)  # validate type TString80
        value = find_attr_value("infrastructureProcess", node)
        if value is not None and "infrastructureProcess" not in already_processed:
            already_processed.add("infrastructureProcess")
            if value in ("true", "1"):
                self.infrastructureProcess = True
            elif value in ("false", "0"):
                self.infrastructureProcess = False
            else:
                raise_parse_error(node, "Bad boolean attribute")
        value = find_attr_value("minValue", node)
        if value is not None and "minValue" not in already_processed:
            already_processed.add("minValue")
            value = self.gds_parse_double(value, node, "minValue")
            self.minValue = value
            self.validate_TFloatNumber(self.minValue)  # validate type TFloatNumber
        value = find_attr_value("maxValue", node)
        if value is not None and "maxValue" not in already_processed:
            already_processed.add("maxValue")
            value = self.gds_parse_double(value, node, "maxValue")
            self.maxValue = value
            self.validate_TFloatNumber(self.maxValue)  # validate type TFloatNumber
        value = find_attr_value("mostLikelyValue", node)
        if value is not None and "mostLikelyValue" not in already_processed:
            already_processed.add("mostLikelyValue")
            value = self.gds_parse_double(value, node, "mostLikelyValue")
            self.mostLikelyValue = value
            self.validate_TFloatNumber(
                self.mostLikelyValue
            )  # validate type TFloatNumber

    def _buildChildren(
        self, child, node, nodeName, fromsubclass=False, gds_collector=None
    ):
        if nodeName == "inputGroup" and child.text:
            sval = child.text
            ival = self.gds_parse_integer(sval, node, "inputGroup")
            ival = self.gds_validate_integer(ival, node, "inputGroup")
            self.inputGroup = ival
            # validate type inputGroupType
            self.validate_inputGroupType(self.inputGroup)
        elif nodeName == "outputGroup" and child.text:
            sval = child.text
            ival = self.gds_parse_integer(sval, node, "outputGroup")
            ival = self.gds_validate_integer(ival, node, "outputGroup")
            self.outputGroup = ival
            # validate type outputGroupType
            self.validate_outputGroupType(self.outputGroup)


# end class Exchange
