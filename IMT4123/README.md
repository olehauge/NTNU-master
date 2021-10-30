# Assignment 3 - XACML implementation


## Testing
Downloaded and ran ```sunxacml``` with the provided test data. Had to set the ```CLASSPATH``` variable in the command line while running the application in order to make it run correctly. It was run from the ```sunxacml-1.2/sample``` directory.
```
java -cp ../lib/sunxacml.jar:../lib/samples.jar src/SimplePDP.java request/sensitive.xml policy/*.xml
```

Then I continued testing with the files supplied with the assignment and got the following results to see if it matched what I expected from reading the files myself.

**Testing Request1.xml against Policy1.xml:**
```
java -cp ../lib/sunxacml.jar:../lib/samples.jar src/SimplePDP.java policy-request/Request1.xml policy-request/Policy1.xml 
Note: src/SimplePDP.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
<Response>
  <Result ResourceID="http://medico.com/record/patient/BartSimpson">
    <Decision>Permit</Decision>
    <Status>
      <StatusCode Value="urn:oasis:names:tc:xacml:1.0:status:ok"/>
    </Status>
  </Result>
</Response>
```
**Testing request2.xml against policy2.xml:**
```
java -cp ../lib/sunxacml.jar:../lib/samples.jar src/SimplePDP.java policy-request/request2.xml policy-request/policy2.xml 
Note: src/SimplePDP.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
Oct 28, 2021 8:50:57 AM com.sun.xacml.finder.AttributeFinder findAttribute
INFO: Failed to resolve any values for urn:xacml:2.0:interop:example:resource:account-status
<Response>
  <Result ResourceID="CustomerAccount">
    <Decision>Deny</Decision>
    <Status>
      <StatusCode Value="urn:oasis:names:tc:xacml:1.0:status:ok"/>
    </Status>
    <Obligations>
      <Obligation ObligationId="urn:xacml:2.0:interop:example:obligation:status-code" FulfillOn="Deny">
      </Obligation>
      <Obligation ObligationId="urn:xacml:2.0:interop:example:obligation:decision" FulfillOn="Deny">
      </Obligation>
      <Obligation ObligationId="urn:xacml:2.0:interop:example:obligation:status-message" FulfillOn="Deny">
      </Obligation>
    </Obligations>
  </Result>
</Response>
```
