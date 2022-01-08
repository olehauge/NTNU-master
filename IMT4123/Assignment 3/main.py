import logging
import sys
import subprocess
from typing import List

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def test_scenarios():
    """
    A hard coded test of the 3 scenarios that the assignment asks us to test with.
    """
    logging.info("Trying to request a XACML authorization decision for the 3 scenarios that the "
                 "assignment asks us to test with")
    classpath: str = "sunxacml-1.2/lib/sunxacml.jar:sunxacml-1.2/lib/samples.jar"
    pdp_engine: str = "sunxacml-1.2/sample/src/SimplePDP.java"
    request1: str = "test-scenarios/case1Request.xml"
    policy1: str = "test-scenarios/case1Policy.xml"
    request2: str = "test-scenarios/case9Request.xml"
    policy2: str = "test-scenarios/case9Policy.xml"
    request3: str = "test-scenarios/case17Request.xml"
    policy3: str = "test-scenarios/case17Policy.xml"
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request1, policy1]
    subprocess.run(command)
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request2, policy2]
    subprocess.run(command)
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request3, policy3]
    subprocess.run(command)


def test_assignment_supplied_files():
    """
    A hard coded test of the policies and requests supplied with the assignment
    """
    logging.info("Trying to request a XACML authorization decision for the policies "
                 "and requests supplied with the assignment")
    classpath: str = "sunxacml-1.2/lib/sunxacml.jar:sunxacml-1.2/lib/samples.jar"
    pdp_engine: str = "sunxacml-1.2/sample/src/SimplePDP.java"
    request1: str = "policy-request/Request1.xml"
    policy1: str = "policy-request/Policy1.xml"
    request2: str = "policy-request/request2.xml"
    policy2: str = "policy-request/policy2.xml"
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request1, policy1]
    subprocess.run(command)
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request2, policy2]
    subprocess.run(command)


def test_cwp():
    """
    A hard coded test of the CWP with the CWP request file
    """
    logging.info("Trying to request a XACML authorization decision for the CWP policy")
    classpath: str = "sunxacml-1.2/lib/sunxacml.jar:sunxacml-1.2/lib/samples.jar"
    pdp_engine: str = "sunxacml-1.2/sample/src/SimplePDP.java"
    request: str = "chinese-wall-model/CWP_request.xml"
    policy: str = "chinese-wall-model/CWP.xml"
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request, policy]
    subprocess.run(command)


def test_blp():
    """
    A hard coded test of the BLP with the BLP request file
    """
    logging.info("Trying to request a XACML authorization decision for the BLP policy")
    classpath: str = "sunxacml-1.2/lib/sunxacml.jar:sunxacml-1.2/lib/samples.jar"
    pdp_engine: str = "sunxacml-1.2/sample/src/SimplePDP.java"
    request: str = "bell-lapadula-model/BLP_request.xml"
    policy: str = "bell-lapadula-model/BLP.xml"
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request, policy]
    subprocess.run(command)


def test_pdp_engine(request: str, policy: str):
    """
    A simple implementation of the sunxacml-1.2 API.
    Testing requests against policies are done by changing the ''request'' and ''policy'' variables.
    """
    logging.info("Trying to request a XACML authorization decision")
    classpath: str = "sunxacml-1.2/lib/sunxacml.jar:sunxacml-1.2/lib/samples.jar"
    pdp_engine: str = "sunxacml-1.2/sample/src/SimplePDP.java"
    command: List[str] = ["java", "-cp", classpath, pdp_engine, request, policy]
    subprocess.run(command)


if __name__ == "__main__":
    """
    This is a simple application to test the PDP engine and/or policy and request files. For simplicity, the various
    test files have been sorted into different functions which can be called from main. 
    
    If you want to test other files you can use the "test_pdp_engine()" function that is commented out below. 
    To do so just supply  the file path for the request and policy xml-files.
    
    Regarding all request files: the request xml-files have to be manually modified for testing various outcomes.
    """

    # test_pdp_engine("bell-lapadula-model/BLP_request.xml", "bell-lapadula-model/BLP.xml")

    test_assignment_supplied_files()  # For testing the PDP engine implementation with the supplied files
    test_scenarios()                  # For testing the PDP engine implementation with the scenario files
    test_blp()                        # For testing the BLP model
    test_cwp()                        # For testing the CWP model




