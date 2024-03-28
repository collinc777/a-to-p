
# fetch the url and write it to a file:
curl -s -o ./eden_schema.json https://api.edenai.run/v2/info/schema
# replace sucess with success:
sed -i '' 's/sucess/success/g' ./eden_schema.json
openapi-generator generate -i ./eden_schema.json -g python --skip-validate-spec -o ./openapi-output --library asyncio
# openapi-python-client generate --path ./eden_schema.json
rm -fr ./eden_schema.json
# caching issues happen with poetry. I don't know how to solve them

