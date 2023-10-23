import * as cdk from 'aws-cdk-lib';
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class GitlinkedBackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const func = new lambda.DockerImageFunction(this, 'GitlinkedBackend', {
      code: lambda.DockerImageCode.fromImageAsset('./image'),
      memorySize: 1024,
      timeout: cdk.Duration.seconds(10),
    })

    const functionUrl = func.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.NONE,
      cors: {
        allowedMethods: [lambda.HttpMethod.ALL],
        allowedHeaders: ['*'],
        allowedOrigins: ['*'],
      }
    })

    new cdk.CfnOutput(this, 'FunctionUrl', {
      value: functionUrl.url,
    })

  }
}
