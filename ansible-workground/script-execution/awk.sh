#!/bin/bash
awk  '{ if ( $6 == "Accepted" || $6 == "Failed" ) print }' auth.log

