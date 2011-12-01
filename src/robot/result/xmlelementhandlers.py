#  Copyright 2008-2011 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import with_statement

from robot.errors import DataError


class ElementStack(object):

    def __init__(self, result, root_element=None):
        self._results = [result]
        self._elements = [root_element or RootElement()]

    @property
    def _result(self):
        return self._results[-1]

    @property
    def _element(self):
        return self._elements[-1]

    def start(self, elem):
        self._elements.append(self._element.child_element(elem.tag))
        self._results.append(self._element.start(elem, self._result))

    def end(self, elem):
        self._elements.pop().end(elem, self._results.pop())
        elem.clear()


class _Element(object):
    tag = ''

    def start(self, elem, result):
        return result

    def end(self, elem, result):
        pass

    def child_element(self, tag):
        # TODO: replace _children() list with dict
        for child_type in self._children():
            if child_type.tag == tag:
                return child_type()
        raise DataError("Incompatible XML element '%s'" % tag)

    def _children(self):
        return []


class RootElement(_Element):

    def _children(self):
        return [RobotElement]


class RobotElement(_Element):
    tag = 'robot'

    def start(self, elem, result):
        result.generator = elem.get('generator', 'unknown').split()[0].upper()
        return result

    def _children(self):
        return [RootSuiteElement, StatisticsElement, ErrorsElement]


class SuiteElement(_Element):
    tag = 'suite'

    def start(self, elem, result):
        return result.suites.create(name=elem.get('name'),
                                    source=elem.get('source'))

    def _children(self):
        return [SuiteElement, DocElement, SuiteStatusElement,
                KeywordElement, TestCaseElement, MetadataElement]


class RootSuiteElement(SuiteElement):

    def start(self, elem, result):
        result.suite.name = elem.get('name')
        result.suite.source = elem.get('source')
        return result.suite


class TestCaseElement(_Element):
    tag = 'test'

    def start(self, elem, result):
        return result.tests.create(name=elem.get('name'),
                                   timeout=elem.get('timeout'))

    def _children(self):
        return [KeywordElement, TagsElement, DocElement, TestStatusElement]


class KeywordElement(_Element):
    tag = 'kw'

    def start(self, elem, result):
        return result.keywords.create(name=elem.get('name'),
                                      timeout=elem.get('timeout'),
                                      type=elem.get('type'))

    def _children(self):
        return [DocElement, ArgumentsElement, KeywordElement, MessageElement,
                KeywordStatusElement]


class MessageElement(_Element):
    tag = 'msg'

    def end(self, elem, result):
        html = elem.get('html', 'no') == 'yes'
        linkable = elem.get('linkable', 'no') == 'yes'
        result.messages.create(elem.text or '', elem.get('level'),
                               html, elem.get('timestamp'), linkable)


class _StatusElement(_Element):
    tag = 'status'

    def _set_status(self, elem, result):
        result.status = elem.get('status', 'FAIL')

    def _set_message(self, elem, result):
        result.message = elem.text or ''

    def _set_times(self, elem, result):
        result.starttime = elem.get('starttime', 'N/A')
        result.endtime = elem.get('endtime', 'N/A')


class KeywordStatusElement(_StatusElement):

    def end(self, elem, result):
        self._set_status(elem, result)
        self._set_times(elem, result)


class SuiteStatusElement(_StatusElement):

    def end(self, elem, result):
        self._set_message(elem, result)
        self._set_times(elem, result)


class TestStatusElement(_StatusElement):

    def end(self, elem, result):
        self._set_status(elem, result)
        self._set_message(elem, result)
        self._set_times(elem, result)


class DocElement(_Element):
    tag = 'doc'

    def end(self, elem, result):
        result.doc = elem.text or ''


class MetadataElement(_Element):
    tag = 'metadata'

    def _children(self):
        return [MetadataItemElement]


class MetadataItemElement(_Element):
    tag = 'item'

    def _children(self):
        return [MetadataItemElement]

    def end(self, elem, result):
        result.metadata[elem.get('name')] = elem.text or ''


class TagsElement(_Element):
    tag = 'tags'

    def _children(self):
        return [TagElement]


class TagElement(_Element):
    tag = 'tag'

    def end(self, elem, result):
        result.tags.add(elem.text or '')


class ArgumentsElement(_Element):
    tag = 'arguments'

    def _children(self):
        return [ArgumentElement]


class ArgumentElement(_Element):
    tag = 'arg'

    def end(self, elem, result):
        result.args.append(elem.text or '')


class ErrorsElement(_Element):
    tag = 'errors'

    def start(self, elem, result):
        return result.errors

    def _children(self):
        return [MessageElement]


class StatisticsElement(_Element):
    tag = 'statistics'

    def child_element(self, tag):
        return self