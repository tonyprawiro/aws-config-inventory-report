SELECT
    resourceId,
    resourceType,
    configuration.runtime,
    configuration.lastModified,
    configuration.description
WHERE
    resourceType = 'AWS::Lambda::Function'