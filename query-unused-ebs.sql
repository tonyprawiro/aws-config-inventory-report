SELECT
    resourceId,
    resourceType,
    configuration.volumeType,
    configuration.size,
    resourceCreationTime,
    configuration.encrypted,
    configuration.availabilityZone,
    configuration.state.value
WHERE
    resourceType = 'AWS::EC2::Volume'
    AND configuration.state.value <> 'in-use'