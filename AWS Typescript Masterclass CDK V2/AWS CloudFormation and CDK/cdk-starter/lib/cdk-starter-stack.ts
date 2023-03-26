import * as cdk from 'aws-cdk-lib';
import { Duration } from 'aws-cdk-lib';
import { Bucket, CfnBucket } from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

// L3 construct
class L3Bucket extends Construct {
  constructor(scope: Construct, id: string, expiration: number) {
    super(scope, id)
    
    new Bucket( this, 'MyL3Bucket', {
      lifecycleRules: [{
        expiration: Duration.days(expiration)
      }]
    })
  }
}

export class CdkStarterStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // create an s3 bucket in 3 ways:
    // L2 construct
    new Bucket(this, 'MyL2Bucket', {
      lifecycleRules: [{
        expiration: Duration.days(2)
      }]
    })

    // L1 constrcut
    new CfnBucket(this, 'MyL1Bucket', {
      lifecycleConfiguration:{
        rules: [{
          expirationInDays: 1,
          status: 'Enabled'  // typo only will be revealed until last step of deployment
        }]
      }
    })

    // L3 construct
    new L3Bucket(this, 'MyL3Bucket', 3)
  }
}
