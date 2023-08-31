#!/bin/bash
# this script takes a URL, sends a Get request along with a Header
curl -s -H "X-School-User-Id: 98" $1
