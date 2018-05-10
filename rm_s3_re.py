import sys
import boto3

session = boto3.session.Session(profile_name=sys.argv[1])
s3 = session.resource('s3')

for bucket in sys.argv[2:]:
    print("The below files will be removed:")
    for object in s3.Bucket(bucket).objects.all():
        print("{}".format(object.bucket_name + '/' + object.key))
    select = str(input("Do you want to continue: [Y/N] "))
    while (select != "Y") and (select != "N"):
        print(select)
        select = str(input("Do you want to continue: [Y/N] "))
    if select == "Y":
        s3.Bucket(bucket).objects.all().delete()
        s3.Bucket(bucket).delete()
        print("\nFiles and folders have been removed.")
        break
    elif select =="N":
        print("\nNo action will be done.")
        break
