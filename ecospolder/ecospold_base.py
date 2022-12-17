import base64
import datetime as date_t
import decimal
from decimal import Decimal
import os
import re
import sys
from io import StringIO
from lxml import etree as etre
from typing import List
import time
from io import TextIOBase
import typing

try:
    ModulenotfoundExp = ModuleNotFoundError
except NameError:
    ModulenotfoundExp = ImportError

# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS = True
CapturedNsmap = {}
tag_pattern = re.compile(r"({.*})?(.*)")
CDATA_pattern = re.compile(r"<!\[CDATA\[.*?\]\]>", re.DOTALL)

if sys.version_info.major == 2:
    BaseStrType = basestring
else:
    BaseStrType = str

Validate_simpletypes = True
SaveElementTreeNode = True
TagNamePrefix = ""

try:
    from enum import Enum
except ModulenotfoundExp:
    Enum = object

CurrentSubclassModule = None

def cast_value_with_type(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

class CollectorClass(object):
    def __init__(self, messages=None) -> None:
        self.messages = [] if messages is None else messages

    def add_message(self, msg: str) -> None:
        self.messages.append(msg)

    def get_messages(self) -> str:
        return self.messages

    def clear_messages(self) -> None:
        self.messages = []

    def print_messages(self) -> None:
        for msg in self.messages:
            print("Warning: {}".format(msg))

    def write_messages(self, outstream) -> None:
        for msg in self.messages:
            outstream.write("Warning: {}\n".format(msg))


class EcospoldBase:
    tzoff_pattern = re.compile(r"(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$")

    class _FixedOffsetTZ(date_t.tzinfo):
        def __init__(self, offset, name) -> None:
            self.__offset = date_t.timedelta(minutes=offset)
            self.__name = name

        def utcoffset(self) -> date_t.timedelta:
            return self.__offset

        def tzname(self) -> str:
            return self.__name

        def dst(self) -> None:
            return None

    def __str__(self) -> str:
        settings = {
            "str_pretty_print": True,
            "str_indent_level": 0,
            "str_namespaceprefix": "",
            "str_name": self.__class__.__name__,
            "str_namespacedefs": "",
        }
        for n in settings:
            if hasattr(self, n):
                settings[n] = getattr(self, n)
        output = StringIO()
        self.export(
            output,
            settings["str_indent_level"],
            pretty_print=settings["str_pretty_print"],
            namespaceprefix=settings["str_namespaceprefix"],
            name=settings["str_name"],
            namespacedef=settings["str_namespacedefs"],
        )
        strval = output.getvalue()
        output.close()
        return strval

    def format_string(self, input_data : str, input_name : str) -> str:
        return input_data

    def parse_string(self, input_data : str, node=None, input_name="") -> str:
        return input_data

    def validate_string(self, input_data : str, node=None, input_name="") -> str:
        if not input_data:
            return ""
        else:
            return input_data

    def format_integer(self, input_data : int, input_name="") -> str:
        return "%d" % int(input_data)

    def parse_integer(self, input_data : int, node=None, input_name="") -> int:
        try:
            ival = int(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, "Requires integer value: %s" % exp)
        return ival

    def validate_integer(self, input_data : int, node=None, input_name="") -> int:
        try:
            value = int(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, "Requires integer value")
        return value

    def format_integer_list(self, input_data : List[int], input_name="") -> str:
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType):
            input_data = [str(s) for s in input_data]
        return "%s" % " ".join(input_data)

    def validate_integer_list(self, input_data : List[int], node=None, input_name="") -> List[int]:
        values = input_data.split()
        for value in values:
            try:
                int(value)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires sequence of integer values")
        return values

    def format_float(self, input_data : float, input_name="") -> str:
        return ("%.15f" % float(input_data)).rstrip("0")

    def parse_float(self, input_data : float, node=None, input_name="") -> float:
        try:
            fval = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, "Requires float or double value: %s" % exp)
        return fval

    def validate_float(self, input_data : float, node=None, input_name="") -> float:
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, "Requires float value")
        return value

    def format_float_list(self, input_data : List[float], input_name="") -> str:
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType):
            input_data = [str(s) for s in input_data]
        return "%s" % " ".join(input_data)

    def validate_float_list(self, input_data : List[float], node=None, input_name="") -> List[float]:
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires sequence of float values")
        return values

    def format_decimal(self, input_data : Decimal, input_name="") -> str:
        return_value = "%s" % input_data
        if "." in return_value:
            return_value = return_value.rstrip("0")
            if return_value.endswith("."):
                return_value = return_value.rstrip(".")
        return return_value

    def parse_decimal(self, input_data : Decimal, node=None, input_name="") -> Decimal:
        try:
            decimal_value = Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, "Requires decimal value")
        return decimal_value

    def validate_decimal(self, input_data : Decimal, node=None, input_name="") -> Decimal:
        try:
            value = Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, "Requires decimal value")
        return value

    def format_decimal_list(self, input_data : List[Decimal], input_name="") -> str:
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType):
            input_data = [str(s) for s in input_data]
        return " ".join([self.format_decimal(item) for item in input_data])

    def validate_decimal_list(self, input_data : List[Decimal], node=None, input_name="") -> List[Decimal]:
        values = input_data.split()
        for value in values:
            try:
                Decimal(value)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires sequence of decimal values")
        return values

    def format_double(self, input_data : float, input_name="") -> str:
        return "%s" % input_data

    def parse_double(self, input_data : float, node=None, input_name="") -> float:
        try:
            fval = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, "Requires double or float value: %s" % exp)
        return fval

    def validate_double(self, input_data : float, node=None, input_name="") -> float:
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, "Requires double or float value")
        return value

    def format_double_list(self, input_data : List[float], input_name="") -> str:
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType):
            input_data = [str(s) for s in input_data]
        return "%s" % " ".join(input_data)

    def validate_double_list(self, input_data : List[float], node=None, input_name="") -> List[float]:
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires sequence of double or float values")
        return values

    def format_boolean(self, input_data, input_name="") -> str:
        return ("%s" % input_data).lower()

    def parse_boolean(self, input_data : str, node=None, input_name="") -> bool:
        input_data = input_data.strip()
        if input_data in ("true", "1"):
            bval = True
        elif input_data in ("false", "0"):
            bval = False
        else:
            raise_parse_error(node, "Requires boolean value")
        return bval

    def validate_boolean(self, input_data : bool, node=None, input_name="") -> bool:
        if input_data not in (
            True,
            1,
            False,
            0,
        ):
            raise_parse_error(
                node, "Requires boolean value " "(one of True, 1, False, 0)"
            )
        return input_data

    def format_boolean_list(self, input_data : List[str], input_name="") -> str:
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType):
            input_data = [str(s) for s in input_data]
        return "%s" % " ".join(input_data)

    def validate_boolean_list(self, input_data : List[bool], node=None, input_name="") -> List[bool]:
        values = input_data.split()
        for value in values:
            value = self.parse_boolean(value, node, input_name)
            if value not in (
                True,
                1,
                False,
                0,
            ):
                raise_parse_error(
                    node,
                    "Requires sequence of boolean values " "(one of True, 1, False, 0)",
                )
        return values

    def validate_datetime(self, input_data : date_t, node=None, input_name="") -> date_t:
        return input_data

    def format_datetime(self, input_data : date_t, input_name="") -> str:
        if input_data.microsecond == 0:
            _svalue = "%04d-%02d-%02dT%02d:%02d:%02d" % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = "%04d-%02d-%02dT%02d:%02d:%02d.%s" % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ("%f" % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += "Z"
                else:
                    if total_seconds < 0:
                        _svalue += "-"
                        total_seconds *= -1
                    else:
                        _svalue += "+"
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += "{0:02d}:{1:02d}".format(hours, minutes)
        return _svalue

    @classmethod
    def parse_datetime(cls, input_data : str) -> date_t.datetime:
        tz = None
        if input_data[-1] == "Z":
            tz = EcospoldBase._FixedOffsetTZ(0, "UTC")
            input_data = input_data[:-1]
        else:
            results = EcospoldBase.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(":")
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == "-":
                    tzoff *= -1
                tz = EcospoldBase._FixedOffsetTZ(tzoff, results.group(0))
                input_data = input_data[:-6]
        time_parts = input_data.split(".")
        if len(time_parts) > 1:
            micro_seconds = int(float("0." + time_parts[1]) * 1000000)
            input_data = "%s.%s" % (
                time_parts[0],
                "{}".format(micro_seconds).rjust(6, "0"),
            )
            dt = date_t.datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            dt = date_t.datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S")
        dt = dt.replace(tzinfo=tz)
        return dt

    def validate_date(self, input_data : date_t, node=None, input_name="") -> date_t:
        return input_data

    def format_date(self, input_data : date_t, input_name="") -> str:
        _svalue = "%04d-%02d-%02d" % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += "Z"
                    else:
                        if total_seconds < 0:
                            _svalue += "-"
                            total_seconds *= -1
                        else:
                            _svalue += "+"
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += "{0:02d}:{1:02d}".format(hours, minutes)
        except AttributeError:
            pass
        return _svalue

    @classmethod
    def parse_date(cls, input_data : str) -> date_t.date:
        tz = None
        if input_data[-1] == "Z":
            tz = EcospoldBase._FixedOffsetTZ(0, "UTC")
            input_data = input_data[:-1]
        else:
            results = EcospoldBase.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(":")
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == "-":
                    tzoff *= -1
                tz = EcospoldBase._FixedOffsetTZ(tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = date_t.datetime.strptime(input_data, "%Y-%m-%d")
        dt = dt.replace(tzinfo=tz)
        return dt.date()

    def validate_time(self, input_data : str, node=None, input_name="") -> str:
        return input_data

    def format_time(self, input_data : date_t.time, input_name="") -> str:
        if input_data.microsecond == 0:
            _svalue = "%02d:%02d:%02d" % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = "%02d:%02d:%02d.%s" % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ("%f" % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += "Z"
                else:
                    if total_seconds < 0:
                        _svalue += "-"
                        total_seconds *= -1
                    else:
                        _svalue += "+"
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += "{0:02d}:{1:02d}".format(hours, minutes)
        return _svalue

    def validate_simple_patterns(self, patterns : List[str], target : str) -> bool:
        # pat is a list of lists of strings/patterns.
        # The target value must match at least one of the patterns
        # in order for the test to succeed.
        found1 = True
        target = str(target)
        for patterns1 in patterns:
            found2 = False
            for patterns2 in patterns1:
                mo = re.search(patterns2, target)
                if mo is not None and len(mo.group(0)) == len(target):
                    found2 = True
                    break
            if not found2:
                found1 = False
                break
        return found1

    @classmethod
    def parse_time(cls, input_data : str) -> date_t.time:
        tz = None
        if input_data[-1] == "Z":
            tz = EcospoldBase._FixedOffsetTZ(0, "UTC")
            input_data = input_data[:-1]
        else:
            results = EcospoldBase.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(":")
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == "-":
                    tzoff *= -1
                tz = EcospoldBase._FixedOffsetTZ(tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split(".")) > 1:
            dt = date_t.datetime.strptime(input_data, "%H:%M:%S.%f")
        else:
            dt = date_t.datetime.strptime(input_data, "%H:%M:%S")
        dt = dt.replace(tzinfo=tz)
        return dt.time()

    def check_cardinality(
        self, value : List[str], input_name : str, min_occurs=0, max_occurs=1, required=None
    ) -> None:
        if value is None:
            length = 0
        elif isinstance(value, list):
            length = len(value)
        else:
            length = 1
        if required is not None:
            if required and length < 1:
                self.collector.add_message(
                    "Required value {}{} is missing".format(
                        input_name, self.get_node_lineno()
                    )
                )
        if length < min_occurs:
            self.collector.add_message(
                "Number of values for {}{} is below "
                "the minimum allowed, "
                "expected at least {}, found {}".format(
                    input_name, self.get_node_lineno(), min_occurs, length
                )
            )
        elif length > max_occurs:
            self.collector.add_message(
                "Number of values for {}{} is above "
                "the maximum allowed, "
                "expected at most {}, found {}".format(
                    input_name, self.get_node_lineno(), max_occurs, length
                )
            )

    def validate_builtin_ST(
        self,
        validator,
        value,
        input_name,
        min_occurs=None,
        max_occurs=None,
        required=None,
    ) -> bool:
        if value is not None:
            try:
                validator(value, input_name=input_name)
            except ParseError as parse_error:
                self.collector.add_message(str(parse_error))
        return True

    def validate_defined_ST(
        self,
        validator,
        value,
        input_name,
        min_occurs=None,
        max_occurs=None,
        required=None,
    ) -> bool:
        if value is not None:
            try:
                validator(value)
            except ParseError as parse_error:
                self.collector.add_message(str(parse_error))
        return True

    def str_lower(self, instring : str) -> str:
        return instring.lower()

    def get_path(self, node) -> str:
        path_list = []
        self.get_path_list(node, path_list)
        path_list.reverse()
        path = "/".join(path_list)
        return path

    Tag_strip_pattern_ = re.compile(r"\{.*\}")

    def get_path_list(self, node, path_list) -> str:
        if node is None:
            return
        tag = EcospoldBase.Tag_strip_pattern_.sub("", node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list(node.getparent(), path_list)

    @staticmethod
    def encode(instring : str) -> str:
        if sys.version_info.major == 2:
            encoding = "utf-8"
            return instring.encode(encoding)
        else:
            return instring

    @staticmethod
    def convert_unicode(instring : str) -> str:
        if isinstance(instring, str):
            result = quote_xml(instring)
        elif sys.version_info.major == 2 and isinstance(instring, unicode):
            result = quote_xml(instring).encode("utf8")
        else:
            result = EcospoldBase.encode(str(instring))
        return result

    def get_node_lineno(self) -> str:
        if (
            hasattr(self, "elementtree_node")
            and self.elementtree_node is not None
        ):
            return " near line {}".format(self.elementtree_node.sourceline)
        else:
            return ""

def parsexml(infile : str, parser=None, **kwargs) -> object:
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etre.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etre.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etre.parse(infile, parser=parser, **kwargs)
    return doc

def showIndent(outfile, level : int, pretty_print=True) -> None:
    if pretty_print:
        for idx in range(level):
            outfile.write("    ")


def quote_xml(inStr : str) -> str:
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ""
    s1 = isinstance(inStr, BaseStrType) and inStr or "%s" % inStr
    s2 = ""
    pos = 0
    matchobjects = CDATA_pattern.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos : mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start() : mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr : str) -> str:
    s1 = inStr.replace("&", "&amp;")
    s1 = s1.replace("<", "&lt;")
    s1 = s1.replace(">", "&gt;")
    return s1


def quote_attrib(inStr : str) -> str:
    s1 = isinstance(inStr, BaseStrType) and inStr or "%s" % inStr
    s1 = s1.replace("&", "&amp;")
    s1 = s1.replace("<", "&lt;")
    s1 = s1.replace(">", "&gt;")
    s1 = s1.replace("\n", "&#10;")
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr : str) -> str:
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find("\n") == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find("\n") == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def find_attr_value(attr_name, node : object) -> object:
    attrs = node.attrib
    attr_parts = attr_name.split(":")
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == "xml":
            namespace = "http://www.w3.org/XML/1998/namespace"
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get(
                "{%s}%s"
                % (
                    namespace,
                    name,
                )
            )
    return value


def encode_str_2_3(instr : str) -> str:
    return instr


class ParseError(Exception):
    pass


def raise_parse_error(node : object, msg : str) -> None:
    if node is not None:
        msg = "%s (element %s/line %d)" % (
            msg,
            node.tag,
            node.sourceline,
        )
    raise ParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8

    def __init__(self, category : int, content_type : int, name : str, value : str) -> None:
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value

    def getCategory(self) -> int:
        return self.category

    def getContenttype(self, content_type) -> int:
        return self.content_type

    def getValue(self) -> str:
        return self.value

    def getName(self) -> str:
        return self.name

    def export(self, outfile : TextIOBase, level : int, name : str, namespace : str, pretty_print=True) -> None:
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:  # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name=name, pretty_print=pretty_print
            )

    def exportSimple(self, outfile : TextIOBase, level : int, name : str) -> None:
        if self.content_type == MixedContainer.TypeString:
            outfile.write("<%s>%s</%s>" % (self.name, self.value, self.name))
        elif (
            self.content_type == MixedContainer.TypeInteger
            or self.content_type == MixedContainer.TypeBoolean
        ):
            outfile.write("<%s>%d</%s>" % (self.name, self.value, self.name))
        elif (
            self.content_type == MixedContainer.TypeFloat
            or self.content_type == MixedContainer.TypeDecimal
        ):
            outfile.write("<%s>%f</%s>" % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write("<%s>%g</%s>" % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write(
                "<%s>%s</%s>" % (self.name, base64.b64encode(self.value), self.name)
            )

    def to_etree(self, element : typing.Any, mapping=None, reverse_mapping=None, nsmap=None) -> None:
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etre.SubElement(element, "%s" % self.name)
            subelement.text = self.to_etresimple()
        else:  # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)

    def to_etresimple(self, mapping=None, reverse_mapping=None, nsmap=None) -> str:
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (
            self.content_type == MixedContainer.TypeInteger
            or self.content_type == MixedContainer.TypeBoolean
        ):
            text = "%d" % self.value
        elif (
            self.content_type == MixedContainer.TypeFloat
            or self.content_type == MixedContainer.TypeDecimal
        ):
            text = "%f" % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = "%g" % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = "%s" % base64.b64encode(self.value)
        return text

    def exportLiteral(self, outfile : TextIOBase, level : int, name : str) -> None:
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value)
            )
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value)
            )
        else:  # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n'
                % (
                    self.category,
                    self.content_type,
                    self.name,
                )
            )
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(")\n")


class MemberSpec(object):
    def __init__(
        self,
        name="",
        data_type="",
        container=0,
        optional=0,
        child_attrs=None,
        choice=None,
    ) -> None:
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional

    def set_name(self, name : str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_data_type(self, data_type : str) -> None:
        self.data_type = data_type

    def get_data_type_chain(self) -> str:
        return self.data_type

    def get_data_type(self) -> str:
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return "xs:string"
        else:
            return self.data_type

    def set_container(self, container : int) -> None:
        self.container = container

    def get_container(self) -> int:
        return self.container

    def set_child_attrs(self, child_attrs : object) -> None:
        self.child_attrs = child_attrs

    def get_child_attrs(self) -> object:
        return self.child_attrs

    def set_choice(self, choice : object) -> None:
        self.choice = choice

    def get_choice(self) -> object:
        return self.choice

    def set_optional(self, optional : int) -> None:
        self.optional = optional

    def get_optional(self)  -> int:
        return self.optional
