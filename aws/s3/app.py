import boto3
import sys

def main(args):
    bucket = args[0]
    path = args[1]
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    total_size = 0

    for obj in my_bucket.objects.filter(Prefix=path):
        total_size = total_size + obj.size

    size = str(round(int(total_size)/(1024*1024*1000),4)) + "GB"
    print("Size of prefix " + path +" in bucket " + bucket + " is " + size)
    return total_size

if __name__ == "__main__":
    main(sys.argv[1:])
