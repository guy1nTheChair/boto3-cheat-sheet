import boto3

def get_size(bucket, path):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    total_size = 0

    for obj in my_bucket.objects.filter(Prefix=path):
        total_size = total_size + obj.size

    print(int(total_size)/(1024*1024*1000))
    return total_size

get_size("ap-south-1-santosh", "youtube/")