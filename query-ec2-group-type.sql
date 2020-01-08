SELECT
    configuration.instanceType,
    COUNT(*)
WHERE
    resourceType = 'AWS::EC2::Instance'
GROUP BY
    configuration.instanceType