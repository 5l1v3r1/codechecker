# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------


from codechecker_report_converter.analyzer_result import AnalyzerResult
from codechecker_report_converter.plist_converter import PlistConverter

from .output_parser import MSANParser


class MSANAnalyzerResult(AnalyzerResult):
    """ Transform analyzer result of Clang MemorySanitizer. """

    TOOL_NAME = 'msan'

    def parse(self, analyzer_result):
        """ Creates plist files from the given analyzer result to the given
        output directory.
        """
        parser = MSANParser()

        content = self._get_analyzer_result_file_content(analyzer_result)
        messages = parser.parse_messages(content)

        plist_converter = PlistConverter(self.TOOL_NAME)
        plist_converter.add_messages(messages)
        return plist_converter.get_plist_results()
