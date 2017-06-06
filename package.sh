rm aws_upload.zip

zip aws_upload.zip .app* .usr* lambda_function.py tweet_list.yml
pushd realdildotrump/lib/python2.7/site-packages
zip -r ../../../../aws_upload.zip *
popd
