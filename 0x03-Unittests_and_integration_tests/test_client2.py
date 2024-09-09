#!/usr/bin/env python3


from fixtures import TEST_PAYLOAD


#print(TEST_PAYLOAD)
print(type(TEST_PAYLOAD))

org_payload = dict(TEST_PAYLOAD[0])

#print("index_0", index_0)
print("type of org_payload", type(org_payload))

repos_url = org_payload[0]["repos_url"]

print("the repos_url returned by  _public_repos_ur is", repos_url)

repos_payload = org_payload[1]

print("the repos_payload is ", repos_payload)

expected_repos = org_payload[2]

print("the expected_repos is", expected_repos)
