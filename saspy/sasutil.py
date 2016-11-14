#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
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
#
import logging
from saspy.sasproccommons import SASProcCommons


class SASutil:
    """
    This class is for SAS BASE procedures to be called as python3 objects and use SAS as the computational engine
    This class and all the useful work in this package require a licensed version of SAS.
    To add a new procedure do the following:
    1. Create a new method for the procedure
    2. Create the set of required statements. If there are no required statements then create an empty set {}
    3. Create the legal set of statements. This can often be obtained from the documentation of the procedure.
        'procopts' should always be included in the legal set to allow flexibility in calling the procedure.
    4. Create the doc string with the following parts at a minimum:
        A. Procedure Name
        B. Required set
        C. Legal set
        D. Link to the procedure documentation
    5. Add the return call for the method using an existing procedure as an example
    6. Verify that all the statements in the required and legal sets are listed in _makeProcCallMacro method
        of sasproccommons.py
    7. Write at least one test to exercise the procedures and include it in the appropriate testing file
    """
    def __init__(self, session, *args, **kwargs):
        """
        Submit an initial set of macros to prepare the SAS system
        """
        self.sasproduct = "util"
        # create logging
        # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.WARN)
        self.sas = session
        logging.debug("Initialization of SAS Macro: " + self.sas.saslog())

    def hpimpute(self, **kwargs: dict) -> object:
        """
        Python method to call the HPSPLIT procedure

        required_set = {}
        legal_set= {'cls', 'code', 'grow', 'id', 'model', 'out'
                    'partition', 'performance', 'prune', 'rules'}
        For more information on the statements see the Documentation link.
        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/stathpug/68163/HTML/default/viewer.htm#stathpug_hpsplit_syntax.htm
        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {'input'}
        legal_set = {'input', 'impute', 'performance', 'id', 'freq', 'code',
                     'procopts'}
        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "HPIMPUTE", required_set, legal_set, **kwargs)


    def hpbin(self, **kwargs: dict) -> object:
        """
        Python method to call the HPSPLIT procedure

        required_set = {}
        legal_set= {'cls', 'code', 'grow', 'id', 'model', 'out'
                    'partition', 'performance', 'prune', 'rules'}
        For more information on the statements see the Documentation link.
        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/stathpug/68163/HTML/default/viewer.htm#stathpug_hpsplit_syntax.htm
        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {}
        legal_set = {'code', 'id', 'performance', 'target', 'input', 'procopts'}
        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "HPBIN", required_set, legal_set, **kwargs)


    def hpsample(self, **kwargs: dict) -> object:
        """
        Python method to call the HPSPLIT procedure

        required_set = {}
        legal_set= {'cls', 'code', 'grow', 'id', 'model', 'out'
                    'partition', 'performance', 'prune', 'rules'}
        For more information on the statements see the Documentation link.
        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/stathpug/68163/HTML/default/viewer.htm#stathpug_hpsplit_syntax.htm
        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {}
        legal_set = { 'class', 'performance', 'target', 'var', 'procopts'}
        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "HPSAMPLE", required_set, legal_set, **kwargs)


        # def hpaccess(self, **kwargs: dict) -> object:
        # """
        # Python method to call the HPSPLIT procedure
        #
        # required_set = {}
        # legal_set= {'cls', 'code', 'grow', 'id', 'model', 'out'
        #             'partition', 'performance', 'prune', 'rules'}
        # For more information on the statements see the Documentation link.
        # cls is an alias for the class statement
        # Documentation link:
        # http://support.sas.com/documentation/cdl/en/stathpug/68163/HTML/default/viewer.htm#stathpug_hpsplit_syntax.htm
        # :param kwargs: dict
        # :return: SAS result object
        # """
        # required_set = {}
        # legal_set = {'cls', 'code', 'grow', 'id', 'model', 'out',
        #              'partition', 'performance', 'prune', 'rules', 'target', 'input', 'procopts'}
        # logging.debug("kwargs type: " + str(type(kwargs)))
        # return SASProcCommons._run_proc(self, "HPACCESS", required_set, legal_set, **kwargs)