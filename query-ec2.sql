SELECT
    resourceId,
    resourceName,
    resourceType,
    configuration.instanceType,
    availabilityZone,
    configuration.state.name,
    configuration.privateIpAddress
WHERE
    resourceType = 'AWS::EC2::Instance'